#!/usr/bin/env python3
"""
Export to GEMMA
===============
Exporteert objecttypes en relaties vanuit het Gemeentelijk Gegevensmodel (GGM)
naar een CSV-formaat dat door GEMMA ingelezen kan worden.

Gebruik:
    python export_to_gemma.py --db_uri "/pad/naar/model.qea"
    python export_to_gemma.py --db_uri "/pad/naar/model.qea" --root_guid "{D7FD597E-...}" --output_dir "./output"
"""

import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime

import pandas as pd
from treelib import Tree


# ---------------------------------------------------------------------------
# Overgenomen uit database.py
# ---------------------------------------------------------------------------

object_properties = [
    'object_id', 'object_type', 'stereotype', 'name', 'alias', 'author',
    'version', 'objectnote', 'pdata1', 'ea_guid', 'parentid', 'package_id',
    'modifieddate', 'note',
]

output_properties = [
    'object_id', 'object_type', 'stereotype', 'name', 'alias', 'author',
    'version', 'objectnote', 'ea_guid', 'modifieddate',
    'attributes', 'start_connectors', 'end_connectors', 'note', 'package_id',
]

sql_classes = """select
o.object_id as object_id,
o.stereotype as stereotype,
o.Object_Type as object_type,
o.Name as name,
o.Alias as alias,
o.Author as author,
o.Version as version,
o.Note as objectnote,
o.pdata1 as pdata1,
o.ea_guid as ea_guid,
o.ParentID as parentid,
o.Package_ID as package_id,
o.Note as note,
o.ModifiedDate as modifieddate
FROM t_object o
Where o.Object_Type IN ('Package', 'Class', 'Enumeration', 'DataType')"""

sql_connectors = """select
c.Name as connector_name,
c.Connector_Type as connector_type,
c.Start_object_id as start_object_id,
c.End_object_id as end_object_id,
c.SourceCard as connector_sourcecard,
c.DestCard as connector_destcard,
c.SourceRole as connector_sourcerole,
c.DestRole as connector_destrole,
c.Top_Start_Label as top_start_label,
c.Top_Mid_Label as top_mid_label,
c.Top_End_Label as top_end_label,
c.ea_guid as connector_ea_guid,
c.connector_ID as connector_id,
c.Notes as note,
so.Name as start_object_name,
so.ea_guid as ea_guid_source,
eo.Name as end_object_name,
eo.ea_guid as ea_guid_dest
FROM t_connector c, t_object so, t_object eo
Where c.Connector_Type IN ('Association', 'Generalization')
 AND so.object_id = c.Start_object_id
 AND eo.object_id = c.End_object_id"""


def get_parent(package_ID, df_objecten):
    """Geeft een keten van alle parent-IDs terug, gescheiden door koppeltekens."""
    pID = str(package_ID)
    df_package = df_objecten[df_objecten.pdata1 == pID]
    if not df_package.empty:
        value = str(df_package['package_id'].iloc[0])
        return str(pID + '-' + get_parent(value, df_objecten))
    else:
        return str(pID)


def get_children(df, root_guid, props=None):
    """Filtert het dataframe op de subtree onder het opgegeven root-package."""
    if props is None:
        props = output_properties
    select_columns = props + ['tree']
    rename_columns = {'name_y': 'package_name'}

    df_package = df[df.object_type == 'Package'].copy()
    df_nonpackage = df[df.object_type != 'Package'].copy()

    df_package["tree"] = df_package.apply(lambda x: get_parent(x.pdata1, df_package), axis=1)
    df_package['package_id'] = pd.to_numeric(df_package['pdata1'])

    root_row = df_package[df_package.ea_guid.str.contains(root_guid)]
    root_tree = root_row.iloc[0]['tree']

    df_combine = pd.merge(df_nonpackage, df_package, on='package_id', suffixes=('', '_y'))
    return pd.concat([
        df_combine[df_combine.tree.str.endswith(root_tree)].rename(columns=rename_columns)[select_columns],
        df_package[df_package.tree.str.endswith(root_tree)][select_columns],
    ])


def get_df(uri, sql):
    """Voert een SQL-query uit op een SQLite-database en geeft het resultaat terug als DataFrame."""
    connection = sqlite3.connect(uri)
    try:
        df = pd.read_sql(sql, connection)
        return df
    finally:
        connection.close()


def get_df_objectsHierar(uri, root_guid=None):
    """Laadt alle objecten uit de database en filtert optioneel op een root-GUID."""
    df_classes = get_df(uri, sql_classes)

    mask = df_classes["ea_guid"].astype(str).str.contains(root_guid, na=False, regex=False)
    if root_guid and mask.sum() == 1:
        lst_prop = [item for item in output_properties if item not in ['attributes', 'start_connectors', 'end_connectors']]
        return get_children(df_classes, root_guid, props=lst_prop)
    else:
        print(f'Root Guid {root_guid} not found, returning all')
        return df_classes


# ---------------------------------------------------------------------------
# Overgenomen uit util.py
# ---------------------------------------------------------------------------

def verwijder_getallen_en_blanks_vooraan(s):
    """Verwijdert voorloopgetallen en witruimte uit een string."""
    s = str(s)
    return re.sub(r'^[0-9\s]+', '', s)


def addToTree(df, tree, item_ID, child_column, parent_column, tag_column, parent=None):
    """Recursieve hulpfunctie om een dataframe om te zetten naar een boomstructuur."""
    df_item = df[df[child_column] == item_ID]
    if len(df_item) == 0:
        return None
    item = df_item.iloc[0]
    tree.create_node(tag=item[tag_column], identifier=item[child_column], parent=parent, data=item)

    df_children = df[df[parent_column] == item_ID]
    for index, child in df_children.iterrows():
        addToTree(df, tree, child[child_column], child_column, parent_column, tag_column, item_ID)


def DataframeToTree(df, child_column, parent_column, rootID, tag_column=None):
    """Zet een dataframe om naar een boomstructuur (treelib.Tree)."""
    tree = Tree()
    tag_column = 'Name' if not tag_column else tag_column
    addToTree(df, tree, rootID, child_column, parent_column, verwijder_getallen_en_blanks_vooraan(tag_column), parent=None)
    return tree


def exportColumns(df, col_list: list, col_mapping: dict = None):
    """Filtert en hernoemt kolommen voor export; voegt ontbrekende kolommen als leeg toe."""
    df_export = df.copy()
    if col_mapping:
        df_export.drop(
            columns=[col for col in col_mapping.values() if col not in df_export.columns and 'GEMMA' in col],
            inplace=True, errors='ignore',
        )
        df_export = df_export.rename(columns=col_mapping)

    full_cols = [col for col in col_list if col in list(df_export.columns)]
    empty_cols = [col for col in col_list if col not in full_cols]

    df_export = df_export[full_cols]
    for col in empty_cols:
        df_export[col] = ''

    return df_export


# ---------------------------------------------------------------------------
# Standaardwaarden
# ---------------------------------------------------------------------------

DEFAULT_ROOT_GUID = '{D7FD597E-1F40-48df-AFFC-EA3B5B5D3FBF}'  # Root GGM

OBJ_COLUMNS = [
    'GGM-naam', 'GGM-definitie', 'GGM-uml-type', 'GGM-toelichting',
    'GGM-synoniemen', 'GGM-guid', 'GGM-bron', 'domein-iv3', 'domein-dcat',
    'domein-gemma', 'GEMMA-naam', 'GEMMA-definitie', 'GEMMA-toelichting',
    'GEMMA-synoniemen', 'GEMMA-bron', 'GEMMA-URL', 'GEMMA-alternate-name',
    'GEMMA-guid', 'GEMMA-type', 'datum-tijd-export',
]
OBJ_COLUMN_MAPPING = {
    'name': 'GGM-naam',
    'object_type': 'GGM-uml-type',
    'ea_guid': 'GGM-guid',
    'herkomst': 'GGM-bron',
    'note': 'GGM-definitie',
    'toelichting': 'GGM-toelichting',
    'synoniemen': 'GGM-synoniemen',
    'archimate-type': 'GEMMA-type',
    'gemma-guid': 'GEMMA-guid',
}

CON_COLUMNS = [
    'GGM-naam', 'GGM-definitie', 'GGM-uml-type', 'GGM-toelichting',
    'GGM-guid', 'GGM-source-guid', 'GGM-target-guid', 'GEMMA-naam',
    'GEMMA-definitie', 'GEMMA-toelichting', 'GEMMA-type', 'GEMMA-guid',
    'GEMMA-source-guid', 'GEMMA-target-guid', 'datum-tijd-export',
]
CON_COLUMN_MAPPING = {
    'connector_name': 'GGM-naam',
    'connector_type': 'GGM-uml-type',
    'ea_guid_connector': 'GGM-guid',
    'note': 'GGM-definitie',
    'toelichting': 'GGM-toelichting',
    'ea_guid_source': 'GGM-source-guid',
    'ea_guid_target': 'GGM-target-guid',
}


# ---------------------------------------------------------------------------
# Hoofdlogica
# ---------------------------------------------------------------------------

def export_to_gemma(db_uri: str, root_guid: str, output_objects: str, output_relations: str) -> None:
    """Voer de volledige export uit en sla de resultaten op als CSV."""

    now = datetime.now()
    dt_string = now.strftime("%d%m%Y-%H%M%S")

    # Vervang timestamp-placeholders in outputpaden als die er in zitten
    output_objects = output_objects.format(dt=dt_string)
    output_relations = output_relations.format(dt=dt_string)

    # Zorg dat de outputmap bestaat
    os.makedirs(os.path.dirname(os.path.abspath(output_objects)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(output_relations)), exist_ok=True)

    # -----------------------------------------------------------------------
    # Stap 1: Packages inlezen en omzetten naar tree-structuur
    # -----------------------------------------------------------------------
    print("Packages inlezen...")
    df_package = get_df(db_uri, "select * from t_package")
    df_package['Name'] = df_package['Name'].apply(
        lambda x: verwijder_getallen_en_blanks_vooraan(x)
    )

    root_id = df_package[df_package.ea_guid == root_guid]['Package_ID'].values[0]  # noqa: F841
    package_tree = DataframeToTree(df_package, 'Package_ID', 'Parent_ID', 3)

    # -----------------------------------------------------------------------
    # Stap 2: Objecttypes inlezen
    # -----------------------------------------------------------------------
    print("Objecttypes inlezen...")
    df_obj = get_df_objectsHierar(db_uri, root_guid=root_guid)
    df_obj.dropna(subset='name', inplace=True)

    # Packages zijn niet nodig voor de export
    df_obj = df_obj[df_obj.object_type != 'Package']

    # Object properties pivot
    df_objprop = get_df(db_uri, 'select * from t_objectproperties')
    df_objprop = df_objprop.pivot(index="Object_ID", columns="Property", values="Value")
    df_objprop.reset_index(inplace=True)
    df_objprop.drop(columns=['Toelichting'], inplace=True, errors='ignore')

    df_obj = df_obj.merge(
        df_objprop, how='left',
        left_on='object_id', right_on='Object_ID',
        suffixes=('', '_y'),
    )

    # IV3-domein afleiden uit de package-tree
    def getIV3Domein(packageID):
        node = package_tree.get_node(packageID)
        if not node:
            return None
        tag = node.tag
        tag = verwijder_getallen_en_blanks_vooraan(tag)
        if not tag.startswith('Model') and not tag.startswith('Diagram'):
            return tag
        parent = package_tree.parent(packageID)
        if parent is None:
            return None
        return getIV3Domein(parent.identifier)

    df_obj['domein-iv3'] = df_obj.apply(lambda x: getIV3Domein(x['package_id']), axis=1)

    # -----------------------------------------------------------------------
    # Stap 3: Objecten exportklaar maken
    # -----------------------------------------------------------------------
    print("Objectkolommen filteren en hernoemen...")
    df_obj_export = exportColumns(df_obj, OBJ_COLUMNS, OBJ_COLUMN_MAPPING)
    df_obj_export['datum-tijd-export'] = dt_string

    # Correctie voor dubbele toelichting-kolom
    df_obj_export['toelichting_save'] = df_obj_export.apply(
        lambda row: ' '.join([str(x) for x in row[['GGM-toelichting']] if pd.notna(x)]),
        axis=1,
    )
    df_obj_export.drop(columns='GGM-toelichting', inplace=True)
    df_obj_export.rename(columns={'toelichting_save': 'GGM-toelichting'}, inplace=True)

    # -----------------------------------------------------------------------
    # Stap 4: Relaties inlezen
    # -----------------------------------------------------------------------
    print("Relaties inlezen...")
    df_con = get_df(db_uri, sql_connectors).copy()
    df_con = df_con.rename(columns={
        'connector_ea_guid': 'ea_guid_connector',
        'ea_guid_source': 'ea_guid_source_con',
        'ea_guid_dest': 'ea_guid_dest_con',
    })

    df_src = df_obj.copy()[['object_id', 'ea_guid', 'domein-iv3']].rename(columns={
        'object_id': 'start_object_id',
        'ea_guid': 'ea_guid_source',
    })
    df_tgt = df_obj.copy()[['object_id', 'ea_guid']].rename(columns={
        'object_id': 'end_object_id',
        'ea_guid': 'ea_guid_target',
    })

    df_con['start_object_id'] = pd.to_numeric(df_con['start_object_id'], errors='coerce').astype('Int64')
    df_con['end_object_id']   = pd.to_numeric(df_con['end_object_id'],   errors='coerce').astype('Int64')
    df_src['start_object_id'] = pd.to_numeric(df_src['start_object_id'], errors='coerce').astype('Int64')
    df_tgt['end_object_id']   = pd.to_numeric(df_tgt['end_object_id'],   errors='coerce').astype('Int64')

    df_con = df_con.merge(df_src, on='start_object_id', how='inner', validate='many_to_one')
    df_con = df_con.merge(df_tgt, on='end_object_id',   how='inner', validate='many_to_one')
    df_con = df_con.drop_duplicates(subset=['connector_id'])

    # Connector-tags pivot
    df_conprop_raw = get_df(db_uri, 'select * from t_connectortag')
    df_conprop = (
        df_conprop_raw
        .pivot_table(index='ElementID', columns='Property', values='VALUE', aggfunc='first')
        .reset_index()
    )

    df_con['connector_id'] = pd.to_numeric(df_con['connector_id'], errors='coerce').astype('Int64')
    df_conprop['ElementID'] = pd.to_numeric(df_conprop['ElementID'], errors='coerce').astype('Int64')

    df_con = df_con.merge(df_conprop, how='left', left_on='connector_id', right_on='ElementID')
    df_con = df_con.drop(columns=['ElementID'], errors='ignore')

    # -----------------------------------------------------------------------
    # Stap 5: Relaties exportklaar maken
    # -----------------------------------------------------------------------
    print("Relatiekolommen filteren en hernoemen...")
    df_con_export = exportColumns(df_con, CON_COLUMNS, CON_COLUMN_MAPPING)
    df_con_export = df_con_export.loc[:, ~df_con_export.columns.duplicated()].copy()
    df_con_export['datum-tijd-export'] = dt_string

    # NaN opruimen
    df_con_export = df_con_export.fillna('')
    df_con_export = df_con_export.replace(to_replace=r'^\s*nan\s*$', value='', regex=True)

    # -----------------------------------------------------------------------
    # Stap 6: CSV's wegschrijven
    # -----------------------------------------------------------------------
    print(f"Exporteren naar {output_objects}")
    df_obj_export.drop(columns='nr', inplace=True, errors='ignore')
    df_obj_export.index.name = 'nr'
    df_obj_export = df_obj_export.reset_index()
    df_obj_export.to_csv(output_objects, index=False)

    print(f"Exporteren naar {output_relations}")
    df_con_export.drop(columns=['nr', ''], inplace=True, errors='ignore')
    df_con_export.index.name = 'nr'
    df_con_export = df_con_export.reset_index()
    df_con_export.to_csv(output_relations, index=False)

    print("Export geslaagd!")


# ---------------------------------------------------------------------------
# CLI-interface
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Exporteer GGM-objecttypes en -relaties naar CSV voor de GEMMA.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        '--db_uri',
        required=True,
        help='Pad naar de Enterprise Architect SQLite-database (.qea bestand).',
    )
    parser.add_argument(
        '--root_guid',
        default=DEFAULT_ROOT_GUID,
        help=(
            f'GUID van het root-package om te exporteren '
            f'(standaard: root GGM = {DEFAULT_ROOT_GUID}).'
        ),
    )
    parser.add_argument(
        '--output_dir',
        default='./output',
        help='Map waar de CSV-bestanden worden weggeschreven (standaard: ./output).',
    )
    parser.add_argument(
        '--output_objects',
        default=None,
        help=(
            'Volledig pad voor het objecten-CSV-bestand. '
            'Gebruik {dt} als tijdstempel-placeholder. '
            'Overschrijft --output_dir voor dit bestand.'
        ),
    )
    parser.add_argument(
        '--output_relations',
        default=None,
        help=(
            'Volledig pad voor het relaties-CSV-bestand. '
            'Gebruik {dt} als tijdstempel-placeholder. '
            'Overschrijft --output_dir voor dit bestand.'
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Bouw standaard outputpaden als ze niet expliciet zijn opgegeven
    output_objects = args.output_objects or os.path.join(
        args.output_dir, "ggm_export_objects_for_gemma.csv"
    )
    output_relations = args.output_relations or os.path.join(
        args.output_dir, "ggm_export_relations_for_gemma.csv"
    )

    print(f"Database  : {args.db_uri}")
    print(f"Root GUID : {args.root_guid}")
    print(f"Objecten  : {output_objects}")
    print(f"Relaties  : {output_relations}")
    print()

    try:
        export_to_gemma(
            db_uri=args.db_uri,
            root_guid=args.root_guid,
            output_objects=output_objects,
            output_relations=output_relations,
        )
    except Exception as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
