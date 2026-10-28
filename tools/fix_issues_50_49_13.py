#!/usr/bin/env python3
"""Correcties uit GitHub-issues 50, 49 en 13 op de EA-repository van het GGM (.qea = SQLite).

Zelfde werkwijze als tools/fix_issue_53.py: één transactie, standaard een dry-run op een
tijdelijke kopie (exacte aantallen, origineel onaangeroerd), met --apply vastleggen in de
echte .qea. Idempotent: een tweede run meldt 0 wijzigingen. EA gesloten, back-up gemaakt.

  #50  Model BAG: Nummeraanduiding is niet abstract; AdresseerbaarObject (zes subklassen) wel.
  #49  Enumeratie Eenheid (Model Jeugd en Wmo Generiek) volgt de iWmo/iStandaarden-codes:
       01 Minuut, 04 Uur, 14 Etmaal, 16 Dagdeel (4 uur), 82 Stuks (output), 83 Euro's,
       84 Stuks (inspanning). De GGM-eigen waarden Onbekend (-1) en Leeg (-2) blijven.
       Let op: de codes zijn tekst met voorloopnul, zoals iWmo ze voorschrijft.
  #13  Definitie van Kunstwerk verwijst naar https://definities.geostandaarden.nl/nl/;
       definitie van Kwaliteitscatalogus Openbare Ruimte verwijst naar de huidige CROW-pagina
       (editie 2023) in plaats van de verdwenen pagina van de editie 2018. De tagged value
       'GEMMA definitie' blijft wat GEMMA Online toont.

Gebruik:
  python3 -I tools/fix_issues_50_49_13.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/fix_issues_50_49_13.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys
import tempfile
import uuid
from datetime import datetime

ABSTRACT = [  # (guid, naam, pakket, abstract)
    ("{32A22BC6-89EC-44af-8D7D-79B12311AE2D}", "Nummeraanduiding", "Model BAG", "0"),
    ("{8A04280B-E0B4-4e36-B448-C99750393D0D}", "AdresseerbaarObject", "Model BAG", "1"),
]
# Enumeratie Eenheid: literal-guid -> (naam oud, naam nieuw, waarde oud, waarde nieuw)
EENHEID = [
    ("{58E4FD67-C88D-42ed-B524-74D841576C39}", "Minuut", "Minuut", "1", "01"),
    ("{B741968A-373F-48ca-A242-DAA13496E912}", "Uur", "Uur", "4", "04"),
    ("{9B5E3056-74F7-4a60-B23B-42317E6DBAB9}", "Stuks", "Stuks (output)", "82", "82"),
    ("{70AB0639-89B9-4914-B6BA-9234DF316B0F}", "Euros", "Euro's", "83", "83"),
]
EENHEID_TEMPLATE = "{9B5E3056-74F7-4a60-B23B-42317E6DBAB9}"  # Stuks: sjabloon voor het nieuwe literal
EENHEID_NEW = ("Stuks (inspanning)", "84")  # komt op de positie vóór Onbekend/Leeg
EENHEID_TAIL = ["Onbekend", "Leeg"]  # GGM-eigen waarden, schuiven één positie op
DEFINITIONS = [  # (guid, naam, oude definitie (exact), nieuwe definitie)
    ("{71BCDE9D-88C2-4519-8105-028E40898AB}", "Kunstwerk",
     "Civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen "
     "en/of leidingen en niet bedoeld voor permanent menselijk verblijf. http://definities.geostandaarden.nl",
     "Civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen "
     "en/of leidingen en niet bedoeld voor permanent menselijk verblijf. https://definities.geostandaarden.nl/nl/"),
    ("{2C6C809D-28B0-4037-BBFA-3E438A2DF81D}", "Kwaliteitscatalogus Openbare Ruimte",
     "zie https://www.crow.nl/publicaties/kwaliteitscatalogus-openbare-ruimte-2018 ",
     "Catalogus van CROW met landelijke standaard kwaliteitsniveaus voor het beheer en onderhoud "
     "van de openbare ruimte, vastgelegd in beeldmeetlatten met foto's, beschrijvingen en "
     "prestatie-eisen. Zie https://www.crow.nl/kennisproducten/kwaliteitscatalogus-openbare-ruimte-2023/"),
]


def new_guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


class Fixer:
    def __init__(self, conn: sqlite3.Connection):
        self.c = conn
        self.c.row_factory = sqlite3.Row
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changes = 0
        self.warnings: list[str] = []

    def say(self, msg: str) -> None:
        print(f"    {msg}")

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)
        print(f"    LET OP: {msg}")

    def one(self, sql: str, *params):
        return self.c.execute(sql, params).fetchone()

    def run(self, sql: str, *params) -> int:
        n = self.c.execute(sql, params).rowcount
        self.changes += n
        return n

    def touch(self, object_id: int) -> None:
        self.c.execute("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", (self.now, object_id))

    # ---------------------------------------------------------------- #50
    def abstract_flags(self) -> None:
        print("\n#50 Abstracte objecttypen in Model BAG")
        for guid, name, pkg, value in ABSTRACT:
            o = self.one("SELECT o.Object_ID, o.Name, o.Abstract, p.Name AS pkg FROM t_object o "
                         "JOIN t_package p ON p.Package_ID=o.Package_ID WHERE upper(o.ea_guid)=upper(?)", guid)
            if o is None or o["Name"] != name or o["pkg"] != pkg:
                self.warn(f"{name} ({guid}) niet gevonden in {pkg}; overgeslagen")
                continue
            if o["Abstract"] == value:
                self.say(f"al gedaan: {name} abstract={value}")
                continue
            self.run("UPDATE t_object SET Abstract=? WHERE Object_ID=?", value, o["Object_ID"])
            self.touch(o["Object_ID"])
            self.say(f"{name}: abstract {o['Abstract']} -> {value}")

    # ---------------------------------------------------------------- #49
    def eenheid(self) -> None:
        print("\n#49 Enumeratie Eenheid conform iWmo")
        tpl = self.one("SELECT * FROM t_attribute WHERE upper(ea_guid)=upper(?)", EENHEID_TEMPLATE)
        if tpl is None:
            self.warn("sjabloon-literal (Stuks) niet gevonden; #49 overgeslagen")
            return
        enum_id = tpl["Object_ID"]
        for guid, old_name, new_name, old_val, new_val in EENHEID:
            a = self.one("SELECT ID, Name, \"Default\", Style FROM t_attribute WHERE upper(ea_guid)=upper(?)", guid)
            if a is None:
                self.warn(f"literal {old_name} ({guid}) niet gevonden")
                continue
            if a["Name"] == new_name and a["Default"] == new_val:
                self.say(f"al gedaan: {new_name} = {new_val}")
                continue
            if a["Name"] != old_name or a["Default"] != old_val:
                self.warn(f"literal {guid} is {a['Name']!r}={a['Default']!r}, verwacht {old_name!r}={old_val!r}; overgeslagen")
                continue
            style = new_val if a["Style"] == old_val else a["Style"]  # EA spiegelt de waarde in Style
            self.run("UPDATE t_attribute SET Name=?, \"Default\"=?, Style=? WHERE ID=?", new_name, new_val, style, a["ID"])
            self.say(f"{old_name} = {old_val}  ->  {new_name} = {new_val}")
        # Nieuw literal 84 Stuks (inspanning), vóór Onbekend/Leeg.
        name, value = EENHEID_NEW
        if self.one("SELECT 1 FROM t_attribute WHERE Object_ID=? AND Name=?", enum_id, name):
            self.say(f"al gedaan: {name} = {value}")
        else:
            tail = self.c.execute(
                f"SELECT ID, Name, Pos FROM t_attribute WHERE Object_ID=? AND Name IN ({','.join('?' * len(EENHEID_TAIL))}) ORDER BY Pos",
                (enum_id, *EENHEID_TAIL)).fetchall()
            pos = tail[0]["Pos"] if tail else (self.one("SELECT MAX(Pos)+1 FROM t_attribute WHERE Object_ID=?", enum_id)[0] or 0)
            for row in tail:
                self.run("UPDATE t_attribute SET Pos=Pos+1 WHERE ID=?", row["ID"])
            cols = [k for k in tpl.keys() if k != "ID"]
            vals = dict(zip(cols, [tpl[k] for k in cols]))
            vals.update({"Name": name, "Default": value, "Pos": pos, "ea_guid": new_guid(),
                         "Style": value if tpl["Style"] == tpl["Default"] else tpl["Style"]})
            self.c.execute(f"INSERT INTO t_attribute ({', '.join(f'\"{k}\"' for k in cols)}) VALUES ({', '.join('?' * len(cols))})",
                           [vals[k] for k in cols])
            self.changes += 1
            new_id = self.one("SELECT ID FROM t_attribute WHERE ea_guid=?", vals["ea_guid"])["ID"]
            # Tagged values en stereotype-xref van het sjabloon meekopiëren.
            for t in self.c.execute("SELECT Property, VALUE, NOTES FROM t_attributetag WHERE ElementID=?", (tpl["ID"],)):
                self.run("INSERT INTO t_attributetag (ElementID, Property, VALUE, NOTES, ea_guid) VALUES (?,?,?,?,?)",
                         new_id, t["Property"], t["VALUE"], t["NOTES"], new_guid())
            for x in self.c.execute("SELECT * FROM t_xref WHERE upper(Client)=upper(?)", (tpl["ea_guid"],)):
                xcols = list(x.keys())
                xvals = dict(zip(xcols, [x[k] for k in xcols]))
                xvals["Client"] = vals["ea_guid"]
                xvals["XrefID"] = new_guid()  # geen autosleutel: EA gebruikt een GUID
                self.run(f"INSERT INTO t_xref ({', '.join(f'\"{k}\"' for k in xcols)}) VALUES ({', '.join('?' * len(xcols))})",
                         *[xvals[k] for k in xcols])
            self.touch(enum_id)
            self.say(f"toegevoegd: {name} = {value} op positie {pos}; {', '.join(r['Name'] for r in tail)} schuiven op")

    # ---------------------------------------------------------------- #13
    def definitions(self) -> None:
        print("\n#13 Definities met verouderde URL's")
        for guid, name, old, new in DEFINITIONS:
            o = self.one("SELECT Object_ID, Name, Note FROM t_object WHERE upper(ea_guid)=upper(?)", guid)
            if o is None or o["Name"] != name:
                self.warn(f"{name} ({guid}) niet gevonden; overgeslagen")
                continue
            if o["Note"] == new:
                self.say(f"al gedaan: {name}")
                continue
            if (o["Note"] or "").rstrip() != old.rstrip():  # EA laat soms een regeleinde achter
                self.warn(f"{name}: definitie is {o['Note'][:80]!r}..., verwacht de oude tekst; overgeslagen")
                continue
            self.run("UPDATE t_object SET Note=? WHERE Object_ID=?", new, o["Object_ID"])
            self.touch(o["Object_ID"])
            self.say(f"{name}: definitie bijgewerkt")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea", help="pad naar de .qea (SQLite) van Enterprise Architect")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run op een kopie)")
    args = ap.parse_args()

    target = args.qea
    if not args.apply:
        tmp = tempfile.NamedTemporaryFile(prefix="fix_issues-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    f = Fixer(conn)
    try:
        f.abstract_flags()
        f.eenheid()
        f.definitions()
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
