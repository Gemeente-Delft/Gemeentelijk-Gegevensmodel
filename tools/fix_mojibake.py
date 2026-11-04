#!/usr/bin/env python3
"""Herstelt verkeerd gecodeerde tekens (mojibake) in de EA-repository van het GGM (nov 2026).

Bij de IMBOR-import is UTF-8-tekst als Windows-1252 gelezen en opnieuw als UTF-8 opgeslagen: "één"
werd "Ã©Ã©n", "’" werd "â€™". Het script zoekt zulke tekst in de namen en toelichtingen van
enumeratiewaarden, attributen en objecten en draait de dubbele codering terug (tekst → cp1252-bytes →
UTF-8). Alleen teksten die daarna geen Ã of â€ meer bevatten worden gewijzigd; de rest wordt gemeld.
Harde spaties (U+00A0) worden gewone spaties en namen verliezen witruimte aan de randen.

Standaard dry-run (mode=ro); --apply schrijft in één transactie. Idempotent.

Gebruik:
  python3 -I tools/fix_mojibake.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"
  python3 -I tools/fix_mojibake.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply
"""
import argparse
import re
import sqlite3
import sys
from datetime import datetime

KENMERK = re.compile(r"Ã.|â€.|Â.")
VELDEN = (
    ("t_attribute", "ID", "Name", "enumeratiewaarde/attribuut naam"),
    ("t_attribute", "ID", "Notes", "enumeratiewaarde/attribuut toelichting"),
    ("t_object", "Object_ID", "Name", "object naam"),
    ("t_object", "Object_ID", "Note", "object toelichting"),
    ("t_attributetag", "PropertyID", "VALUE", "attribuuttag"),
    ("t_objectproperties", "PropertyID", "Value", "objecttag"),
)


def herstel(s: str):
    """Geeft de herstelde tekst, of None als de tekst niet (volledig) te herstellen is."""
    uit = s
    for _ in range(3):  # soms is de tekst meer dan één keer dubbel gecodeerd
        if not KENMERK.search(uit):
            return uit
        try:
            kandidaat = uit.encode("cp1252").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            try:
                kandidaat = uit.encode("latin-1").decode("utf-8")
            except (UnicodeEncodeError, UnicodeDecodeError):
                return None
        uit = kandidaat
    return None if KENMERK.search(uit) else uit


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run, alleen lezen)")
    args = ap.parse_args()
    conn = sqlite3.connect(args.qea if args.apply else f"file:{args.qea}?mode=ro", uri=not args.apply,
                           isolation_level=None)
    if args.apply:
        conn.execute("BEGIN")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    totaal, niet, touched_obj = 0, [], set()
    for tabel, sleutel, veld, label in VELDEN:
        rijen = conn.execute(f'SELECT {sleutel}, "{veld}"' + (", Object_ID" if tabel == "t_attribute" else "")
                             + f' FROM {tabel} WHERE "{veld}" LIKE \'%Ã%\' OR "{veld}" LIKE \'%â€%\' OR "{veld}" LIKE \'%Â%\''
                             + f' OR instr("{veld}", char(160)) > 0').fetchall()
        n = 0
        for r in rijen:
            nieuw = herstel(r[1])
            if nieuw is None:
                niet.append((label, r[0], r[1][:80]))
                continue
            # Een harde spatie (U+00A0, uit Word geplakt) wordt een gewone; namen verliezen witruimte aan de randen.
            nieuw = nieuw.replace("\xa0", " ")
            if veld == "Name":
                nieuw = nieuw.strip()
            if nieuw == r[1]:
                continue
            n += 1
            if n <= 4 or tabel != "t_attribute":
                kort = lambda t: re.sub(r"\s+", " ", t)[:70]
                print(f"  {label} {r[0]}: {kort(r[1])!r} -> {kort(nieuw)!r}")
            if args.apply:
                conn.execute(f'UPDATE {tabel} SET "{veld}"=? WHERE {sleutel}=?', (nieuw, r[0]))
                if tabel == "t_attribute":
                    touched_obj.add(r[2])
                elif tabel == "t_object":
                    touched_obj.add(r[0])
        print(f"{label}: {n} hersteld van {len(rijen)}")
        totaal += n
    for label, key, tekst in niet:
        print(f"  NIET hersteld ({label} {key}): {tekst!r}")
    print(f"\n{totaal} teksten hersteld; {len(niet)} niet te herstellen")
    if not args.apply:
        print("DRY-RUN: de .qea is alleen gelezen (gebruik --apply om door te voeren)")
        return 0
    for oid in touched_obj:
        conn.execute("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", (now, oid))
    conn.execute("COMMIT")
    ok = conn.execute("PRAGMA integrity_check").fetchone()[0]
    print(f"TOEGEPAST en vastgelegd in {args.qea}; integrity_check: {ok}")
    return 0 if ok == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
