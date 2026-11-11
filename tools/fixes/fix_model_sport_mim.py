#!/usr/bin/env python3
"""De oudere elementen van Model Sport (5 Sport, Cultuur en Recreatie > Sport) naar MIM brengen in de
EA-repository van het GGM (.qea = SQLite). Vervolg op tools/fixes/fix_zwembaden.py (11 november 2026), op
verzoek van Arjen ("Ja, ook Model Sport").

Wat het script doet:
  1. Aantal: «Objecttype» (profiel VNGR SIM+Grouping NL) met de MIM-tagset; attribuut aantalMateriaal
     wordt «Attribuutsoort» met tagset.
  2. Sport: profiel MIM::Objecttype wordt VNGR SIM+Grouping NL::Objecttype, tagset aangevuld (oude
     tags in kleine letters krijgen de juiste schrijfwijze); attribuut naam wordt «Attribuutsoort».
  3. Relatie Sportvereniging 'oefent uit' Sport wordt «Relatiesoort».
  4. Ontwerpregel m4: Bezetting, Onderhoudskosten en Veld krijgen elk één attribuut
     (aantalDeelnemers, bedrag, naam).
  5. De «Relatiesoort»-associaties vanuit Model Sport krijgen de MIM-tagset voor relatiesoorten
     (niet de dubbele relaties naar het archiefpackage van RSGB).
  6. Tikfout in de definitie van Sportmateriaal ('odnersteuning').

Niet gewijzigd: de Usage-relatie Binnenlocatie 'inspectierapport' Document (zelfde patroon als de
andere 16 Usage-relaties naar Document in het GGM) en bestaande definities en datatypes.

Eén transactie, standaard een dry-run op een tijdelijke kopie, met --apply vastleggen. Idempotent.
Enterprise Architect gesloten, back-up gemaakt.

Gebruik:
  python3 -I tools/fixes/fix_model_sport_mim.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/fixes/fix_model_sport_mim.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys
import tempfile
import uuid
from datetime import datetime

PKG_MODEL_SPORT = "{D6E7B2AB-8AD0-4c88-8742-3970AEDB4203}"
TPL_CLASS = ("{BBBB63AC-B546-409b-B6D4-53DB561253B7}", "Werknemer")
TPL_ATTR = ("{96DB65D5-F296-4d9b-857F-8327DFF570DE}", "naam")
TPL_ASSOC = ("{87F9EA19-0A1D-4c3f-ADCA-C8F48F216312}", "kan leiden tot")
TPL_ASSOC_TAGS = ("{1778947E-A0EE-C776-2C1C-281C33036576}", "leidt tot")
OEFENT_UIT = "{3BD57709-AE22-40c0-A501-1DB1435C1488}"

DATUM_OPNAME = "11 november 2026"
TO_OBJECTTYPE = ["Aantal", "Sport"]                     # klasse zonder (VNGR SIM-)stereotype
TO_ATTRIBUUTSOORT = [("Aantal", "aantalMateriaal"), ("Sport", "naam")]
# objecttype -> (attribuut, datatype, lengte, precisie, schaal, Lengte-tag, eenheid, definitie)
NEW_ATTRS = {
    "Bezetting": ("aantalDeelnemers", "Integer", 0, 0, 0, "", None, "Aantal deelnemers aan de activiteit."),
    "Onderhoudskosten": ("bedrag", "Decimal", 0, 10, 2, "10,2", "EUR", "Bedrag van de onderhoudskosten."),
    "Veld": ("naam", "CharacterString", 200, 0, 0, "200", None, "Naam van het veld."),
}
TYPO = ("Sportmateriaal", "odnersteuning", "ondersteuning")
GEMMA_TAGS = {"GEMMA alternate name", "GEMMA bron", "GEMMA definitie", "GEMMA guid", "GEMMA naam",
              "GEMMA synoniemen", "GEMMA toelichting", "GEMMA type", "GEMMA url", "Datum tijd export"}


def new_guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


class Fixer:
    def __init__(self, conn: sqlite3.Connection):
        self.c = conn
        self.c.row_factory = sqlite3.Row
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changes = 0

    def say(self, msg: str) -> None:
        print(f"    {msg}")

    def one(self, sql: str, *params):
        return self.c.execute(sql, params).fetchone()

    def all(self, sql: str, *params):
        return self.c.execute(sql, params).fetchall()

    def run(self, sql: str, *params) -> int:
        n = self.c.execute(sql, params).rowcount
        self.changes += n
        return n

    def insert(self, table: str, vals: dict) -> int:
        cols = list(vals)
        self.c.execute(f"INSERT INTO {table} ({', '.join(f'\"{k}\"' for k in cols)}) "
                       f"VALUES ({', '.join('?' * len(cols))})", [vals[k] for k in cols])
        self.changes += 1
        return self.c.execute("SELECT last_insert_rowid()").fetchone()[0]

    def tpl(self, table: str, ref: tuple):
        r = self.one(f"SELECT * FROM {table} WHERE upper(ea_guid)=upper(?)", ref[0])
        if r is None or r["Name"] != ref[1]:
            raise SystemExit(f"sjabloon {ref[1]} ({ref[0]}) niet gevonden in {table}; niets gewijzigd")
        return r

    def cls(self, name: str):
        rows = self.all("SELECT * FROM t_object WHERE Package_ID=? AND Object_Type='Class' AND Name=?", self.pid, name)
        if len(rows) != 1:
            raise SystemExit(f"klasse {name} niet precies één keer gevonden in Model Sport; niets gewijzigd")
        return rows[0]

    def stereotype_xref(self, guid: str, template_guid: str) -> int:
        tpl = self.one("SELECT * FROM t_xref WHERE upper(Client)=upper(?) AND Name='Stereotypes'", template_guid)
        cur = self.all("SELECT XrefID, Description FROM t_xref WHERE upper(Client)=upper(?) AND Name='Stereotypes'", guid)
        if len(cur) == 1 and cur[0]["Description"] == tpl["Description"]:
            return 0
        for x in cur:
            self.run("DELETE FROM t_xref WHERE XrefID=?", x["XrefID"])
        vals = {k: tpl[k] for k in tpl.keys()}
        vals.update({"XrefID": new_guid(), "Client": guid})
        self.insert("t_xref", vals)
        return 1

    def tagset(self, table: str, key: str, value_col: str, notes_col: str, element_id: int, tpl_tags,
               overrides: dict, rename: bool = True) -> tuple:
        """Tagset van het sjabloon aanvullen; bestaande tags blijven. EA vergelijkt tagnamen zonder onderscheid
        tussen hoofd- en kleine letters: een bestaande variant wordt hernoemd (rename) of met rust gelaten."""
        cur = {r["Property"]: r["PropertyID"] for r in
               self.all(f"SELECT PropertyID, Property FROM {table} WHERE {key}=?", element_id)}
        lower = {p.lower(): p for p in cur}
        added = renamed = 0
        for t in tpl_tags:
            prop = t["Property"]
            if prop in cur:
                continue
            if prop.lower() in lower and not rename:
                continue
            if prop.lower() in lower:
                self.run(f"UPDATE {table} SET Property=? WHERE PropertyID=?", prop, cur[lower[prop.lower()]])
                renamed += 1
                continue
            value = overrides.get(prop, None if prop in GEMMA_TAGS else t[value_col])
            self.insert(table, {key: element_id, "Property": prop, value_col: value, notes_col: t[notes_col],
                                "ea_guid": new_guid()})
            added += 1
        return added, renamed

    # -- stappen ---------------------------------------------------------------------------
    def fix(self) -> None:
        p = self.one("SELECT Package_ID, Name FROM t_package WHERE upper(ea_guid)=upper(?)", PKG_MODEL_SPORT)
        if p is None or p["Name"] != "Model Sport":
            raise SystemExit("package Model Sport niet gevonden; niets gewijzigd")
        self.pid = p["Package_ID"]
        tpl_class, tpl_attr = self.tpl("t_object", TPL_CLASS), self.tpl("t_attribute", TPL_ATTR)
        tpl_assoc, tpl_assoc_tags = self.tpl("t_connector", TPL_ASSOC), self.tpl("t_connector", TPL_ASSOC_TAGS)
        class_tags = self.all("SELECT Property, Value, Notes FROM t_objectproperties WHERE Object_ID=? ORDER BY PropertyID",
                              tpl_class["Object_ID"])
        attr_tags = self.all("SELECT Property, VALUE, NOTES FROM t_attributetag WHERE ElementID=? ORDER BY PropertyID",
                             tpl_attr["ID"])
        rel_tags = self.all("SELECT Property, VALUE, NOTES FROM t_connectortag WHERE ElementID=? ORDER BY PropertyID",
                            tpl_assoc_tags["Connector_ID"])
        dt = {r["Name"]: r["Object_ID"] for r in
              self.all("SELECT Object_ID, Name FROM t_object WHERE Object_Type='DataType' AND Package_ID=6")}

        print("\n1. Objecttypen zonder VNGR SIM-stereotype")
        for name in TO_OBJECTTYPE:
            o = self.cls(name)
            done = []
            if o["Stereotype"] != "Objecttype":
                self.run("UPDATE t_object SET Stereotype='Objecttype' WHERE Object_ID=?", o["Object_ID"])
                done.append("«Objecttype»")
            if self.stereotype_xref(o["ea_guid"], TPL_CLASS[0]):
                done.append("profiel VNGR SIM")
            added, renamed = self.tagset("t_objectproperties", "Object_ID", "Value", "Notes", o["Object_ID"],
                                         class_tags, {})
            if added or renamed:
                done.append(f"{added} tags toegevoegd, {renamed} tags hernoemd naar de MIM-schrijfwijze")
            if done:
                self.run("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", self.now, o["Object_ID"])
                self.say(f"{name}: {'; '.join(done)}")

        print("\n2. Attributen zonder stereotype")
        for cname, aname in TO_ATTRIBUUTSOORT:
            o = self.cls(cname)
            a = self.one("SELECT * FROM t_attribute WHERE Object_ID=? AND Name=?", o["Object_ID"], aname)
            if a is None:
                raise SystemExit(f"attribuut {cname}.{aname} niet gevonden; niets gewijzigd")
            done = []
            if a["Stereotype"] != "Attribuutsoort":
                self.run("UPDATE t_attribute SET Stereotype='Attribuutsoort' WHERE ID=?", a["ID"])
                done.append("«Attribuutsoort»")
            if self.stereotype_xref(a["ea_guid"], TPL_ATTR[0]):
                done.append("profiel VNGR SIM")
            added, _ = self.tagset("t_attributetag", "ElementID", "VALUE", "NOTES", a["ID"], attr_tags,
                                   {"Lengte": str(a["Length"]) if a["Length"] else "", "Mogelijk geen waarde": "Ja"})
            if added:
                done.append(f"{added} tags toegevoegd")
            if done:
                self.say(f"{cname}.{aname}: {'; '.join(done)}")

        print("\n3. Relatie zonder stereotype")
        r = self.one("SELECT * FROM t_connector WHERE upper(ea_guid)=upper(?)", OEFENT_UIT)
        if r is None or r["Name"] != "oefent uit":
            raise SystemExit("relatie 'oefent uit' niet gevonden; niets gewijzigd")
        done = []
        if r["Stereotype"] != "Relatiesoort":
            self.run("UPDATE t_connector SET Stereotype='Relatiesoort' WHERE Connector_ID=?", r["Connector_ID"])
            done.append("«Relatiesoort»")
        if self.stereotype_xref(r["ea_guid"], TPL_ASSOC[0]):
            done.append("profiel VNGR SIM")
        if done:
            self.say(f"Sportvereniging 'oefent uit' Sport: {'; '.join(done)}")

        print("\n4. Objecttypen zonder attributen (m4)")
        for cname, (aname, dtype, length, precision, scale, lengte_tag, eenheid, definition) in NEW_ATTRS.items():
            o = self.cls(cname)
            if self.one("SELECT 1 FROM t_attribute WHERE Object_ID=?", o["Object_ID"]):
                continue
            vals = {k: tpl_attr[k] for k in tpl_attr.keys() if k != "ID"}
            vals.update({"Object_ID": o["Object_ID"], "Name": aname, "Type": dtype, "Classifier": str(dt[dtype]),
                         "Length": length, "Precision": precision, "Scale": scale, "Notes": definition, "Pos": 0,
                         "Default": "", "Style": "", "ea_guid": new_guid()})
            aid = self.insert("t_attribute", vals)
            self.stereotype_xref(vals["ea_guid"], TPL_ATTR[0])
            self.tagset("t_attributetag", "ElementID", "VALUE", "NOTES", aid, attr_tags,
                        {"Lengte": lengte_tag, "Eenheid": eenheid, "Datum opname": DATUM_OPNAME,
                         "Mogelijk geen waarde": "Ja"})
            self.run("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", self.now, o["Object_ID"])
            self.say(f"{cname}: + {aname} : {dtype}" + (f" ({lengte_tag})" if lengte_tag else ""))

        print("\n5. MIM-tagset op de relatiesoorten vanuit Model Sport")
        n_rel = n_tags = 0
        for r in self.all("SELECT c.Connector_ID, c.Name, s.Name AS s, d.Name AS d FROM t_connector c "
                          "JOIN t_object s ON s.Object_ID=c.Start_Object_ID JOIN t_object d ON d.Object_ID=c.End_Object_ID "
                          "JOIN t_package dp ON dp.Package_ID=d.Package_ID LEFT JOIN t_package dpp ON dpp.Package_ID=dp.Parent_ID "
                          "WHERE s.Package_ID=? AND s.Object_Type='Class' AND c.Connector_Type IN ('Association','Aggregation') "
                          "AND c.Stereotype='Relatiesoort' AND coalesce(dpp.Name,'')<>'archief' ORDER BY c.Connector_ID",
                          self.pid):
            added, _ = self.tagset("t_connectortag", "ElementID", "VALUE", "NOTES", r["Connector_ID"], rel_tags,
                                   {"Authentiek": None}, rename=False)   # GEMMA-tag 'toelichting' blijft
            if added:
                n_rel += 1
                n_tags += added
                self.say(f"{r['s']} '{r['Name']}' {r['d']}: {added} tags")
        self.say(f"{n_rel} relaties aangevuld ({n_tags} tags)")

        print("\n6. Tikfout")
        cname, wrong, right = TYPO
        o = self.cls(cname)
        if wrong in (o["Note"] or ""):
            self.run("UPDATE t_object SET Note=?, ModifiedDate=? WHERE Object_ID=?", o["Note"].replace(wrong, right),
                     self.now, o["Object_ID"])
            self.say(f"{cname}: '{wrong}' -> '{right}'")

    def verify(self) -> int:
        print("\n7. Eindcontrole Model Sport (m1, m3, m4, m7 en MIM-stereotypen)")
        problems = []
        vngr = "VNGR SIM+Grouping NL::"
        classes = self.all("SELECT * FROM t_object WHERE Package_ID=? AND Object_Type='Class' ORDER BY Name", self.pid)
        for o in classes:
            x = self.one("SELECT Description FROM t_xref WHERE Client=? AND Name='Stereotypes'", o["ea_guid"])
            own = self.one("SELECT COUNT(*) FROM t_attribute WHERE Object_ID=?", o["Object_ID"])[0]
            inherited = self.one("SELECT COUNT(*) FROM t_attribute a JOIN t_connector c ON c.End_Object_ID=a.Object_ID "
                                 "WHERE c.Start_Object_ID=? AND c.Connector_Type='Generalization'", o["Object_ID"])[0]
            if o["Stereotype"] != "Objecttype" or x is None or vngr + "Objecttype" not in x["Description"]:
                problems.append(f"{o['Name']}: stereotype of profiel")
            if not o["Note"]:
                problems.append(f"{o['Name']}: geen definitie")
            if own + inherited == 0:
                problems.append(f"{o['Name']}: geen attributen")
            for a in self.all("SELECT a.*, c.Name AS cls FROM t_attribute a LEFT JOIN t_object c ON c.Object_ID=a.Classifier "
                              "WHERE a.Object_ID=?", o["Object_ID"]):
                ax = self.one("SELECT Description FROM t_xref WHERE Client=? AND Name='Stereotypes'", a["ea_guid"])
                if a["Stereotype"] != "Attribuutsoort" or ax is None or a["cls"] != a["Type"]:
                    problems.append(f"{o['Name']}.{a['Name']}: stereotype of datatype")
        rels = self.all("SELECT c.*, s.Name AS s, d.Name AS d FROM t_connector c JOIN t_object s ON s.Object_ID=c.Start_Object_ID "
                        "JOIN t_object d ON d.Object_ID=c.End_Object_ID WHERE s.Package_ID=? AND s.Object_Type='Class'", self.pid)
        usage = 0
        for r in rels:
            if r["Connector_Type"] == "Usage":
                usage += 1
            elif r["Connector_Type"] == "Generalization":
                if r["Stereotype"] != "Generalisatie":
                    problems.append(f"generalisatie {r['s']} -> {r['d']}")
            elif r["Stereotype"] != "Relatiesoort" or not r["SourceCard"] or not r["DestCard"] \
                    or r["Direction"] != "Source -> Destination":
                problems.append(f"relatie {r['s']} '{r['Name']}' {r['d']}")
        n_attr = self.one("SELECT COUNT(*) FROM t_attribute a JOIN t_object o ON o.Object_ID=a.Object_ID "
                          "WHERE o.Package_ID=? AND o.Object_Type='Class'", self.pid)[0]
        self.say(f"{len(classes)} objecttypen, {n_attr} attributen, {len(rels)} relaties "
                 f"(waarvan {usage} Usage, ongewijzigd); {len(problems)} afwijking(en)")
        for p in problems:
            self.say(f"    AFWIJKING: {p}")
        return len(problems)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea", help="pad naar de .qea (SQLite) van Enterprise Architect")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run op een kopie)")
    args = ap.parse_args()

    target = args.qea
    if not args.apply:
        tmp = tempfile.NamedTemporaryFile(prefix="fix_model_sport_mim-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    f = Fixer(conn)
    try:
        f.fix()
        problems = f.verify()
    except BaseException:
        conn.execute("ROLLBACK")
        if not args.apply:
            conn.close()
            pathlib.Path(target).unlink(missing_ok=True)
        raise

    print(f"\n{f.changes} gewijzigde rijen; {problems} afwijking(en) in de eindcontrole")
    if args.apply and problems == 0:
        conn.execute("COMMIT")
        ok = conn.execute("PRAGMA integrity_check").fetchone()[0]
        print(f"TOEGEPAST en vastgelegd in {args.qea}; integrity_check: {ok}")
        return 0 if ok == "ok" else 1
    conn.execute("ROLLBACK")
    conn.close()
    if args.apply:
        print("NIET toegepast: de eindcontrole meldt afwijkingen")
        return 1
    pathlib.Path(target).unlink(missing_ok=True)
    print("DRY-RUN op een tijdelijke kopie: niets opgeslagen (gebruik --apply om door te voeren)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
