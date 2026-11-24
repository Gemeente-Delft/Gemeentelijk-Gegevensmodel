#!/usr/bin/env python3
"""
Import from GEMMA
=================
Importeert de door GEMMA teruggeleverde gegevens (elementen en relaties) als
tagged values in het Gemeentelijk Gegevensmodel (GGM) EA-bestand (.qea), zodat de
GEMMA-kolommen bij de export (tools/export_to_gemma.py) gevuld worden.

De GEMMA-gegevens worden gematcht op GGM-guid en weggeschreven als properties met
exact de namen die de export weer uitleest (GEMMA-naam, GEMMA-guid, GEMMA-type,
GEMMA-definitie, GEMMA-toelichting, GEMMA-synoniemen, GEMMA-bron, GEMMA-URL,
GEMMA-alternate-name voor objecten; idem + GEMMA-source-guid/GEMMA-target-guid voor
relaties).

Bron (standaard): de door GEMMA gepubliceerde CSV's in de VNG-Realisatie repo
GEMMA-GGM-Archi-repository. Een lokaal pad mag ook via --import_objects/--import_relations.

Gebruik:
    python import_gemma.py --db_uri "/pad/naar/model.qea"
    python import_gemma.py --db_uri "model.qea" --dry-run
    python import_gemma.py --db_uri "model.qea" --import_objects ./elements.csv
"""

import argparse
import os
import shutil
import socket
import sqlite3
import sys
import uuid
from collections import defaultdict

import pandas as pd

DEFAULT_TIMEOUT = 30  # seconden; voorkomt dat een trage/onbereikbare URL het proces ophangt


# ---------------------------------------------------------------------------
# Standaardwaarden en configuratie
# ---------------------------------------------------------------------------

DEFAULT_IMPORT_OBJECTS = (
    "https://raw.githubusercontent.com/VNG-Realisatie/GEMMA-GGM-Archi-repository/"
    "master/exports/GEMMA_Bedrijfsobjecten_element.csv"
)
DEFAULT_IMPORT_RELATIONS = (
    "https://raw.githubusercontent.com/VNG-Realisatie/GEMMA-GGM-Archi-repository/"
    "master/exports/GEMMA_Bedrijfsobjecten_relatie.csv"
)

# GEMMA-properties die dit script beheert. De CSV-kolomnaam is gelijk aan de
# property-naam in de EA-repository, en exact wat export_to_gemma.py weer uitleest.
OBJ_GEMMA_PROPS = [
    'GEMMA-naam', 'GEMMA-guid', 'GEMMA-type', 'GEMMA-definitie',
    'GEMMA-toelichting', 'GEMMA-synoniemen', 'GEMMA-bron', 'GEMMA-URL',
    'GEMMA-alternate-name',
]
CON_GEMMA_PROPS = [
    'GEMMA-naam', 'GEMMA-guid', 'GEMMA-type', 'GEMMA-definitie',
    'GEMMA-toelichting', 'GEMMA-source-guid', 'GEMMA-target-guid',
]


# ---------------------------------------------------------------------------
# Hulpfuncties
# ---------------------------------------------------------------------------

def new_ea_guid() -> str:
    """Genereer een EA-conform GUID, bv. {AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE}."""
    return '{' + str(uuid.uuid4()).upper() + '}'


def is_empty(val) -> bool:
    """True voor None, NaN of lege/placeholder-strings."""
    if val is None:
        return True
    if isinstance(val, float) and pd.isna(val):
        return True
    return str(val).strip() in ('', 'nan', 'None')


def read_gemma_csv(path: str) -> pd.DataFrame:
    """Lees een GEMMA-CSV (lokaal pad of URL) als strings."""
    df = pd.read_csv(path, dtype=str)
    # Bekende aanlever-variant: kolomkop 'GEMMA URL' i.p.v. 'GEMMA-URL'.
    df = df.rename(columns={'GEMMA URL': 'GEMMA-URL'})
    return df


def guid_to_id_map(con: sqlite3.Connection, sql: str) -> dict:
    """Bouw een map ea_guid (hoofdletter-ongevoelig) -> id voor objecten/connectoren."""
    mapping = {}
    for _id, ea_guid in con.execute(sql).fetchall():
        if ea_guid:
            mapping[str(ea_guid).upper()] = _id
    return mapping


def import_entities(con, df, props, id_map, table, fk_col, val_col, dry_run):
    """Idempotente upsert van GEMMA-properties voor objecten of connectoren.

    Bestaande rijen worden ge-update (PropertyID en ea_guid blijven behouden),
    nieuwe toegevoegd en verdwenen waarden verwijderd. Bij gelijke GEMMA-data
    verandert er niets, zodat de .qea niet onnodig wijzigt. Lege waarden worden
    overgeslagen; GGM-bronvelden worden niet aangeraakt.
    """
    # Gewenste waarden uit de GEMMA-CSV: {(ent_id, property): value}
    desired = {}
    matched, unmatched = set(), 0
    for _, row in df.iterrows():
        ggm_guid = row.get('GGM-guid')
        if is_empty(ggm_guid):
            continue
        ent_id = id_map.get(str(ggm_guid).strip().upper())
        if ent_id is None:
            unmatched += 1
            continue
        matched.add(ent_id)
        for prop in props:
            val = row.get(prop)
            if not is_empty(val):
                desired[(ent_id, prop)] = str(val).strip()

    # Bestaande beheerde rijen groeperen per (ent_id, property)
    placeholders = ",".join("?" * len(props))
    existing = defaultdict(list)
    for pid, eid, prop, val in con.execute(
        f"SELECT PropertyID, {fk_col}, Property, {val_col} FROM {table} "
        f"WHERE Property IN ({placeholders})", props
    ).fetchall():
        existing[(eid, prop)].append((pid, val))

    to_insert, to_update, to_delete = [], [], []
    for key, value in desired.items():
        if key in existing:
            keep_pid, keep_val = existing[key][0]
            if keep_val != value:
                to_update.append((value, keep_pid))
            to_delete.extend(pid for pid, _ in existing[key][1:])  # eventuele duplicaten opruimen
        else:
            to_insert.append((key[0], key[1], value, new_ea_guid()))
    for key, rows in existing.items():
        if key not in desired:
            to_delete.extend(pid for pid, _ in rows)

    print(
        f"  {table}: {len(matched)} entiteiten gematcht, {unmatched} niet in model "
        f"| +{len(to_insert)} nieuw, ~{len(to_update)} gewijzigd, -{len(to_delete)} verwijderd"
    )
    n_changes = len(to_insert) + len(to_update) + len(to_delete)
    if dry_run:
        return n_changes

    if to_delete:
        con.executemany(f"DELETE FROM {table} WHERE PropertyID = ?", [(p,) for p in to_delete])
    if to_update:
        con.executemany(f"UPDATE {table} SET {val_col} = ? WHERE PropertyID = ?", to_update)
    if to_insert:
        con.executemany(
            f"INSERT INTO {table} ({fk_col}, Property, {val_col}, ea_guid) VALUES (?, ?, ?, ?)",
            to_insert,
        )
    return n_changes


# ---------------------------------------------------------------------------
# Hoofdlogica
# ---------------------------------------------------------------------------

def import_gemma(db_uri, import_objects, import_relations, dry_run, timeout=DEFAULT_TIMEOUT) -> None:
    """Lees de GEMMA-CSV's en werk de GEMMA-properties in de .qea bij."""

    if not os.path.isfile(db_uri):
        raise FileNotFoundError(f"EA-bestand niet gevonden: {db_uri}")

    # Fout-tolerant: als de GEMMA-bron (URL/bestand) niet beschikbaar is, slaan we de
    # import over met een waarschuwing i.p.v. het proces (full-deploy) te laten klappen.
    socket.setdefaulttimeout(timeout)
    try:
        print(f"Inlezen GEMMA-elementen : {import_objects}")
        df_obj = read_gemma_csv(import_objects)
        print(f"Inlezen GEMMA-relaties  : {import_relations}")
        df_con = read_gemma_csv(import_relations)
    except Exception as exc:
        print(
            f"WAARSCHUWING: GEMMA-bron niet beschikbaar ({type(exc).__name__}: {exc}). "
            "Import overgeslagen; model en bestaande GEMMA-gegevens blijven ongewijzigd.",
            file=sys.stderr,
        )
        return
    print(f"GEMMA-elementen: {len(df_obj)} rijen | GEMMA-relaties: {len(df_con)} rijen")

    # Back-up vóór wijzigen (alleen als er daadwerkelijk geschreven wordt).
    if not dry_run:
        backup = db_uri + '.bak'
        shutil.copy2(db_uri, backup)
        print(f"Back-up van model gemaakt: {backup}")

    con = sqlite3.connect(db_uri)
    try:
        obj_id_map = guid_to_id_map(con, "SELECT Object_ID, ea_guid FROM t_object")
        con_id_map = guid_to_id_map(con, "SELECT Connector_ID, ea_guid FROM t_connector")

        print("Objecten:")
        changes = import_entities(con, df_obj, OBJ_GEMMA_PROPS, obj_id_map,
                                  't_objectproperties', 'Object_ID', 'Value', dry_run)
        print("Relaties:")
        changes += import_entities(con, df_con, CON_GEMMA_PROPS, con_id_map,
                                   't_connectortag', 'ElementID', 'VALUE', dry_run)

        if dry_run:
            con.rollback()
            print("DRY-RUN: geen wijzigingen weggeschreven.")
        else:
            con.commit()
            print(f"Import geslaagd! ({changes} wijziging(en) in het model)"
                  if changes else "Import gereed: GEMMA-gegevens waren al actueel, geen wijzigingen.")
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


# ---------------------------------------------------------------------------
# CLI-interface
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Importeer GEMMA-gegevens (elementen + relaties) als tagged values in het GGM (.qea).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        '--db_uri',
        required=True,
        help='Pad naar de Enterprise Architect SQLite-database (.qea bestand).',
    )
    parser.add_argument(
        '--import_objects',
        default=DEFAULT_IMPORT_OBJECTS,
        help='Pad of URL naar het GEMMA-elementen-CSV-bestand (standaard: VNG-repo).',
    )
    parser.add_argument(
        '--import_relations',
        default=DEFAULT_IMPORT_RELATIONS,
        help='Pad of URL naar het GEMMA-relaties-CSV-bestand (standaard: VNG-repo).',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Toon alleen wat er zou gebeuren; schrijf niets weg.',
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f'Netwerk-timeout (seconden) voor het ophalen van de GEMMA-bron (standaard {DEFAULT_TIMEOUT}).',
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print(f"Database  : {args.db_uri}")
    print(f"Dry-run   : {args.dry_run}")
    print()

    try:
        import_gemma(
            db_uri=args.db_uri,
            import_objects=args.import_objects,
            import_relations=args.import_relations,
            dry_run=args.dry_run,
            timeout=args.timeout,
        )
    except Exception as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
