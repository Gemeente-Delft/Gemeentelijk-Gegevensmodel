#!/usr/bin/env python3
"""Memo Domein Financiën in POHV en GGM (Michiel van Wezel, Invest-NL, 26 november 2025; RFC in consultatie
sinds februari 2026, akkoord, toegezegd voor de volgende release) doorvoeren in de EA-repository van het GGM
(.qea = SQLite), volgens tools/proposal-financien-pohv-rgs.md met de aanbevolen keuzes. Besluit Arjen
4 november 2026: de definities van RGS (Referentiegrootboekrekening en de relatie 'is van soort') blijven
buiten deze wijziging.

Zelfde werkwijze als tools/add_samenwerkomgeving.py: één transactie, standaard een dry-run op een tijdelijke
kopie, met --apply vastleggen. Idempotent. Enterprise Architect gesloten, back-up gemaakt.

Wat het script doet, in Model Financien:
  1. Vijf objecttypen «Objecttype» met definitie, MIM-tagset en attributen met MIM-datatypes:
     Verbijzonderingsoort, Verbijzondering, Verdeelsleutel, Verdeelkenmerk, Verdeelregel.
  2. Kostenplaats: attribuut indicatieHulpkostenplaats : Boolean. Mutatie: scherpere definitie.
  3. Zes relaties «Relatiesoort» met kardinaliteiten.
  4. Diagram 'Financien Verwerken Mutaties': Verbijzondering en Verbijzonderingsoort erbij, met de twee
     relaties; nieuw diagram 'Financien Kostenverdeling' met Kostenplaats, Verdeelsleutel, Verdeelkenmerk en
     Verdeelregel (attributen zichtbaar).

Gebruik:
  python3 -I tools/add_financien_pohv.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/add_financien_pohv.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys
import tempfile
import uuid
from datetime import datetime

PKG_MODEL = ("{5FFD0C07-FF86-4896-9605-D8492189984D}", "Model Financien")
PKG_DIAGRAM = ("{21F9F340-C1AF-4c81-BC23-A41BAEE559D7}", "Diagram")
KOSTENPLAATS = ("{D90E822D-7EF8-4ea6-AF5C-4A4362577941}", "Kostenplaats")
MUTATIE = ("{CB0A6B53-D263-459e-8C28-AD97E5552FFF}", "Mutatie")
TPL_ATTR = ("{6F38439B-23A4-4dd3-9C4E-F6B6E57027BF}", "naam")  # Kostenplaats.naam
TPL_CONNECTOR = ("{6CFEC8E4-A77E-44d6-8AB7-8D425CB81C98}", "leidt tot")  # Factuurregel -> Mutatie
DIAGRAM_MUTATIES = ("{B758018F-CB22-420e-B4E4-E17EB5F71EDA}", "Financien Verwerken Mutaties")
DIAGRAM_NEW = "Financien Kostenverdeling"
AUTHOR = "Arjen Brienen"
HERKOMST = "Memo Domein Financiën in POHV en GGM (Invest-NL, Programma Onderwijshuisvesting, 2025)"
DATUM_OPNAME = "4 november 2026"
MUTATIE_NOTE = ("Boeking van een bedrag van de ene hoofdrekening naar de andere op een datum, toegeschreven aan een "
                "kostenplaats. Een mutatie ontstaat uit een factuurregel, batchregel of bankafschriftregel en kan met "
                "verbijzonderingen vanuit extra perspectieven worden gerapporteerd.")
DIAGRAM_OBJECT_STYLE = ("NSL=0;BCol=-1;BFol=-1;LCol=-1;LWth=-1;fontsz=0;bold=0;black=0;italic=0;ul=0;charset=0;"
                        "pitch=0;AttPro=0;AttPri=0;AttPub=0;AttPkg=0;OpPro=0;OpPri=0;OpPub=0;OpPkg=0;AttCustom=0;"
                        "OpCustom=0;RzO=1;")
GEMMA_TAGS = {"GEMMA alternate name", "GEMMA bron", "GEMMA definitie", "GEMMA guid", "GEMMA naam",
              "GEMMA synoniemen", "GEMMA toelichting", "GEMMA type", "GEMMA url", "Datum tijd export"}
CS, BOOL, DATE, DECIMAL, URI = "CharacterString", "Boolean", "Date", "Decimal", "URI"

CLASSES = {
    "Verbijzonderingsoort": (
        "Soort kenmerk waarmee een mutatie nader wordt geclassificeerd, zoals de 6S-laag van Stewart Brand "
        "(Site, Structure, Skin, Services, Space plan, Stuff), de NL/SfB-code, de componentomschrijving of de "
        "geplande vervangingsdatum. Naar het voorbeeld van VERA (woningcorporaties).",
        [("code", CS, 20, "Code van de verbijzonderingsoort, zoals 6S of NLSFB."),
         ("naam", CS, 80, "Naam van de verbijzonderingsoort."),
         ("omschrijving", CS, 0, "Omschrijving van de verbijzonderingsoort."),
         ("waardelijst", URI, 0, "Verwijzing naar de externe lijst met toegestane waarden, bijvoorbeeld NL/SfB.")]),
    "Verbijzondering": (
        "Kenmerk dat aan een mutatie is toegekend om deze vanuit een extra perspectief te kunnen rapporteren, "
        "zonder het grootboekschema te verfijnen; bijvoorbeeld de 6S-laag Services of de NL/SfB-hoofdgroep 50 "
        "bij de vervanging van een cv-ketel.",
        [("waarde", CS, 200, "Waarde van het kenmerk, zoals Services of 50."),
         ("omschrijving", CS, 0, "Toelichting bij de verbijzondering.")]),
    "Verdeelsleutel": (
        "Maatstaf waarmee de kosten van een hulpkostenplaats over andere kostenplaatsen worden verdeeld, zoals "
        "vierkante meters, fte of leerlingaantal.",
        [("naam", CS, 80, "Naam van de verdeelsleutel, zoals m2, FTE of leerlingaantal."),
         ("omschrijving", CS, 0, "Omschrijving van de verdeelsleutel."),
         ("eenheid", CS, 20, "Eenheid waarin de waarden van de verdeelsleutel worden uitgedrukt.")]),
    "Verdeelkenmerk": (
        "Waarde van een verdeelsleutel voor een kostenplaats in een periode, zoals 1.200 m2 voor een basisschool "
        "in een multifunctionele accommodatie.",
        [("waarde", DECIMAL, 0, "Kwantitatieve waarde van de verdeelsleutel voor de kostenplaats."),
         ("datumBeginGeldigheid", DATE, 0, "Datum vanaf wanneer de waarde geldt."),
         ("datumEindeGeldigheid", DATE, 0, "Datum tot wanneer de waarde geldt.")]),
    "Verdeelregel": (
        "Regel die bepaalt dat de kosten van een hulpkostenplaats volgens een verdeelsleutel worden verdeeld over "
        "de kostenplaatsen die een verdeelkenmerk voor die sleutel hebben; bijvoorbeeld de energiekosten van een "
        "multifunctionele accommodatie naar rato van vierkante meters over de huurders.",
        [("omschrijving", CS, 0, "Omschrijving van de verdeelregel."),
         ("datumBeginGeldigheid", DATE, 0, "Datum vanaf wanneer de regel geldt."),
         ("datumEindeGeldigheid", DATE, 0, "Datum tot wanneer de regel geldt.")]),
}
KOSTENPLAATS_ATTRS = [
    ("indicatieHulpkostenplaats", BOOL, 0,
     "Indicatie of de kostenplaats een hulpkostenplaats is waarvan de kosten via een verdeelregel over andere "
     "kostenplaatsen worden verdeeld."),
]
# (bron, relatienaam, doel, kardinaliteit bron, kardinaliteit doel)
RELATIONS = [
    ("Mutatie", "heeft", "Verbijzondering", "1", "0..*"),
    ("Verbijzondering", "is van soort", "Verbijzonderingsoort", "0..*", "1"),
    ("Kostenplaats", "heeft verdeelkenmerk", "Verdeelkenmerk", "1", "0..*"),
    ("Verdeelkenmerk", "van verdeelsleutel", "Verdeelsleutel", "0..*", "1"),
    ("Verdeelregel", "verdeelt kosten van", "Kostenplaats", "0..*", "1"),
    ("Verdeelregel", "volgens verdeelsleutel", "Verdeelsleutel", "0..*", "1"),
]
# Bestaand diagram (attributen verborgen, vakjes 90 x 70): rechts van Subrekening.
PLACES_MUTATIES = {"Verbijzondering": (-380, 725, 815, -450), "Verbijzonderingsoort": (-500, 725, 815, -570)}
LINKS_MUTATIES = {("Mutatie", "Verbijzondering"), ("Verbijzondering", "Verbijzonderingsoort")}
# Nieuw diagram (attributen zichtbaar): naam -> (RectTop, RectLeft, RectRight); hoogte volgt uit de attributen.
PLACES_NEW = {"Kostenplaats": (-30, 30, 260), "Verdeelkenmerk": (-30, 330, 560), "Verdeelsleutel": (-30, 630, 860),
              "Verdeelregel": (-300, 330, 560)}
LINKS_NEW = {("Kostenplaats", "Verdeelkenmerk"), ("Verdeelkenmerk", "Verdeelsleutel"),
             ("Verdeelregel", "Kostenplaats"), ("Verdeelregel", "Verdeelsleutel")}


def new_guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


def new_duid() -> str:
    return uuid.uuid4().hex[:8].upper()


class Builder:
    def __init__(self, conn: sqlite3.Connection):
        self.c = conn
        self.c.row_factory = sqlite3.Row
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changes = 0
        self.warnings: list[str] = []
        self.ids: dict[str, int] = {}
        self.connectors: list[tuple[int, str, str]] = []

    def say(self, msg): print(f"    {msg}")
    def warn(self, msg): self.warnings.append(msg); print(f"    LET OP: {msg}")
    def step(self, title): print(f"\n{title}")
    def one(self, sql, *p): return self.c.execute(sql, p).fetchone()
    def all(self, sql, *p): return self.c.execute(sql, p).fetchall()

    def run(self, sql, *p) -> int:
        n = self.c.execute(sql, p).rowcount
        self.changes += n
        return n

    def insert(self, table: str, vals: dict) -> int:
        cols = list(vals)
        self.c.execute(f"INSERT INTO {table} ({', '.join(f'\"{k}\"' for k in cols)}) VALUES ({', '.join('?' * len(cols))})",
                       [vals[k] for k in cols])
        self.changes += 1
        return self.c.execute("SELECT last_insert_rowid()").fetchone()[0]

    def row(self, table, guid_col, ref, name_col="Name"):
        r = self.one(f"SELECT * FROM {table} WHERE upper({guid_col})=upper(?)", ref[0])
        if r is None or r[name_col] != ref[1]:
            raise SystemExit(f"sjabloon {ref[1]} ({ref[0]}) niet gevonden in {table}; niets gewijzigd")
        return r

    def touch(self, oid: int) -> None:
        self.c.execute("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", (self.now, oid))

    def copy_tags(self, tpl_oid: int, oid: int, overrides: dict) -> int:
        n = 0
        for t in self.all("SELECT Property, Value, Notes FROM t_objectproperties WHERE Object_ID=? ORDER BY PropertyID", tpl_oid):
            value = "" if t["Property"] in GEMMA_TAGS else t["Value"]
            self.insert("t_objectproperties", {"Object_ID": oid, "Property": t["Property"],
                                               "Value": overrides.get(t["Property"], value), "Notes": t["Notes"],
                                               "ea_guid": new_guid()})
            n += 1
        return n

    def copy_xref(self, tpl_guid: str, guid: str) -> int:
        n = 0
        for x in self.all("SELECT * FROM t_xref WHERE upper(Client)=upper(?)", tpl_guid):
            vals = {k: x[k] for k in x.keys()}
            vals.update({"XrefID": new_guid(), "Client": guid})
            self.insert("t_xref", vals)
            n += 1
        return n

    def datatype_id(self, name: str) -> int:
        r = self.one("SELECT Object_ID FROM t_object WHERE Object_Type='DataType' AND Package_ID=6 AND Name=?", name)
        if r is None:
            raise SystemExit(f"datatype {name} niet gevonden")
        return r["Object_ID"]

    def add_attributes(self, oid: int, attrs: list, attr_tpl, attr_tags) -> list[str]:
        pos = (self.one("SELECT COALESCE(MAX(Pos), -1) FROM t_attribute WHERE Object_ID=?", oid)[0]) + 1
        added = []
        for aname, dtype, length, anote in attrs:
            if self.one("SELECT 1 FROM t_attribute WHERE Object_ID=? AND Name=?", oid, aname):
                continue
            avals = {k: attr_tpl[k] for k in attr_tpl.keys() if k != "ID"}
            avals.update({"Object_ID": oid, "Name": aname, "Type": dtype, "Classifier": str(self.datatype_id(dtype)),
                          "Length": length, "Notes": anote, "Pos": pos, "Default": "", "Style": "", "ea_guid": new_guid()})
            pos += 1
            aid = self.insert("t_attribute", avals)
            overrides = {"Lengte": str(length) if length else "", "Herkomst": HERKOMST,
                         "Datum opname": DATUM_OPNAME, "Mogelijk geen waarde": "Ja"}
            for t in attr_tags:
                self.insert("t_attributetag", {"ElementID": aid, "Property": t["Property"],
                                               "VALUE": overrides.get(t["Property"], t["VALUE"]),
                                               "NOTES": t["NOTES"], "ea_guid": new_guid()})
            self.copy_xref(attr_tpl["ea_guid"], avals["ea_guid"])
            added.append(f"{aname} : {dtype}" + (f" ({length})" if length else ""))
        if added:
            self.touch(oid)
        return added

    # -- 1. objecttypen -------------------------------------------------------------------
    def classes(self) -> None:
        self.step("1. Objecttypen en attributen in Model Financien")
        pkg = self.row("t_package", "ea_guid", PKG_MODEL)["Package_ID"]
        tpl = self.row("t_object", "ea_guid", KOSTENPLAATS)
        attr_tpl = self.row("t_attribute", "ea_guid", TPL_ATTR)
        attr_tags = self.all("SELECT Property, VALUE, NOTES FROM t_attributetag WHERE ElementID=? ORDER BY PropertyID", attr_tpl["ID"])
        self.ids["Kostenplaats"] = tpl["Object_ID"]
        self.ids["Mutatie"] = self.row("t_object", "ea_guid", MUTATIE)["Object_ID"]
        for name, (note, attrs) in CLASSES.items():
            existing = self.one("SELECT Object_ID FROM t_object WHERE Package_ID=? AND Name=?", pkg, name)
            if existing:
                oid = existing["Object_ID"]
                self.say(f"al gedaan: {name}")
            else:
                guid = new_guid()
                vals = {k: tpl[k] for k in tpl.keys() if k != "Object_ID"}
                vals.update({"Name": name, "Note": note, "Package_ID": pkg, "ea_guid": guid, "Author": AUTHOR,
                             "Version": "1.0", "CreatedDate": self.now, "ModifiedDate": self.now})
                oid = self.insert("t_object", vals)
                self.copy_tags(tpl["Object_ID"], oid, {"Datum opname": DATUM_OPNAME, "Herkomst": HERKOMST})
                self.copy_xref(tpl["ea_guid"], guid)
                self.say(f"aangemaakt: «Objecttype» {name}")
            self.ids[name] = oid
            added = self.add_attributes(oid, attrs, attr_tpl, attr_tags)
            if added:
                self.say(f"    attributen: {', '.join(added)}")
        self.step("2. Kostenplaats en Mutatie")
        added = self.add_attributes(self.ids["Kostenplaats"], KOSTENPLAATS_ATTRS, attr_tpl, attr_tags)
        self.say(f"Kostenplaats: {', '.join(added) if added else 'al gedaan'}")
        m = self.one("SELECT Note FROM t_object WHERE Object_ID=?", self.ids["Mutatie"])
        if m["Note"] == MUTATIE_NOTE:
            self.say("Mutatie: definitie al gedaan")
        else:
            self.run("UPDATE t_object SET Note=? WHERE Object_ID=?", MUTATIE_NOTE, self.ids["Mutatie"])
            self.touch(self.ids["Mutatie"])
            self.say(f"Mutatie: definitie was {m['Note']!r}")

    # -- 3. relaties ------------------------------------------------------------------------
    def relations(self) -> None:
        self.step("3. Relaties")
        tpl = self.row("t_connector", "ea_guid", TPL_CONNECTOR)
        for src, name, dst, scard, dcard in RELATIONS:
            sid, did = self.ids[src], self.ids[dst]
            existing = self.one("SELECT Connector_ID FROM t_connector WHERE Start_Object_ID=? AND End_Object_ID=? "
                                "AND Connector_Type='Association' AND Name=?", sid, did, name)
            if existing:
                self.connectors.append((existing["Connector_ID"], src, dst))
                continue
            vals = {k: tpl[k] for k in tpl.keys() if k != "Connector_ID"}
            vals.update({"Name": name, "Notes": "", "Direction": "Source -> Destination", "SourceCard": scard,
                         "DestCard": dcard, "Btm_Start_Label": scard, "Btm_End_Label": dcard, "Top_Mid_Label": name,
                         "Start_Object_ID": sid, "End_Object_ID": did, "DiagramID": 0, "ea_guid": new_guid()})
            cid = self.insert("t_connector", vals)
            self.copy_xref(tpl["ea_guid"], vals["ea_guid"])
            self.connectors.append((cid, src, dst))
            self.say(f"{src} {scard} '{name}' -> {dst} {dcard}")

    # -- 4. diagrammen ----------------------------------------------------------------------
    def _place(self, did: int, name: str, rect: tuple, duids: dict, seq: int) -> int:
        oid = self.ids[name]
        r = self.one("SELECT ObjectStyle FROM t_diagramobjects WHERE Diagram_ID=? AND Object_ID=?", did, oid)
        if r:
            duids[name] = r["ObjectStyle"].split("DUID=")[1].split(";")[0]
            return seq
        duid = new_duid()
        top, left, right, bottom = rect
        self.insert("t_diagramobjects", {"Diagram_ID": did, "Object_ID": oid, "RectTop": top, "RectLeft": left,
                                         "RectRight": right, "RectBottom": bottom, "Sequence": seq,
                                         "ObjectStyle": "DUID=" + duid + ";" + DIAGRAM_OBJECT_STYLE})
        duids[name] = duid
        self.say(f"geplaatst: {name}")
        return seq + 1

    def _link(self, did: int, duids: dict, wanted: set) -> None:
        for cid, src, dst in self.connectors:
            if (src, dst) not in wanted or self.one("SELECT 1 FROM t_diagramlinks WHERE DiagramID=? AND ConnectorID=?", did, cid):
                continue
            self.insert("t_diagramlinks", {
                "DiagramID": did, "ConnectorID": cid,
                "Geometry": "SX=0;SY=0;EX=0;EY=0;EDGE=1;$LLB=;LLT=;LMT=;LMB=;LRT=;LRB=;IRHS=;ILHS=;",
                "Style": f"Mode=3;EOID={duids[dst]};SOID={duids[src]};Color=-1;LWidth=0;", "Hidden": 0, "Path": ""})
            self.say(f"link: {src} -> {dst}")

    def diagrams(self) -> None:
        self.step("4. Diagram Financien Verwerken Mutaties")
        d = self.row("t_diagram", "ea_guid", DIAGRAM_MUTATIES)
        did = d["Diagram_ID"]
        duids = {}
        for name in ("Mutatie",):
            r = self.one("SELECT ObjectStyle FROM t_diagramobjects WHERE Diagram_ID=? AND Object_ID=?", did, self.ids[name])
            duids[name] = r["ObjectStyle"].split("DUID=")[1].split(";")[0]
        seq = (self.one("SELECT MAX(Sequence) FROM t_diagramobjects WHERE Diagram_ID=?", did)[0] or 0) + 1
        for name, rect in PLACES_MUTATIES.items():
            seq = self._place(did, name, rect, duids, seq)
        self._link(did, duids, LINKS_MUTATIES)

        self.step(f"5. Diagram {DIAGRAM_NEW}")
        pkg = self.row("t_package", "ea_guid", PKG_DIAGRAM)["Package_ID"]
        existing = self.one("SELECT Diagram_ID FROM t_diagram WHERE Package_ID=? AND Name=?", pkg, DIAGRAM_NEW)
        if existing:
            nid = existing["Diagram_ID"]
            self.say(f"al gedaan: diagram {DIAGRAM_NEW} ({nid})")
        else:
            vals = {k: d[k] for k in d.keys() if k != "Diagram_ID"}
            vals.update({"Package_ID": pkg, "ParentID": 0, "Name": DIAGRAM_NEW, "Author": AUTHOR, "Version": "1.0",
                         "CreatedDate": self.now, "ModifiedDate": self.now, "ea_guid": new_guid(),
                         "PDATA": (d["PDATA"] or "").replace("HideAtts=1", "HideAtts=0"),
                         "StyleEx": "SaveTag=" + new_duid() + ";" + (d["StyleEx"] or "").split(";", 1)[1]})
            nid = self.insert("t_diagram", vals)
            self.say(f"aangemaakt: diagram {DIAGRAM_NEW} ({nid})")
        duids = {}
        seq = (self.one("SELECT MAX(Sequence) FROM t_diagramobjects WHERE Diagram_ID=?", nid)[0] or 0) + 1
        for name, (top, left, right) in PLACES_NEW.items():
            n_attrs = self.one("SELECT COUNT(*) FROM t_attribute WHERE Object_ID=?", self.ids[name])[0]
            seq = self._place(nid, name, (top, left, right, top - max(60, 46 + 17 * n_attrs)), duids, seq)
        self._link(nid, duids, LINKS_NEW)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    target = args.qea
    if not args.apply:
        tmp = tempfile.NamedTemporaryFile(prefix="add_financien_pohv-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    b = Builder(conn)
    try:
        b.classes()
        b.relations()
        b.diagrams()
    except Exception:
        conn.execute("ROLLBACK")
        raise
    print(f"\n{b.changes} gewijzigde rijen; {len(b.warnings)} waarschuwing(en)")
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
