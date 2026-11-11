#!/usr/bin/env python3
"""Proposal Inkooporderregels (Bart van den Bos, Rotterdam, en Arjen Brienen; expertgroep 4 februari 2026,
openbare consultatie tot 13 juni 2026) doorvoeren in de EA-repository van het GGM (.qea = SQLite), volgens
tools/proposal-inkooporderregels.md.

Zelfde werkwijze als tools/fixes/add_financien_pohv.py: één transactie, standaard een dry-run op een tijdelijke
kopie, met --apply vastleggen. Idempotent. Enterprise Architect gesloten, back-up gemaakt.

Wat het script doet, in Model Financien:
  1. Objecttype «Objecttype» Inkooporderregel met definitie, MIM-tagset en elf attributen (MIM-datatypes,
     bedragen in het GGM-datatype Bedrag zoals bij Factuurregel).
  2. Vier relaties «Relatiesoort»: Inkooporder heeft Inkooporderregel (1 - 1..*), Inkooporderregel wordt
     geschreven op Hoofdrekening (0..* - 0..1), Inkooporderregel heeft Kostenplaats (0..* - 0..1),
     Factuurregel betreft Inkooporderregel (0..* - 0..1).
  3. Diagram 'Financien Verplichtingen en Facturen': Inkooporderregel en Factuurregel erbij, met de vier
     relaties en de bestaande relatie Factuur heeft Factuurregel.

Gebruik:
  python3 -I tools/fixes/add_inkooporderregels.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/fixes/add_inkooporderregels.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
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
INKOOPORDER = ("{A91E9C27-C4FA-4e1b-A4FF-8AE74ED9B7EB}", "Inkooporder")
FACTUUR = ("{E1DA56C3-6ECA-4ec9-8CF4-FC57E1C43102}", "Factuur")
FACTUURREGEL = ("{65E960EA-CC92-4af1-AF2B-B4625FA6AEA0}", "Factuurregel")
HOOFDREKENING = ("{0EEAF579-3F47-4551-B9F9-7367280EB3EB}", "Hoofdrekening")
KOSTENPLAATS = ("{D90E822D-7EF8-4ea6-AF5C-4A4362577941}", "Kostenplaats")
TPL_ATTR = ("{6F38439B-23A4-4dd3-9C4E-F6B6E57027BF}", "naam")  # Kostenplaats.naam
TPL_CONNECTOR = ("{6CFEC8E4-A77E-44d6-8AB7-8D425CB81C98}", "leidt tot")
DIAGRAM = ("{0723EB5C-4A2C-44d4-B15B-37AC71B5D711}", "Financien Verplichtingen en Facturen")
AUTHOR = "Arjen Brienen"
HERKOMST = "Proposal Inkooporderregels (gemeente Rotterdam en expertgroep GGM, 2026)"
DATUM_OPNAME = "4 november 2026"
DIAGRAM_OBJECT_STYLE = ("NSL=0;BCol=-1;BFol=-1;LCol=-1;LWth=-1;fontsz=0;bold=0;black=0;italic=0;ul=0;charset=0;"
                        "pitch=0;AttPro=0;AttPri=0;AttPub=0;AttPkg=0;OpPro=0;OpPri=0;OpPub=0;OpPkg=0;AttCustom=0;"
                        "OpCustom=0;RzO=1;")
GEMMA_TAGS = {"GEMMA alternate name", "GEMMA bron", "GEMMA definitie", "GEMMA guid", "GEMMA naam",
              "GEMMA synoniemen", "GEMMA toelichting", "GEMMA type", "GEMMA url", "Datum tijd export"}
CS, INT, DECIMAL, DATE, BEDRAG = "CharacterString", "Integer", "Decimal", "Date", "Bedrag"

CLASS = ("Inkooporderregel",
         "Regel van een inkooporder voor één artikel of dienst, met het bestelde aantal, de prijs en de btw. Een "
         "inkooporder bestaat uit een of meer inkooporderregels; de kop bevat de algemene ordergegevens.",
         [("regelnummer", INT, 0, "Volgnummer van de regel binnen de inkooporder."),
          ("artikelcode", CS, 80, "Code van het bestelde artikel of de dienst."),
          ("omschrijving", CS, 200, "Omschrijving van het bestelde artikel of de dienst."),
          ("aantal", DECIMAL, 0, "Bestelde hoeveelheid."),
          ("eenheid", CS, 20, "Eenheid van de hoeveelheid, zoals stuks, uur of m2."),
          ("prijsPerEenheid", BEDRAG, 0, "Prijs per eenheid exclusief btw."),
          ("bedragExBTW", BEDRAG, 0, "Bedrag van de regel exclusief btw."),
          ("bedragBTW", BEDRAG, 0, "Btw-bedrag van de regel."),
          ("BTWPercentage", DECIMAL, 0, "Btw-percentage dat op de regel van toepassing is."),
          ("datumLevering", DATE, 0, "Afgesproken of verwachte leverdatum van de regel."),
          ("status", CS, 80, "Status van de regel, zoals besteld, geleverd of gefactureerd.")])
RELATIONS = [
    ("Inkooporder", "heeft", "Inkooporderregel", "1", "1..*"),
    ("Inkooporderregel", "wordt geschreven op", "Hoofdrekening", "0..*", "0..1"),
    ("Inkooporderregel", "heeft", "Kostenplaats", "0..*", "0..1"),
    ("Factuurregel", "betreft", "Inkooporderregel", "0..*", "0..1"),
]
PLACES = {"Inkooporderregel": (-275, 375, 465, -345), "Factuurregel": (-408, 375, 465, -478)}
EXISTING_LINKS = [("Factuur", "heeft", "Factuurregel")]


def new_guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


def new_duid() -> str:
    return uuid.uuid4().hex[:8].upper()


class Builder:
    def __init__(self, conn):
        self.c = conn
        self.c.row_factory = sqlite3.Row
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changes = 0
        self.ids = {}
        self.connectors = []

    def say(self, msg): print(f"    {msg}")
    def step(self, title): print(f"\n{title}")
    def one(self, sql, *p): return self.c.execute(sql, p).fetchone()
    def all(self, sql, *p): return self.c.execute(sql, p).fetchall()

    def run(self, sql, *p):
        n = self.c.execute(sql, p).rowcount
        self.changes += n
        return n

    def insert(self, table, vals):
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

    def touch(self, oid):
        self.c.execute("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", (self.now, oid))

    def copy_tags(self, tpl_oid, oid, overrides):
        for t in self.all("SELECT Property, Value, Notes FROM t_objectproperties WHERE Object_ID=? ORDER BY PropertyID", tpl_oid):
            value = "" if t["Property"] in GEMMA_TAGS else t["Value"]
            self.insert("t_objectproperties", {"Object_ID": oid, "Property": t["Property"],
                                               "Value": overrides.get(t["Property"], value), "Notes": t["Notes"],
                                               "ea_guid": new_guid()})

    def copy_xref(self, tpl_guid, guid):
        for x in self.all("SELECT * FROM t_xref WHERE upper(Client)=upper(?)", tpl_guid):
            vals = {k: x[k] for k in x.keys()}
            vals.update({"XrefID": new_guid(), "Client": guid})
            self.insert("t_xref", vals)

    def datatype_id(self, name):
        r = self.one("SELECT Object_ID FROM t_object WHERE Object_Type='DataType' AND Name=? ORDER BY CASE WHEN Package_ID=6 THEN 0 ELSE 1 END", name)
        if r is None:
            raise SystemExit(f"datatype {name} niet gevonden")
        return r["Object_ID"]

    def classes(self):
        self.step("1. Objecttype Inkooporderregel")
        pkg = self.row("t_package", "ea_guid", PKG_MODEL)["Package_ID"]
        tpl = self.row("t_object", "ea_guid", INKOOPORDER)
        for ref in (INKOOPORDER, FACTUUR, FACTUURREGEL, HOOFDREKENING, KOSTENPLAATS):
            self.ids[ref[1]] = self.row("t_object", "ea_guid", ref)["Object_ID"]
        name, note, attrs = CLASS
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
        attr_tpl = self.row("t_attribute", "ea_guid", TPL_ATTR)
        attr_tags = self.all("SELECT Property, VALUE, NOTES FROM t_attributetag WHERE ElementID=? ORDER BY PropertyID", attr_tpl["ID"])
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
            self.say(f"    attributen: {', '.join(added)}")

    def relations(self):
        self.step("2. Relaties")
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
        for src, name, dst in EXISTING_LINKS:
            r = self.one("SELECT Connector_ID FROM t_connector WHERE Start_Object_ID=? AND End_Object_ID=? AND Name=?",
                         self.ids[src], self.ids[dst], name)
            if r:
                self.connectors.append((r["Connector_ID"], src, dst))

    def diagram(self):
        self.step("3. Diagram Financien Verplichtingen en Facturen")
        d = self.row("t_diagram", "ea_guid", DIAGRAM)
        did = d["Diagram_ID"]
        duids = {}
        for name in ("Inkooporder", "Hoofdrekening", "Kostenplaats", "Factuur"):
            r = self.one("SELECT ObjectStyle FROM t_diagramobjects WHERE Diagram_ID=? AND Object_ID=?", did, self.ids[name])
            duids[name] = r["ObjectStyle"].split("DUID=")[1].split(";")[0]
        seq = (self.one("SELECT MAX(Sequence) FROM t_diagramobjects WHERE Diagram_ID=?", did)[0] or 0) + 1
        for name, (top, left, right, bottom) in PLACES.items():
            r = self.one("SELECT ObjectStyle FROM t_diagramobjects WHERE Diagram_ID=? AND Object_ID=?", did, self.ids[name])
            if r:
                duids[name] = r["ObjectStyle"].split("DUID=")[1].split(";")[0]
                continue
            duid = new_duid()
            self.insert("t_diagramobjects", {"Diagram_ID": did, "Object_ID": self.ids[name], "RectTop": top,
                                             "RectLeft": left, "RectRight": right, "RectBottom": bottom,
                                             "Sequence": seq, "ObjectStyle": "DUID=" + duid + ";" + DIAGRAM_OBJECT_STYLE})
            seq += 1
            duids[name] = duid
            self.say(f"geplaatst: {name}")
        for cid, src, dst in self.connectors:
            if self.one("SELECT 1 FROM t_diagramlinks WHERE DiagramID=? AND ConnectorID=?", did, cid):
                continue
            self.insert("t_diagramlinks", {
                "DiagramID": did, "ConnectorID": cid,
                "Geometry": "SX=0;SY=0;EX=0;EY=0;EDGE=1;$LLB=;LLT=;LMT=;LMB=;LRT=;LRB=;IRHS=;ILHS=;",
                "Style": f"Mode=3;EOID={duids[dst]};SOID={duids[src]};Color=-1;LWidth=0;", "Hidden": 0, "Path": ""})
            self.say(f"link: {src} -> {dst}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    target = args.qea
    if not args.apply:
        tmp = tempfile.NamedTemporaryFile(prefix="add_inkooporderregels-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    b = Builder(conn)
    try:
        b.classes()
        b.relations()
        b.diagram()
    except Exception:
        conn.execute("ROLLBACK")
        raise
    print(f"\n{b.changes} gewijzigde rijen")
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
