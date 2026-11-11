#!/usr/bin/env python3
"""Proposal Meldingen Openbare Ruimte (Katwijk en Land van Cuijk, mei 2026) doorvoeren in de
EA-repository van het GGM (.qea = SQLite). Besluit 23e expertgroep, 12 augustus 2026; uitwerking in
tools/proposal-meldingen-openbare-ruimte.md.

Zelfde werkwijze als tools/fixes/fix_issue_57.py en tools/fixes/fix_issues_50_49_13.py: één transactie, standaard
een dry-run op een tijdelijke kopie, met --apply vastleggen in de echte .qea. Idempotent: een tweede
run meldt 0 wijzigingen. Enterprise Architect gesloten, back-up gemaakt.

Wat het script doet:
  1. AanvraagOfMelding (Model Dienstverlening): vier attributen met MIM-datatypes
     datumEersteReactie : DateTime, indicatieHogePrioriteit : Boolean,
     datumNormAfhandeling : DateTime, resultaat : CharacterString (Lengte 80).
  2. AanvraagOfMelding: twee relaties, 'behandelaar' naar Medewerker en 'behandelend team' naar
     OrganisatorischeEenheid (beide Model Kern RGBZ), 0..* - 0..1, stereotype Relatiesoort.
  3. MOR-AanvraagOfMelding: drie attributen adres : Adresaanduiding (groepattribuutsoort Kern RSGB),
     datumIngepland : DateTime, indicatieAnoniem : Boolean.
  4. Diagram 'MOR 2.0': Medewerker en OrganisatorischeEenheid erop, de twee relaties als link, en de
     nieuwe attributen in de zichtbare-attributenlijst van AanvraagOfMelding.
  Nieuwe attributen krijgen de MIM-tagset van een bestaand attribuut van dezelfde klasse, met
  Lengte, Herkomst en Datum opname gevuld.

Gebruik:
  python3 -I tools/fixes/fix_proposal_mor.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/fixes/fix_proposal_mor.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys
import tempfile
import uuid
from datetime import datetime

# --- Vaste punten in de v3.0.0-.qea (ea_guid, verwachte naam) ---------------------------------
AOM = ("{8E6BAEF8-1878-400f-9244-23575BD41EAB}", "AanvraagOfMelding")
MOR = ("{A9B89FF7-BCED-49fc-97A4-2A98BCED5B17}", "MOR-AanvraagOfMelding")
MEDEWERKER = ("{16EB3936-03CB-4854-9CD8-9F0911EEA51B}", "Medewerker")
ORG_EENHEID = ("{936A4E8B-3E5A-44b6-8A5D-EFB39F83FB6D}", "OrganisatorischeEenheid")
ADRESAANDUIDING = ("{C14C1D0E-2EE3-4d79-B7AB-BC0B7686FEF4}", "Adresaanduiding")
DT_BOOLEAN = ("{70FBDB70-4B81-46ab-97BB-058195812ECB}", "Boolean")
DT_CHARACTERSTRING = ("{18BFBA8D-E3F4-4d8c-9A8F-4429FA54B041}", "CharacterString")
DT_DATETIME = ("{366435A3-6E41-4add-A833-21873B97D7C7}", "DateTime")

TEMPLATE_ATTR_AOM = "{11348F20-D423-473f-B6E8-3197F6634F91}"  # datumAfhandeling
TEMPLATE_ATTR_MOR = "{3019043D-A904-4460-A5D4-1DB29675511B}"  # locatieOmschrijving
TEMPLATE_CONNECTOR = "{87F9EA19-0A1D-4c3f-ADCA-C8F48F216312}"  # 'kan leiden tot' (Source -> Destination)
DIAGRAM = ("{B3CC7874-57AA-4aeb-BF3F-98A64E9D76E5}", "MOR 2.0")  # in package Meldingen Openbare Ruimte › Diagram

HERKOMST = "Proposal Meldingen Openbare Ruimte, gemeenten Katwijk en Land van Cuijk (2026)"
DATUM_OPNAME = "4 november 2026"

# (naam, datatype, lengte, definitie)
ATTRS_AOM = [
    ("datumEersteReactie", DT_DATETIME, 0,
     "De datum en tijd waarop een behandelaar een eerste reactie op de aanvraag of melding heeft gegeven."),
    ("indicatieHogePrioriteit", DT_BOOLEAN, 0,
     "Indicatie of de aanvraag of melding met spoed opgepakt dient te worden."),
    ("datumNormAfhandeling", DT_DATETIME, 0,
     "De datum en tijd waarop volgens de geldende servicenorm redelijkerwijs verwacht mag worden dat de "
     "aanvraag of melding is behandeld (normtijd)."),
    ("resultaat", DT_CHARACTERSTRING, 80,
     "Het uiteindelijke resultaat van de aanvraag of melding, zoals opgelost of buiten behandeling gelaten."),
]
ATTRS_MOR = [
    ("adres", ADRESAANDUIDING, 0,
     "Het adres van de locatie waarop de melding betrekking heeft."),
    ("datumIngepland", DT_DATETIME, 0,
     "De datum en tijd waarop de behandeling van de melding is ingepland, bijvoorbeeld het uitvlakken van een "
     "stoep of het snoeien van een boom."),
    ("indicatieAnoniem", DT_BOOLEAN, 0,
     "Indicatie of de melding anoniem is gedaan."),
]
# (naam, doel, definitie)
RELATIONS = [
    ("behandelaar", MEDEWERKER, "De medewerker die de aanvraag of melding behandelt."),
    ("behandelend team", ORG_EENHEID,
     "De organisatorische eenheid (het team) waartoe de behandelaar van de aanvraag of melding behoort."),
]
# Plaats op het diagram (RectTop, RectLeft, RectRight, RectBottom), rechts van MOR-AanvraagOfMelding.
DIAGRAM_PLACES = {MEDEWERKER[0]: (-347, 453, 600, -475), ORG_EENHEID[0]: (-530, 453, 640, -658)}


def new_guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


def new_duid() -> str:
    return uuid.uuid4().hex[:8].upper()


def prefix(guid: str) -> str:
    """Zes tekens waarmee EA een element in diagramstijlen aanduidt (StyleEx SPL=...)."""
    return guid.strip("{")[:6].upper()


class Fixer:
    def __init__(self, conn: sqlite3.Connection):
        self.c = conn
        self.c.row_factory = sqlite3.Row
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changes = 0
        self.warnings: list[str] = []
        self.new_connectors: list[tuple[int, str, int]] = []  # (Connector_ID, naam, End_Object_ID)
        self.new_attr_guids_aom: list[str] = []

    def say(self, msg: str) -> None:
        print(f"    {msg}")

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)
        print(f"    LET OP: {msg}")

    def step(self, title: str) -> None:
        print(f"\n{title}")

    def one(self, sql: str, *params):
        return self.c.execute(sql, params).fetchone()

    def run(self, sql: str, *params) -> int:
        n = self.c.execute(sql, params).rowcount
        self.changes += n
        return n

    def insert(self, table: str, vals: dict) -> int:
        cols = list(vals)
        self.c.execute(f"INSERT INTO {table} ({', '.join(f'\"{k}\"' for k in cols)}) VALUES ({', '.join('?' * len(cols))})",
                       [vals[k] for k in cols])
        self.changes += 1
        return self.c.execute("SELECT last_insert_rowid()").fetchone()[0]

    def touch(self, object_id: int) -> None:
        self.c.execute("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", (self.now, object_id))

    def obj(self, ref: tuple[str, str]) -> int | None:
        guid, name = ref
        row = self.one("SELECT Object_ID, Name FROM t_object WHERE upper(ea_guid)=upper(?)", guid)
        if row is None or row["Name"] != name:
            self.warn(f"{name} ({guid}) niet gevonden of anders benoemd ({row['Name'] if row else '-'})")
            return None
        return row["Object_ID"]

    # -- attributen -----------------------------------------------------------------------
    def add_attributes(self, cls: tuple[str, str], template_guid: str, attrs: list) -> list[str]:
        self.step(f"Attributen op {cls[1]}")
        oid = self.obj(cls)
        if oid is None:
            return []
        tpl = self.one("SELECT * FROM t_attribute WHERE upper(ea_guid)=upper(?) AND Object_ID=?", template_guid, oid)
        if tpl is None:
            self.warn(f"sjabloonattribuut {template_guid} niet gevonden op {cls[1]}; overgeslagen")
            return []
        tpl_tags = self.c.execute("SELECT Property, VALUE, NOTES FROM t_attributetag WHERE ElementID=? ORDER BY PropertyID",
                                  (tpl["ID"],)).fetchall()
        tpl_xref = self.c.execute("SELECT * FROM t_xref WHERE upper(Client)=upper(?)", (tpl["ea_guid"],)).fetchall()
        pos = (self.one("SELECT MAX(Pos) FROM t_attribute WHERE Object_ID=?", oid)[0] or 0) + 1
        guids = []
        for name, (dt_guid, dt_name), length, note in attrs:
            existing = self.one("SELECT ea_guid, Type FROM t_attribute WHERE Object_ID=? AND Name=?", oid, name)
            if existing:
                self.say(f"al gedaan: {name} : {existing['Type']}")
                guids.append(existing["ea_guid"])
                continue
            dt_id = self.obj((dt_guid, dt_name))
            if dt_id is None:
                continue
            vals = {k: tpl[k] for k in tpl.keys() if k != "ID"}
            vals.update({"Name": name, "Type": dt_name, "Classifier": str(dt_id), "Length": length,
                         "Notes": note, "Pos": pos, "Default": "", "Style": "", "ea_guid": new_guid()})
            pos += 1
            new_id = self.insert("t_attribute", vals)
            overrides = {"Lengte": str(length) if length else "", "Herkomst": HERKOMST,
                         "Datum opname": DATUM_OPNAME, "Mogelijk geen waarde": "Ja"}
            for t in tpl_tags:
                self.insert("t_attributetag", {"ElementID": new_id, "Property": t["Property"],
                                               "VALUE": overrides.get(t["Property"], t["VALUE"]),
                                               "NOTES": t["NOTES"], "ea_guid": new_guid()})
            for x in tpl_xref:
                xvals = {k: x[k] for k in x.keys()}
                xvals.update({"XrefID": new_guid(), "Client": vals["ea_guid"]})
                self.insert("t_xref", xvals)
            guids.append(vals["ea_guid"])
            self.say(f"toegevoegd: {name} : {dt_name}{f' ({length})' if length else ''} op positie {vals['Pos']} "
                     f"({len(tpl_tags)} tags, {len(tpl_xref)} xref)")
            self.touch(oid)
        return guids

    # -- relaties -------------------------------------------------------------------------
    def add_relations(self) -> None:
        self.step("Relaties vanuit AanvraagOfMelding")
        oid = self.obj(AOM)
        if oid is None:
            return
        tpl = self.one("SELECT * FROM t_connector WHERE upper(ea_guid)=upper(?) AND Start_Object_ID=?", TEMPLATE_CONNECTOR, oid)
        if tpl is None:
            self.warn("sjabloonrelatie 'kan leiden tot' niet gevonden; relaties overgeslagen")
            return
        tpl_xref = self.c.execute("SELECT * FROM t_xref WHERE upper(Client)=upper(?)", (tpl["ea_guid"],)).fetchall()
        for name, target, note in RELATIONS:
            tid = self.obj(target)
            if tid is None:
                continue
            existing = self.one("SELECT Connector_ID FROM t_connector WHERE Start_Object_ID=? AND End_Object_ID=? "
                                "AND Connector_Type='Association' AND Name=?", oid, tid, name)
            if existing:
                self.say(f"al gedaan: {name} -> {target[1]}")
                self.new_connectors.append((existing["Connector_ID"], name, tid))
                continue
            vals = {k: tpl[k] for k in tpl.keys() if k != "Connector_ID"}
            vals.update({"Name": name, "Notes": note, "Direction": "Source -> Destination",
                         "SourceCard": "0..*", "DestCard": "0..1", "Btm_Start_Label": "0..*", "Btm_End_Label": "0..1",
                         "Top_Mid_Label": name, "Start_Object_ID": oid, "End_Object_ID": tid, "DiagramID": 0,
                         "ea_guid": new_guid()})
            cid = self.insert("t_connector", vals)
            for x in tpl_xref:
                xvals = {k: x[k] for k in x.keys()}
                xvals.update({"XrefID": new_guid(), "Client": vals["ea_guid"]})
                self.insert("t_xref", xvals)
            self.new_connectors.append((cid, name, tid))
            self.say(f"toegevoegd: AanvraagOfMelding 0..* '{name}' -> {target[1]} 0..1 (Relatiesoort)")
        self.touch(oid)

    # -- diagram --------------------------------------------------------------------------
    def update_diagram(self, attr_guids_aom: list[str]) -> None:
        self.step(f"Diagram {DIAGRAM[1]}")
        d = self.one("SELECT Diagram_ID, Name, StyleEx FROM t_diagram WHERE upper(ea_guid)=upper(?)", DIAGRAM[0])
        if d is None or d["Name"] != DIAGRAM[1]:
            self.warn(f"diagram {DIAGRAM[1]} ({DIAGRAM[0]}) niet gevonden; diagram overgeslagen")
            return
        did = d["Diagram_ID"]
        aom = self.obj(AOM)
        src = self.one("SELECT ObjectStyle FROM t_diagramobjects WHERE Diagram_ID=? AND Object_ID=?", did, aom)
        if src is None:
            self.warn("AanvraagOfMelding staat niet op het diagram; diagram overgeslagen")
            return
        style_tpl = src["ObjectStyle"]
        src_duid = style_tpl.split("DUID=")[1].split(";")[0]
        duids: dict[int, str] = {}
        seq = (self.one("SELECT MAX(Sequence) FROM t_diagramobjects WHERE Diagram_ID=?", did)[0] or 0) + 1
        for ref, rect in DIAGRAM_PLACES.items():
            tid = self.one("SELECT Object_ID, Name FROM t_object WHERE upper(ea_guid)=upper(?)", ref)
            row = self.one("SELECT ObjectStyle FROM t_diagramobjects WHERE Diagram_ID=? AND Object_ID=?", did, tid["Object_ID"])
            if row:
                duids[tid["Object_ID"]] = row["ObjectStyle"].split("DUID=")[1].split(";")[0]
                self.say(f"al gedaan: {tid['Name']} staat op het diagram")
                continue
            duid = new_duid()
            style = "DUID=" + duid + ";" + style_tpl.split(";", 1)[1]
            top, left, right, bottom = rect
            self.insert("t_diagramobjects", {"Diagram_ID": did, "Object_ID": tid["Object_ID"], "RectTop": top,
                                             "RectLeft": left, "RectRight": right, "RectBottom": bottom,
                                             "Sequence": seq, "ObjectStyle": style})
            seq += 1
            duids[tid["Object_ID"]] = duid
            self.say(f"op het diagram gezet: {tid['Name']}")
        for cid, name, tid in self.new_connectors:
            if self.one("SELECT 1 FROM t_diagramlinks WHERE DiagramID=? AND ConnectorID=?", did, cid):
                self.say(f"al gedaan: link '{name}'")
                continue
            self.insert("t_diagramlinks", {
                "DiagramID": did, "ConnectorID": cid,
                "Geometry": "SX=0;SY=0;EX=0;EY=0;EDGE=1;$LLB=;LLT=;LMT=;LMB=;LRT=;LRB=;IRHS=;ILHS=;",
                "Style": f"Mode=3;EOID={duids[tid]};SOID={src_duid};Color=-1;LWidth=0;", "Hidden": 0, "Path": ""})
            self.say(f"link op het diagram: '{name}'")
        # Zichtbare attributen van AanvraagOfMelding op dit diagram (StyleEx SPL=S_<obj>=<attr>,...:;).
        key = f"S_{prefix(AOM[0])}="
        style_ex = d["StyleEx"] or ""
        if key in style_ex:
            head, rest = style_ex.split(key, 1)
            lst, tail = rest.split(":", 1)
            items = [i for i in lst.split(",") if i]
            missing = [prefix(g) for g in attr_guids_aom if prefix(g) not in items]
            if missing:
                new_style = head + key + ",".join(items + missing) + ":" + tail
                self.run("UPDATE t_diagram SET StyleEx=? WHERE Diagram_ID=?", new_style, did)
                self.say(f"zichtbare attributen aangevuld met {len(missing)} nieuwe")
            else:
                self.say("al gedaan: zichtbare attributen")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea", help="pad naar de .qea (SQLite) van Enterprise Architect")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run op een kopie)")
    args = ap.parse_args()

    target = args.qea
    if not args.apply:
        tmp = tempfile.NamedTemporaryFile(prefix="fix_proposal_mor-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    f = Fixer(conn)
    try:
        aom_guids = f.add_attributes(AOM, TEMPLATE_ATTR_AOM, ATTRS_AOM)
        f.add_relations()
        f.add_attributes(MOR, TEMPLATE_ATTR_MOR, ATTRS_MOR)
        f.update_diagram(aom_guids)
    except Exception:
        conn.execute("ROLLBACK")
        raise

    print(f"\n{f.changes} gewijzigde rijen; {len(f.warnings)} waarschuwing(en)")
    if args.apply:
        conn.execute("COMMIT")
        ok = conn.execute("PRAGMA integrity_check").fetchone()[0]
        print(f"TOEGEPAST en vastgelegd in {args.qea}; integrity_check: {ok}")
        return 0 if ok == "ok" else 1
    conn.execute("ROLLBACK")
    conn.close()
    pathlib.Path(target).unlink(missing_ok=True)
    print("DRY-RUN op een tijdelijke kopie: niets opgeslagen (gebruik --apply om door te voeren)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
