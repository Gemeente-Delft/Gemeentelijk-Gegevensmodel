#!/usr/bin/env python3
"""Correctie uit GitHub-issue 57 (nov 2026) op de EA-repository van het GGM: Model Werk.

In het Proposal Werk is de Thomas-entiteit BemiddelingsActiviteit twee keer aangemaakt: eerst
als 'Bemiddelingsactiviteit', daarna opnieuw als 'Bemiddelingstraject' met dezelfde zes
attributen. Alleen de tweede staat op Detaildiagram Werk en heeft een relatie met Werkzoekende;
de eerste bleef als wees achter (geen diagram, geen relaties). De naam 'traject' past bovendien
niet bij de inhoud: de attributen beschrijven één bemiddelingscontact.

De .qea van Enterprise Architect is een SQLite-database; dit script past de correctie
rechtstreeks daarin toe, in één transactie. Standaard is het een dry-run op een tijdelijke kopie
van de .qea; met --apply wordt de transactie in de echte .qea vastgelegd. Het script is
idempotent: een tweede run meldt 0 wijzigingen.

Voorwaarden: Enterprise Architect gesloten (of het project daarna opnieuw laden) en een
back-up van de .qea gemaakt.
Nadien: model in EA controleren, diagramafbeelding en XMI opnieuw exporteren, documentatie en
LOD genereren.

Wat het script doet (nummering volgt het issue):
  1. De weesklasse Bemiddelingsactiviteit verwijderen, met haar attributen, tagged values en
     stereotype-rijen. Alleen als niets meer naar de klasse verwijst.
  2. Bemiddelingstraject hernoemen naar Bemiddelingsactiviteit (conform het Thomas-model). De
     GUID, de plaats op het diagram en de relatie met Werkzoekende blijven.
  3. Nieuwe definitie en een toelichting met de herkomst en het onderscheid met een traject.
  4. Attributen gelijktrekken met de oorspronkelijke klasse: OmschrijvingContactbemiddeling
     wordt OmschrijvingSoortContactbemiddeling met type Kanaal contactmoment (enumeratie op
     hetzelfde diagram), DatumVacature wordt DatumVerwijzingVacature.

Gebruik:
  python3 -I tools/fix_issue_57.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/fix_issue_57.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime

# --- Wat er precies verandert (GUID's uit de v3.0.0-.qea) ----------------------------------
ORPHAN = ("{7F16F190-CC44-4550-A677-7BFEC6D34E64}", "Bemiddelingsactiviteit")
KEEP = ("{1C180C62-5B5E-45b4-BB94-F44454D11BDE}", "Bemiddelingstraject", "Bemiddelingsactiviteit")
PACKAGE_NAME = "Model Werk"

DEFINITION = ("Een activiteit in het kader van arbeidstoeleiding waarbij de gemeente of "
              "uitvoeringsinstantie een werkzoekende gericht in contact brengt met een werkgever "
              "of werkplek, bijvoorbeeld door verwijzing naar een vacature.")
TOELICHTING = ("Komt overeen met BemiddelingsActiviteit in het Thomas-model (gemeente Rotterdam). "
               "Het gaat om één bemiddelingscontact, niet om een traject. Middelen om de kansen "
               "op werk te vergroten staan in Reintegratievoorziening.")

ENUM = ("{362B3FC2-A412-450f-AF4D-CF3A4B149060}", "Kanaal contactmoment")
ATTRIBUTE_CHANGES = [  # (attribuut-guid, oude naam, nieuwe naam, retype naar ENUM?)
    ("{0C49FA28-BE82-4c9a-8E5C-53590636F1B4}", "OmschrijvingContactbemiddeling",
     "OmschrijvingSoortContactbemiddeling", True),
    ("{2795FB74-A163-4db5-A763-4E38D70E4215}", "DatumVacature", "DatumVerwijzingVacature", False),
]

assert len(TOELICHTING) <= 255, "toelichting past niet in een gewone tag (max. 255 tekens)"


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
        return self.one("SELECT o.Object_ID, o.Name, o.Note, p.Name FROM t_object o "
                        "JOIN t_package p ON p.Package_ID=o.Package_ID WHERE upper(o.ea_guid)=upper(?)", guid)

    def touch(self, object_id: int) -> None:
        self.c.execute("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", (self.now, object_id))

    def _reference_columns(self) -> list[tuple[str, str]]:
        refs = []
        for (tbl,) in self.c.execute("SELECT name FROM sqlite_master WHERE type='table' "
                                     "AND name LIKE 't\\_%' ESCAPE '\\'"):
            cols = {r[1] for r in self.c.execute(f"PRAGMA table_info({tbl})")}
            for col in ("Object_ID", "Start_Object_ID", "End_Object_ID", "ParentID", "Classifier"):
                if col in cols and not (tbl == "t_object" and col == "Object_ID") and tbl != "t_objectproperties":
                    refs.append((tbl, col))
        return refs

    # -- stappen ---------------------------------------------------------------------------
    def delete_orphan(self) -> None:
        self.step("1. Weesklasse verwijderen")
        guid, name = ORPHAN
        obj = self.object_by_guid(guid)
        if obj is None:
            self.say(f"al gedaan: {name} {guid} bestaat niet meer")
            return
        oid, cur, _, pkg = obj
        if cur != name or pkg != PACKAGE_NAME:
            self.warn(f"{guid} heet {cur!r} in {pkg!r}, verwacht {name!r} in {PACKAGE_NAME!r}; niet verwijderd")
            return
        # Eerst kijken of er buiten de eigen attributen iets naar de klasse verwijst.
        used = [(t, c, self.one(f"SELECT COUNT(*) FROM {t} WHERE {c}=?", oid)[0])
                for t, c in self._reference_columns() if (t, c) != ("t_attribute", "Object_ID")]
        used = [u for u in used if u[2]]
        if used:
            self.warn(f"{name} wordt nog gebruikt ({', '.join(f'{t}.{c}={n}' for t, c, n in used)}); niet verwijderd")
            return
        attrs = self.c.execute("SELECT ID, ea_guid, Name FROM t_attribute WHERE Object_ID=?", (oid,)).fetchall()
        tags = xref = cons = 0
        has_cons = self.one("SELECT 1 FROM sqlite_master WHERE type='table' AND name='t_attributeconstraints'")
        for aid, aguid, _ in attrs:
            tags += self.run("DELETE FROM t_attributetag WHERE ElementID=?", aid)
            xref += self.run("DELETE FROM t_xref WHERE upper(Client)=upper(?)", aguid)
            if has_cons:
                cons += self.run("DELETE FROM t_attributeconstraints WHERE ID=?", aid)
        n_attrs = self.run("DELETE FROM t_attribute WHERE Object_ID=?", oid)
        otags = self.run("DELETE FROM t_objectproperties WHERE Object_ID=?", oid)
        oxref = self.run("DELETE FROM t_xref WHERE upper(Client)=upper(?)", guid)
        self.run("DELETE FROM t_object WHERE Object_ID=?", oid)
        self.say(f"verwijderd: {name} ({n_attrs} attributen met {tags} tagged values, {xref} xref-rijen"
                 f"{f' en {cons} constraints' if cons else ''}; {otags} tagged values en {oxref} xref-rijen op de klasse)")

    def rename_class(self) -> int | None:
        self.step("2/3. Bemiddelingstraject wordt Bemiddelingsactiviteit, met definitie en toelichting")
        guid, old, new = KEEP
        obj = self.object_by_guid(guid)
        if obj is None:
            self.warn(f"{guid} ({old}) niet gevonden")
            return None
        oid, cur, note, pkg = obj
        if cur not in (old, new) or pkg != PACKAGE_NAME:
            self.warn(f"{guid} heet {cur!r} in {pkg!r}, verwacht {old!r} in {PACKAGE_NAME!r}; overgeslagen")
            return None
        if cur == old:
            pkg_id = self.one("SELECT Package_ID FROM t_object WHERE Object_ID=?", oid)[0]
            dup = self.one("SELECT ea_guid FROM t_object WHERE Package_ID=? AND Name=? AND Object_ID<>?", pkg_id, new, oid)
            if dup:
                self.warn(f"naamgenoot {new!r} ({dup[0]}) staat nog in {PACKAGE_NAME}; niet hernoemd")
                return None
            self.run("UPDATE t_object SET Name=? WHERE Object_ID=?", new, oid)
            n = self.run("UPDATE t_attribute SET Type=? WHERE Classifier=? AND Type<>?", new, oid, new)
            self.touch(oid)
            self.say(f"{old!r} -> {new!r}" + (f" (+ {n} attribuuttype(n))" if n else ""))
        else:
            self.say(f"al gedaan: {new!r}")
        if note == DEFINITION:
            self.say("al gedaan: definitie")
        else:
            self.run("UPDATE t_object SET Note=? WHERE Object_ID=?", DEFINITION, oid)
            self.touch(oid)
            self.say(f"definitie was {note!r}")
        row = self.one("SELECT PropertyID, Value FROM t_objectproperties WHERE Object_ID=? AND Property='Toelichting'", oid)
        if row is None:
            self.warn("tag 'Toelichting' ontbreekt; niet gezet")
        elif row[1] == TOELICHTING:
            self.say("al gedaan: toelichting")
        elif (row[1] or "").strip():
            self.warn(f"toelichting is al gevuld ({row[1]!r}); niet overschreven")
        else:
            self.run("UPDATE t_objectproperties SET Value=? WHERE PropertyID=?", TOELICHTING, row[0])
            self.touch(oid)
            self.say("toelichting gezet")
        return oid

    def attributes(self, oid: int) -> None:
        self.step("4. Attributen gelijktrekken met de oorspronkelijke klasse")
        enum = self.object_by_guid(ENUM[0])
        if enum is None or enum[1] != ENUM[1] or enum[3] != PACKAGE_NAME:
            self.warn(f"enumeratie {ENUM[1]} ({ENUM[0]}) niet gevonden in {PACKAGE_NAME}; attributen overgeslagen")
            return
        for aguid, old, new, retype in ATTRIBUTE_CHANGES:
            row = self.one("SELECT ID, Name, Type, Classifier, Object_ID FROM t_attribute WHERE upper(ea_guid)=upper(?)", aguid)
            if row is None or row[4] != oid:
                self.warn(f"attribuut {aguid} ({old}) niet gevonden op de klasse")
                continue
            aid, name, typ, classifier = row[:4]
            if name not in (old, new):
                self.warn(f"attribuut {aguid} heet {name!r}, verwacht {old!r}; overgeslagen")
                continue
            done = []
            if name == old:
                self.run("UPDATE t_attribute SET Name=? WHERE ID=?", new, aid)
                done.append(f"{old!r} -> {new!r}")
            if retype and (typ != ENUM[1] or str(classifier) != str(enum[0])):
                # t_attribute.Classifier is een TEXT-kolom (EA slaat de Object_ID als tekst op).
                self.run("UPDATE t_attribute SET Type=?, Classifier=? WHERE ID=?", ENUM[1], str(enum[0]), aid)
                done.append(f"type {typ!r} -> {ENUM[1]!r}")
            if done:
                self.touch(oid)
                self.say("; ".join(done))
            else:
                self.say(f"al gedaan: {new}" + (f" : {ENUM[1]}" if retype else ""))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea", help="pad naar de .qea (SQLite) van Enterprise Architect")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run)")
    args = ap.parse_args()

    target = args.qea
    if not args.apply:
        # Dry-run op een kopie, zodat het origineel byte-voor-byte onaangeroerd blijft.
        tmp = tempfile.NamedTemporaryFile(prefix="fix_issue_57-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    f = Fixer(conn)
    try:
        f.delete_orphan()
        oid = f.rename_class()
        if oid is not None:
            f.attributes(oid)
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
