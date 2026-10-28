#!/usr/bin/env python3
"""Correcties uit GitHub-issue 53 (Frits de Groot, okt 2026) op de EA-repository van het GGM.

De .qea van Enterprise Architect is een SQLite-database; dit script past de correcties
rechtstreeks daarin toe. Alles loopt in één transactie. Standaard is het een dry-run op een
tijdelijke kopie van de .qea (alle statements worden daar uitgevoerd, zodat de aantallen
exact zijn; het echte bestand wordt niet eens voor schrijven geopend), met --apply wordt
de transactie in de echte .qea vastgelegd. Het script is idempotent: een tweede run meldt 0 wijzigingen.

Voorwaarden: Enterprise Architect gesloten en een back-up van de .qea gemaakt.
Nadien: model in EA controleren (vooral de Boundaries zonder stereotype en de legenda),
XMI opnieuw exporteren en de documentatie/LOD genereren (task full-deploy).

Wat het script doet (nummering volgt het issue):
  1. Typfouten: Nertwerkcomponent, Flexibliteit, Instituuttioneel Huishouden. De tagged
     value 'GEMMA naam' op Netwerkcomponent blijft 'Nertwerkcomponent': GEMMA Online spelt
     het zelf ook zo (melden bij VNG Realisatie).
  2. Oplossingssoort.soort verwijst naar EnumOplossingssoort in plaats van EnumSchuldensoort.
  3. Tagged values: één spelling per naam (de dominante spelling met spaties, enkele spatie,
     geen spatie aan het eind) op objecten, attributen en relaties. Staat op hetzelfde
     element ook al de doelspelling, dan wordt de waarde samengevoegd (leeg doel krijgt de
     waarde); verschillen beide gevuld, dan blijft het staan en wordt het gemeld.
     Plus: 'GEMMA naam' van Aanwezige Deelnemer = 'Aanwezige Deelnemer' (GEMMA Online,
     id ccf78bc5); de waarde 'MaatschappelijkeActiviteit' was fout.
  4. Stereotype Objecttype weg van alle Boundaries (13) en van het naamloze tekstelement in
     de legenda. De legenda-klassen ObjecttypeA t/m G houden het stereotype: zonder tonen
     ze niet meer hoe een objecttype getekend wordt; afnemers sluiten het pakket Tekenwijze
     uit (zoals de eigen LOD-export doet). Linkbaar CMDB-item wordt abstract met een echte
     definitie (was 'Niet opnemen'). Deelplan/Veld en Fase/Oplevering (leeg, nergens
     gebruikt) worden verwijderd.
  5. enum_Incidenttype, enum_Leefgebied, enum_Verzoeksoort -> EnumX (de 115 IMBOR-
     enumeraties met enum_ blijven: die volgen IMBOR en geen attribuut gebruikt ze).
  6. Spaties en regeleinden aan begin/eind van namen van klassen en enumeraties weg (ook
     in attribuuttypen). Omdat Aandachtspunt en Ontwikkelwens een enumeratie-naamgenoot
     in hetzelfde pakket hebben (de spatie hield ze uit elkaar), en Gebruikerrol en
     Leveringsvorm dat zonder spatie al hadden, krijgen die vier enumeraties eerst de naam
     EnumX; in de LOD kregen klasse en enumeratie anders dezelfde IRI.

Gebruik:
  python3 -I tools/fix_issue_53.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/fix_issue_53.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime

OBJECTTYPE_STEREO = "@STEREO;Name=Objecttype;FQName=VNGR SIM+Grouping NL::Objecttype;@ENDSTEREO;"
WS = " \t\r\n"

# --- Wat er precies verandert (GUID's uit het issue en uit de v3.0.0-.qea) -----------------
TYPO_OBJECTS = [  # (guid, oude naam, nieuwe naam)
    ("{DD277E82-0CA5-4460-918F-9178B5F01886}", "Nertwerkcomponent", "Netwerkcomponent"),
    ("{E7BC941E-A54D-49e1-8F77-1D8D7CE8EBD7}", "Flexibliteit", "Flexibiliteit"),
]
TYPO_ATTRIBUTES = [
    ("{C82C554A-BC88-4bb6-9A50-F9CFAE5D7A33}", "Instituuttioneel Huishouden", "Institutioneel Huishouden"),
]
ATTRIBUTE_RETYPE = [  # (attribuut-guid, nieuwe classifier-guid, nieuwe typenaam)
    ("{7FB7917F-F168-449e-B624-7CB7F67444B6}", "{540A2D4C-EF40-457a-A7DD-C8E81DB692A6}", "EnumOplossingssoort"),
]
OBJECT_TAG_RENAMES = {
    "Aanduiding  strijdigheid/nietigheid": "Aanduiding strijdigheid/nietigheid",
    "Data locatie ": "Data locatie",
    "datum-tijd-export": "Datum tijd export",
    "domein-dcat": "Domein DCAT",
    "domein-gemma": "Domein GEMMA",
    "domein-iv3": "Domein IV3",
    "GEMMA-alternate-name": "GEMMA alternate name",
    "GEMMA-bron": "GEMMA bron",
    "GEMMA-definitie": "GEMMA definitie",
    "GEMMA-guid": "GEMMA guid",
    "GEMMA-naam": "GEMMA naam",
    "GEMMA-synoniemen": "GEMMA synoniemen",
    "GEMMA-toelichting": "GEMMA toelichting",
    "GEMMA-type": "GEMMA type",
    "GEMMA-URL": "GEMMA url",
    "Ref-release": "Ref release",
    "Ref-version": "Ref version",
}
ATTRIBUTE_TAG_RENAMES = {
    "Aanduiding  strijdigheid/nietigheid": "Aanduiding strijdigheid/nietigheid",
    "Code ": "Code",
    "Herkomst ": "Herkomst",
    "Toelichting ": "Toelichting",
}
CONNECTOR_TAG_RENAMES = {
    "Aanduiding  strijdigheid/nietigheid": "Aanduiding strijdigheid/nietigheid",
}
TAG_VALUE_FIXES = [  # (object-guid, tag, oude waarde, nieuwe waarde)
    ("{F1E55DC7-0F33-40ea-8713-2E1AC3D7EE8D}", "GEMMA naam", "MaatschappelijkeActiviteit", "Aanwezige Deelnemer"),
]
TEXT_ELEMENT_WITHOUT_STEREO = ["{47EA6A95-24DD-4ff9-BC2C-1B9BBC08C694}"]  # naamloos tekstelement, legenda
ABSTRACT_WITH_DEFINITION = [
    ("{C0F1A08E-C6CD-4524-A2E0-0E5CA483DCFD}", "Linkbaar CMDB-item",
     "CMDB-item dat via een koppeling met andere CMDB-items verbonden kan worden, "
     "zoals een server, database of applicatie."),
]
DELETE_OBJECTS = [
    ("{EC994E7D-E6D1-4243-BA96-38DB7454ECEF}", "Deelplan/Veld"),
    ("{7FA358CC-1160-490b-A543-D5ED69A558D2}", "Fase/Oplevering"),
]
ENUM_RENAMES = [  # (guid, oude naam, nieuwe naam)
    ("{2296EC14-B00D-4836-B553-1CB1F48CFDB2}", "enum_Incidenttype", "EnumIncidenttype"),
    ("{78D6A864-04BD-4d3f-BB6A-CC9840566D19}", "enum_Leefgebied", "EnumLeefgebied"),
    ("{3D8D8ED8-A382-4ffb-8608-4846CFF95E28}", "enum_Verzoeksoort", "EnumVerzoeksoort"),
    # naamgenoten van een klasse in hetzelfde pakket (punt 6)
    ("{B16DEA22-40DB-45a9-ADD9-5C1410F499B8}", "Aandachtspunt", "EnumAandachtspunt"),
    ("{2FCD9A74-460D-4042-A207-FF78590CEBE6}", "Ontwikkelwens", "EnumOntwikkelwens"),
    ("{262A7A23-0CBB-4991-A1B2-D5D3E509549C}", "Gebruikerrol", "EnumGebruikerrol"),
    ("{DC1D1F90-E28B-4fb7-A5E1-C2F76132BE12}", "Leveringsvorm", "EnumLeveringsvorm"),
]


class Fixer:
    def __init__(self, conn: sqlite3.Connection):
        self.c = conn
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changes = 0
        self.warnings: list[str] = []

    # -- hulpfuncties -------------------------------------------------------------------
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

    def object_by_guid(self, guid: str):
        return self.one("SELECT Object_ID, Name, Object_Type, Stereotype, Abstract, Note "
                        "FROM t_object WHERE upper(ea_guid)=upper(?)", guid)

    def touch(self, object_id: int) -> None:
        self.c.execute("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", (self.now, object_id))

    def rename_object(self, guid: str, old: str, new: str) -> None:
        row = self.object_by_guid(guid)
        if row is None:
            self.warn(f"object {guid} ({old}) niet gevonden")
            return
        oid, name = row[0], row[1]
        if name == new:
            self.say(f"al gedaan: {new!r}")
            return
        if name != old:
            self.warn(f"object {guid} heet {name!r}, verwacht {old!r}; overgeslagen")
            return
        self.run("UPDATE t_object SET Name=? WHERE Object_ID=?", new, oid)
        self.touch(oid)
        n = self.run("UPDATE t_attribute SET Type=? WHERE Classifier=? AND Type<>?", new, oid, new)
        self.say(f"{old!r} -> {new!r}" + (f" (+ {n} attribuuttype(n))" if n else ""))

    # -- stappen ---------------------------------------------------------------------------
    def typos(self) -> None:
        self.step("1. Typfouten")
        for guid, old, new in TYPO_OBJECTS:
            self.rename_object(guid, old, new)
        for guid, old, new in TYPO_ATTRIBUTES:
            row = self.one("SELECT ID, Name FROM t_attribute WHERE upper(ea_guid)=upper(?)", guid)
            if row is None:
                self.warn(f"attribuut {guid} ({old}) niet gevonden")
            elif row[1] == new:
                self.say(f"al gedaan: {new!r}")
            elif row[1] != old:
                self.warn(f"attribuut {guid} heet {row[1]!r}, verwacht {old!r}; overgeslagen")
            else:
                self.run("UPDATE t_attribute SET Name=? WHERE ID=?", new, row[0])
                self.say(f"enumeratiewaarde {old!r} -> {new!r}")
        row = self.one("SELECT Value FROM t_objectproperties WHERE Property='GEMMA naam' AND Object_ID="
                       "(SELECT Object_ID FROM t_object WHERE upper(ea_guid)=upper(?))", TYPO_OBJECTS[0][0])
        if row and row[0] == "Nertwerkcomponent":
            self.say("tagged value 'GEMMA naam' blijft 'Nertwerkcomponent' (zo staat het op GEMMA Online)")

    def retype(self) -> None:
        self.step("2. Verwijzing naar enumeratie")
        for attr_guid, cls_guid, type_name in ATTRIBUTE_RETYPE:
            cls = self.object_by_guid(cls_guid)
            attr = self.one("SELECT ID, Name, Type, Classifier, (SELECT Name FROM t_object o WHERE o.Object_ID=a.Object_ID) "
                            "FROM t_attribute a WHERE upper(ea_guid)=upper(?)", attr_guid)
            if cls is None or attr is None:
                self.warn(f"attribuut {attr_guid} of classifier {cls_guid} niet gevonden")
                continue
            if cls[1] != type_name:
                self.warn(f"classifier {cls_guid} heet {cls[1]!r}, verwacht {type_name!r}; overgeslagen")
                continue
            # t_attribute.Classifier is een TEXT-kolom (EA slaat de Object_ID als tekst op).
            if attr[2] == type_name and str(attr[3]) == str(cls[0]):
                self.say(f"al gedaan: {attr[4]}.{attr[1]} : {type_name}")
                continue
            self.run("UPDATE t_attribute SET Type=?, Classifier=? WHERE ID=?", type_name, str(cls[0]), attr[0])
            self.say(f"{attr[4]}.{attr[1]}: {attr[2]} -> {type_name}")

    def _normalise_tags(self, table: str, elem_col: str, value_col: str, notes_col: str,
                        renames: dict[str, str], label: str) -> None:
        for variant, target in renames.items():
            rows = self.c.execute(
                f"SELECT PropertyID, {elem_col}, {value_col}, {notes_col} FROM {table} WHERE Property=?",
                (variant,)).fetchall()
            if not rows:
                continue
            renamed = merged = dropped = kept = 0
            for pid, elem, value, notes in rows:
                tgt = self.one(f"SELECT PropertyID, {value_col}, {notes_col} FROM {table} "
                               f"WHERE {elem_col}=? AND Property=?", elem, target)
                if tgt is None:
                    self.run(f"UPDATE {table} SET Property=? WHERE PropertyID=?", target, pid)
                    renamed += 1
                    continue
                tpid, tvalue, tnotes = tgt
                # Het notitieveld is alleen inhoud bij een memo-tag (waarde '<memo>'); anders staat
                # er de beschrijving van de tag uit het profiel, en telt alleen de waarde.
                memo = (value or "") == "<memo>"
                same = (value or "") == (tvalue or "") and (not memo or (notes or "") == (tnotes or ""))
                target_empty = not (tvalue or "").strip()
                if same:
                    self.run(f"DELETE FROM {table} WHERE PropertyID=?", pid)
                    dropped += 1
                elif target_empty:
                    if memo:
                        self.run(f"UPDATE {table} SET {value_col}=?, {notes_col}=? WHERE PropertyID=?", value, notes, tpid)
                    else:
                        self.run(f"UPDATE {table} SET {value_col}=? WHERE PropertyID=?", value, tpid)
                    self.run(f"DELETE FROM {table} WHERE PropertyID=?", pid)
                    merged += 1
                else:
                    kept += 1
                    self.warn(f"{label} {elem}: {variant!r}={value!r} en {target!r}={tvalue!r} verschillen; "
                              "handmatig beoordelen")
            parts = [f"{renamed} hernoemd"] if renamed else []
            parts += [f"{merged} samengevoegd"] if merged else []
            parts += [f"{dropped} dubbel verwijderd"] if dropped else []
            parts += [f"{kept} laten staan"] if kept else []
            self.say(f"{label}: {variant!r} -> {target!r}: " + ", ".join(parts))

    def tagged_values(self) -> None:
        self.step("3. Tagged values")
        self._normalise_tags("t_objectproperties", "Object_ID", "Value", "Notes", OBJECT_TAG_RENAMES, "object")
        self._normalise_tags("t_attributetag", "ElementID", "VALUE", "NOTES", ATTRIBUTE_TAG_RENAMES, "attribuut")
        self._normalise_tags("t_connectortag", "ElementID", "VALUE", "NOTES", CONNECTOR_TAG_RENAMES, "relatie")
        for guid, tag, old, new in TAG_VALUE_FIXES:
            obj = self.object_by_guid(guid)
            if obj is None:
                self.warn(f"object {guid} niet gevonden")
                continue
            row = self.one("SELECT PropertyID, Value FROM t_objectproperties WHERE Object_ID=? AND Property=?", obj[0], tag)
            if row is None:
                self.warn(f"{obj[1]}: tag {tag!r} ontbreekt")
            elif row[1] == new:
                self.say(f"al gedaan: {obj[1]} {tag}={new!r}")
            elif row[1] != old:
                self.warn(f"{obj[1]}: {tag}={row[1]!r}, verwacht {old!r}; overgeslagen")
            else:
                self.run("UPDATE t_objectproperties SET Value=? WHERE PropertyID=?", new, row[0])
                self.touch(obj[0])
                self.say(f"{obj[1]}: {tag} {old!r} -> {new!r}")

    def _drop_objecttype_stereo(self, oid: int, guid: str, label: str) -> None:
        self.run("UPDATE t_object SET Stereotype=NULL WHERE Object_ID=? AND Stereotype='Objecttype'", oid)
        self.touch(oid)
        for xid, desc in self.c.execute("SELECT XrefID, Description FROM t_xref WHERE Name='Stereotypes' "
                                        "AND upper(Client)=upper(?)", (guid,)).fetchall():
            if desc == OBJECTTYPE_STEREO:
                self.run("DELETE FROM t_xref WHERE XrefID=?", xid)
            elif OBJECTTYPE_STEREO in (desc or ""):
                self.run("UPDATE t_xref SET Description=? WHERE XrefID=?", desc.replace(OBJECTTYPE_STEREO, ""), xid)
                self.warn(f"{label}: meerdere stereotypes; alleen Objecttype verwijderd")
        self.say(f"stereotype weg: {label}")

    def stereotypes(self) -> None:
        self.step("4. Stereotype Objecttype op hulpelementen")
        rows = self.c.execute(
            "SELECT o.Object_ID, o.ea_guid, o.Name, p.Name FROM t_object o JOIN t_package p ON p.Package_ID=o.Package_ID "
            "WHERE o.Object_Type='Boundary' AND o.Stereotype='Objecttype' ORDER BY p.Name, o.Name").fetchall()
        for oid, guid, name, pkg in rows:
            self._drop_objecttype_stereo(oid, guid, f"Boundary {name!r} ({pkg})")
        if not rows:
            self.say("al gedaan: geen Boundary met stereotype Objecttype meer")
        for guid in TEXT_ELEMENT_WITHOUT_STEREO:
            obj = self.object_by_guid(guid)
            if obj is None:
                self.warn(f"tekstelement {guid} niet gevonden")
            elif obj[3] != "Objecttype":
                self.say("al gedaan: tekstelement legenda zonder stereotype")
            else:
                self._drop_objecttype_stereo(obj[0], guid, f"{obj[2]}-element (legenda Tekenwijze)")
        for guid, name, definition in ABSTRACT_WITH_DEFINITION:
            obj = self.object_by_guid(guid)
            if obj is None or obj[1] != name:
                self.warn(f"{name} ({guid}) niet gevonden")
                continue
            if obj[4] == "1" and obj[5] == definition:
                self.say(f"al gedaan: {name} abstract met definitie")
                continue
            self.run("UPDATE t_object SET Abstract='1', Note=? WHERE Object_ID=?", definition, obj[0])
            self.touch(obj[0])
            self.say(f"{name}: abstract, definitie was {obj[5]!r}")
        self._delete_objects()

    def _delete_objects(self) -> None:
        ref_tables = []
        for (tbl,) in self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 't\\_%' ESCAPE '\\'"):
            cols = {r[1] for r in self.c.execute(f"PRAGMA table_info({tbl})")}
            for col in ("Object_ID", "Start_Object_ID", "End_Object_ID", "ParentID", "Classifier"):
                if col in cols and not (tbl == "t_object" and col in ("Object_ID",)) and tbl != "t_objectproperties":
                    ref_tables.append((tbl, col))
        for guid, name in DELETE_OBJECTS:
            obj = self.object_by_guid(guid)
            if obj is None:
                self.say(f"al gedaan: {name} bestaat niet meer")
                continue
            if obj[1] != name:
                self.warn(f"{guid} heet {obj[1]!r}, verwacht {name!r}; niet verwijderd")
                continue
            oid = obj[0]
            used = [(t, c, self.one(f"SELECT COUNT(*) FROM {t} WHERE {c}=?", oid)[0]) for t, c in ref_tables]
            used = [u for u in used if u[2]]
            if used:
                self.warn(f"{name} wordt nog gebruikt ({', '.join(f'{t}.{c}={n}' for t, c, n in used)}); niet verwijderd")
                continue
            tags = self.run("DELETE FROM t_objectproperties WHERE Object_ID=?", oid)
            xref = self.run("DELETE FROM t_xref WHERE upper(Client)=upper(?)", guid)
            self.run("DELETE FROM t_object WHERE Object_ID=?", oid)
            self.say(f"verwijderd: {name} ({tags} tagged values, {xref} xref-rijen)")

    def enum_renames(self) -> None:
        self.step("5/6. Enumeraties hernoemen")
        for guid, old, new in ENUM_RENAMES:
            self.rename_object(guid, old, new)

    def trim_names(self) -> None:
        self.step("6. Witruimte aan begin/eind van namen")
        rows = self.c.execute("SELECT Object_ID, Name, Object_Type, Package_ID FROM t_object "
                              "WHERE Object_Type IN ('Class','Enumeration')").fetchall()
        for oid, name, otype, pkg in rows:
            new = name.strip(WS)
            if new == name:
                continue
            dup = self.one("SELECT Name FROM t_object WHERE Package_ID=? AND Name=? AND Object_ID<>?", pkg, new, oid)
            if dup:
                self.warn(f"{otype} {name!r}: naamgenoot {new!r} in hetzelfde pakket; niet getrimd")
                continue
            self.run("UPDATE t_object SET Name=? WHERE Object_ID=?", new, oid)
            self.touch(oid)
            n = self.run("UPDATE t_attribute SET Type=? WHERE Classifier=? AND Type<>?", new, oid, new)
            self.say(f"{otype} {name!r} -> {new!r}" + (f" (+ {n} attribuuttype(n))" if n else ""))
        if not any(r[1] != r[1].strip(WS) for r in rows):
            self.say("al gedaan: geen namen met witruimte aan begin/eind")
        n = self.run("UPDATE t_attribute SET Type=trim(Type, ' ' || char(9) || char(10) || char(13)) "
                     "WHERE Type IS NOT NULL AND Type<>trim(Type, ' ' || char(9) || char(10) || char(13))")
        if n:
            self.say(f"{n} attribuuttype(n) getrimd")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea", help="pad naar de .qea (SQLite) van Enterprise Architect")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run)")
    args = ap.parse_args()

    target = args.qea
    if not args.apply:
        # Dry-run op een kopie: een rollback laat in SQLite de inhoud van vrije pagina's
        # ongemoeid, waardoor het bestand byte-voor-byte kan afwijken; zo blijft het origineel
        # onaangeroerd.
        tmp = tempfile.NamedTemporaryFile(prefix="fix_issue_53-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    f = Fixer(conn)
    try:
        f.typos()
        f.retype()
        f.tagged_values()
        f.stereotypes()
        f.enum_renames()
        f.trim_names()
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
