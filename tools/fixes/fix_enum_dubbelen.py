#!/usr/bin/env python3
"""Voegt dubbele enumeratiewaarden samen in de EA-repository van het GGM (nov 2026).

Inventaris en voorstel: tools/enumeraties-dubbele-waarden.md. Een enumeratie bevat soms dezelfde
waarde twee of meer keer (OnderdeelDienstTypeRubriek, SubCategorieVordering, CdSzWet, de IMBOR-
enumeraties enum_Type en enum_TypePlus). In de LOD krijgen die waarden dan een volgnummer in hun IRI.

Regels per enumeratie:
  - dubbel = dezelfde naam, of dezelfde naam op hoofdletters en witruimte na;
  - één rij blijft: de rij met een toelichting (Notes), anders de rij met het laagste ID (de oudste;
    bij CdSzWet is dat de officiële schrijfwijze met kleine letters);
  - hebben meer rijen een verschillende toelichting, dan worden die samengevoegd in de blijvende rij,
    gescheiden door een lege regel;
  - de overige rijen gaan weg, met hun tagged values (t_attributetag);
  - waarden die alleen in de LOD-slug samenvallen (A, A+, A++) blijven staan: dat zijn echte waarden.

Standaard dry-run (mode=ro). --apply voert door in één transactie; sluit Enterprise Architect en maak
eerst een back-up. --zonder-imbor slaat het pakket 'Model Basis IMBOR' over. Idempotent.

Gebruik:
  python3 -I tools/fixes/fix_enum_dubbelen.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"
  python3 -I tools/fixes/fix_enum_dubbelen.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply --zonder-imbor
"""
import argparse
import collections
import re
import sqlite3
import sys
from datetime import datetime

IMBOR_PKG = "Model Basis IMBOR"


def fold(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip()).casefold()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run, alleen lezen)")
    ap.add_argument("--zonder-imbor", action="store_true", help="pakket 'Model Basis IMBOR' overslaan")
    args = ap.parse_args()

    conn = sqlite3.connect(args.qea if args.apply else f"file:{args.qea}?mode=ro", uri=not args.apply,
                           isolation_level=None)
    conn.row_factory = sqlite3.Row
    if args.apply:
        conn.execute("BEGIN")
    pk = {r["Package_ID"]: (r["Parent_ID"], r["Name"]) for r in conn.execute("SELECT Package_ID, Parent_ID, Name FROM t_package")}

    def in_imbor(pid) -> bool:
        while pid in pk:
            if pk[pid][1] == IMBOR_PKG:
                return True
            pid = pk[pid][0]
        return False

    lits = collections.defaultdict(list)
    for r in conn.execute("SELECT a.ID, a.Object_ID, a.Name, a.Notes, o.Name AS enum, o.Package_ID FROM t_attribute a "
                          "JOIN t_object o ON o.Object_ID=a.Object_ID WHERE o.Object_Type='Enumeration' ORDER BY a.ID"):
        if args.zonder_imbor and in_imbor(r["Package_ID"]):
            continue
        lits[(r["Object_ID"], fold(r["Name"]))].append(r)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    weg, samengevoegd, touched = 0, 0, set()
    for (oid, _), rows in sorted(lits.items(), key=lambda kv: (kv[1][0]["enum"], kv[1][0]["ID"])):
        if len(rows) < 2:
            continue
        met_notes = [r for r in rows if (r["Notes"] or "").strip()]
        keep = met_notes[0] if met_notes else rows[0]
        notes = [r["Notes"].strip() for r in met_notes]
        uniek = list(dict.fromkeys(notes))
        nieuw_notes = "\n\n".join(uniek) if len(uniek) > 1 else None
        rest = [r for r in rows if r["ID"] != keep["ID"]]
        print(f"{rows[0]['enum']}: {keep['Name']!r} blijft (ID {keep['ID']}); weg: "
              + ", ".join(f"{r['Name']!r} (ID {r['ID']})" for r in rest)
              + (f"; toelichtingen samengevoegd ({len(uniek)})" if nieuw_notes else ""))
        weg += len(rest)
        touched.add(oid)
        if args.apply:
            if nieuw_notes:
                conn.execute("UPDATE t_attribute SET Notes=? WHERE ID=?", (nieuw_notes, keep["ID"]))
                samengevoegd += 1
            for r in rest:
                conn.execute("DELETE FROM t_attributetag WHERE ElementID=?", (r["ID"],))
                conn.execute("DELETE FROM t_attribute WHERE ID=?", (r["ID"],))
    print(f"\n{weg} overtollige waarden in {len(touched)} enumeraties" + (f"; {samengevoegd} toelichtingen samengevoegd" if args.apply else ""))
    if not args.apply:
        print("DRY-RUN: de .qea is alleen gelezen (gebruik --apply om door te voeren)")
        return 0
    for oid in touched:
        conn.execute("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", (now, oid))
    conn.execute("COMMIT")
    ok = conn.execute("PRAGMA integrity_check").fetchone()[0]
    print(f"TOEGEPAST en vastgelegd in {args.qea}; integrity_check: {ok}")
    return 0 if ok == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
