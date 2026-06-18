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
import csv
import io
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

def normalize_eol(val):
    """Normaliseer regeleindes binnen tekstvelden naar LF: verwijder carriage returns
    (CR/CRLF -> LF). De (valide) newlines blijven behouden en worden door pandas correct
    gequote; er wordt NIET door spaties vervangen. Voorkomt de losse CR-tekens die de
    CSV-weergave (o.a. op GitHub) breken."""
    if not isinstance(val, str):
        return val
    return val.replace('\r\n', '\n').replace('\r', '\n')


def validate_csv(path, expected_columns):
    """Valideer een weggeschreven CSV op correctheid en gooi een ValueError bij afwijking:
    - de header is exact de verwachte kolommen (en volgorde);
    - elk record heeft precies evenveel velden (consistente quoting van multiline-velden);
    - er staan geen carriage returns (CR) in het bestand (alleen LF);
    - het bestand is met een strikte CSV-parser uitleesbaar.
    """
    with open(path, newline='', encoding='utf-8') as fh:
        raw = fh.read()
    if '\r' in raw:
        raise ValueError(f"{path}: bevat carriage returns (CR); verwacht uitsluitend LF.")
    try:
        rows = list(csv.reader(io.StringIO(raw)))
    except csv.Error as exc:
        raise ValueError(f"{path}: niet parseerbaar als CSV ({exc}).")
    if not rows:
        raise ValueError(f"{path}: leeg bestand.")
    expected = list(expected_columns)
    if rows[0] != expected:
        raise ValueError(
            f"{path}: header wijkt af.\n  verwacht: {expected}\n  gevonden: {rows[0]}"
        )
    ncol = len(expected)
    bad = [i + 1 for i, row in enumerate(rows) if len(row) != ncol]
    if bad:
        raise ValueError(
            f"{path}: {len(bad)} rij(en) met een afwijkend aantal kolommen "
            f"(eerste op regel {bad[0]}); duidt op kapotte quoting."
        )
    print(f"Validatie OK: {os.path.basename(path)} ({len(rows) - 1} records, {ncol} kolommen)")


DEFAULT_ROOT_GUID = '{D7FD597E-1F40-48df-AFFC-EA3B5B5D3FBF}'  # Root GGM

# Kolommen conform de VNG-spec "GGM-GEMMA data-uitwisseling" (elementen/objecten),
# exacte naam, casing en volgorde. 'nr' wordt bij het wegschrijven vooraan toegevoegd.
OBJ_COLUMNS = [
    'GEMMA-naam', 'GGM-naam', 'GEMMA-guid', 'GGM-guid', 'GEMMA-type',
    'GGM-uml-type', 'GEMMA-definitie', 'GGM-definitie', 'GEMMA-toelichting',
    'GGM-toelichting', 'GEMMA-synoniemen', 'GGM-synoniemen', 'GEMMA-bron',
    'GGM-bron', 'GEMMA-url', 'GEMMA-alternate-name', 'domein-iv3',
    'domein-iv3-guid', 'domein-dcat', 'Datum-tijd-export',
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
    # EA-tag heet 'GEMMA-URL'; spec-kolom is 'GEMMA-url' (kleine letters).
    'GEMMA-URL': 'GEMMA-url',
}

# Kolommen conform de VNG-spec (relaties), exacte naam, casing en volgorde.
# 'nr' wordt bij het wegschrijven vooraan toegevoegd.
CON_COLUMNS = [
    'GEMMA-naam', 'GGM-naam', 'GEMMA-guid', 'GGM-guid', 'GEMMA-type',
    'GGM-uml-type', 'GEMMA-definitie', 'GGM-definitie', 'GEMMA-toelichting',
    'GGM-toelichting', 'GEMMA-source-guid', 'GGM-source-guid',
    'GEMMA-target-guid', 'GGM-target-guid', 'Datum-tijd-export',
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

# Kolommen voor het subdomeinen-bestand (domein-/subdomein-packages). Geen VNG-spec;
# zelfde schone stijl als objects/relations. 'nr' wordt bij het wegschrijven vooraan
# toegevoegd. 'GGM-parent-guid' verwijst naar het bovenliggende (sub)domein.
PKG_COLUMNS = [
    'GGM-naam', 'GGM-guid', 'GGM-definitie', 'GGM-toelichting',
    'GGM-parent-guid', 'GGM-uml-type', 'domein-iv3', 'Datum-tijd-export',
]


# ---------------------------------------------------------------------------
# Hoofdlogica
# ---------------------------------------------------------------------------

def export_to_gemma(
    db_uri: str,
    root_guid: str,
    output_objects: str,
    output_relations: str,
    output_packages: str,
) -> None:
    """Voer de volledige export uit en sla de resultaten op als CSV."""

    now = datetime.now()
    dt_string = now.strftime("%d%m%Y-%H:%M:%S")  # waarde in CSV, conform spec (ddmmyyyy-hh:mm:ss)
    dt_file = now.strftime("%d%m%Y-%H%M%S")       # bestandsnaam-veilige variant (geen dubbele punten)

    # Vervang timestamp-placeholders in outputpaden als die er in zitten
    output_objects = output_objects.format(dt=dt_file)
    output_relations = output_relations.format(dt=dt_file)
    output_packages = output_packages.format(dt=dt_file)

    # Zorg dat de outputmap bestaat
    os.makedirs(os.path.dirname(os.path.abspath(output_objects)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(output_relations)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(output_packages)), exist_ok=True)

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

    # Domein-/subdomein-packages zijn in EA gemarkeerd met stereotype 'Domein'
    # (zo bepaalt ook crunch_uml is_domain). Deze set wordt gebruikt voor zowel het
    # subdomeinen-bestand als de 'domein-iv3'(-guid) bij de objecten, zodat objecten
    # altijd naar een subdomein verwijzen dat ook in het subdomeinen-bestand staat.
    df_domains = get_df(
        db_uri,
        "select ea_guid from t_object where Object_Type = 'Package' and Stereotype = 'Domein'",
    )
    domain_guids = set(df_domains['ea_guid'].dropna())
    domain_pids = set(df_package[df_package['ea_guid'].isin(domain_guids)]['Package_ID'])

    def get_domein_node(package_id):
        """Dichtstbijzijnde voorouder-package (incl. zichzelf) met stereotype 'Domein'."""
        node = package_tree.get_node(package_id)
        while node is not None:
            if node.identifier in domain_pids:
                return node
            node = package_tree.parent(node.identifier)
        return None

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

    # Subdomein (stereotype 'Domein') per object: naam + guid. De naam is al ontdaan
    # van een ordenend cijfer vooraan (zie verwijder_getallen_en_blanks_vooraan in
    # Stap 1) en is identiek aan de GGM-naam in het subdomeinen-bestand.
    domein_nodes = df_obj['package_id'].apply(get_domein_node)
    df_obj['domein-iv3'] = domein_nodes.apply(lambda n: n.tag if n is not None else '')
    df_obj['domein-iv3-guid'] = domein_nodes.apply(lambda n: n.data['ea_guid'] if n is not None else '')

    # -----------------------------------------------------------------------
    # Stap 3: Objecten exportklaar maken
    # -----------------------------------------------------------------------
    print("Objectkolommen filteren en hernoemen...")
    df_obj_export = exportColumns(df_obj, OBJ_COLUMNS, OBJ_COLUMN_MAPPING)
    df_obj_export['Datum-tijd-export'] = dt_string

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
    df_con_export['Datum-tijd-export'] = dt_string

    # NaN opruimen
    df_con_export = df_con_export.fillna('')
    df_con_export = df_con_export.replace(to_replace=r'^\s*nan\s*$', value='', regex=True)

    # -----------------------------------------------------------------------
    # Stap 6: CSV's wegschrijven — exact de spec-kolommen en -volgorde, met een
    # doorlopend 'nr' (0-gebaseerd regelnummer) vooraan. De reindex dwingt de
    # exacte volgorde af en verwijdert eventuele extra (ruis-)kolommen.
    # -----------------------------------------------------------------------
    print(f"Exporteren naar {output_objects}")
    df_obj_export = df_obj_export.loc[:, ~df_obj_export.columns.duplicated()].copy()
    df_obj_export = df_obj_export.fillna('').reset_index(drop=True)
    df_obj_export['nr'] = range(len(df_obj_export))
    df_obj_export = df_obj_export.reindex(columns=['nr'] + OBJ_COLUMNS, fill_value='')
    df_obj_export = df_obj_export.map(normalize_eol)
    df_obj_export.to_csv(output_objects, index=False, lineterminator='\n')
    validate_csv(output_objects, ['nr'] + OBJ_COLUMNS)

    print(f"Exporteren naar {output_relations}")
    df_con_export = df_con_export.loc[:, ~df_con_export.columns.duplicated()].copy()
    df_con_export = df_con_export.fillna('').reset_index(drop=True)
    df_con_export['nr'] = range(len(df_con_export))
    df_con_export = df_con_export.reindex(columns=['nr'] + CON_COLUMNS, fill_value='')
    df_con_export = df_con_export.map(normalize_eol)
    df_con_export.to_csv(output_relations, index=False, lineterminator='\n')
    validate_csv(output_relations, ['nr'] + CON_COLUMNS)

    # -----------------------------------------------------------------------
    # Stap 7: Subdomeinen wegschrijven — alleen de inhoudelijke domein-/subdomein-
    # packages onder de root. De technische 'Diagram'- en 'Model ...'-packages
    # worden overgeslagen. GGM-parent-guid verwijst naar het bovenliggende
    # (sub)domein (leeg voor een top-domein); domein-iv3 is het top-level domein.
    # -----------------------------------------------------------------------
    print(f"Exporteren naar {output_packages}")

    # Domein-/subdomein-packages = de in Stap 1 bepaalde 'Domein'-packages (domain_guids).
    # Technische packages (Model ..., Diagram, datatypes, enumeratiesoorten, klassegroepen)
    # hebben dat stereotype niet en vallen dus vanzelf af.
    def in_domains(node):
        return node is not None and node.data is not None and node.data['ea_guid'] in domain_guids

    def getTopDomein(packageID):
        # Hoogste 'Domein'-voorouder (het IV3-domein) waaronder dit (sub)domein valt.
        node = package_tree.get_node(packageID)
        if node is None:
            return ''
        parent = package_tree.parent(packageID)
        while in_domains(parent):
            node = parent
            parent = package_tree.parent(node.identifier)
        return node.tag

    pkg_records = []
    for node in package_tree.all_nodes():
        if not in_domains(node):
            continue
        data = node.data
        parent = package_tree.parent(node.identifier)
        parent_guid = parent.data['ea_guid'] if in_domains(parent) else ''
        pkg_records.append({
            'GGM-naam': node.tag,
            'GGM-guid': data['ea_guid'],
            'GGM-definitie': data['Notes'] if 'Notes' in data else '',
            'GGM-toelichting': '',
            'GGM-parent-guid': parent_guid,
            'GGM-uml-type': 'Package',
            'domein-iv3': getTopDomein(node.identifier),
            'Datum-tijd-export': dt_string,
        })

    df_pkg_export = pd.DataFrame(pkg_records, columns=PKG_COLUMNS).fillna('')
    if not df_pkg_export.empty:
        df_pkg_export = df_pkg_export.sort_values(['domein-iv3', 'GGM-naam'])
    df_pkg_export = df_pkg_export.reset_index(drop=True)
    df_pkg_export['nr'] = range(len(df_pkg_export))
    df_pkg_export = df_pkg_export.reindex(columns=['nr'] + PKG_COLUMNS, fill_value='')
    df_pkg_export = df_pkg_export.map(normalize_eol)
    df_pkg_export.to_csv(output_packages, index=False, lineterminator='\n')
    validate_csv(output_packages, ['nr'] + PKG_COLUMNS)

    print("Export geslaagd!")


# ---------------------------------------------------------------------------
# CLI-interface
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Exporteer GGM-objecttypes, -relaties en -subdomeinen naar CSV voor de GEMMA.",
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
    parser.add_argument(
        '--output_packages',
        default=None,
        help=(
            'Volledig pad voor het subdomeinen-CSV-bestand (domein-/subdomein-packages). '
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
    output_packages = args.output_packages or os.path.join(
        args.output_dir, "ggm_export_subdomains_for_gemma.csv"
    )

    print(f"Database    : {args.db_uri}")
    print(f"Root GUID   : {args.root_guid}")
    print(f"Objecten    : {output_objects}")
    print(f"Relaties    : {output_relations}")
    print(f"Subdomeinen : {output_packages}")
    print()

    try:
        export_to_gemma(
            db_uri=args.db_uri,
            root_guid=args.root_guid,
            output_objects=output_objects,
            output_relations=output_relations,
            output_packages=output_packages,
        )
    except Exception as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
