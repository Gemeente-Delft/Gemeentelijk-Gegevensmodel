"""
Haal entiteiten uit database
Lees de benodigde data uit de oude en de nieuwe database. Classes, attributen en Connectors staan in afzonderlijke databases. Deze worden allereerst afzonderlijk ingelezen in ieder een eigen dataframe. Waarna de attributen, de uitgaande connectors en de inkomende connectors als JSON-velden aan de dataframe met classes worden toegevoegd. Het resultaat van deze stap is:

df_classes_new: een dataframe met daarin alle classes, enumeraties en packages uit de nieuwe database
df_classes_old: een dataframe met daarin alle classes, enumeraties en packages uit de oude database
In beide dataframes staan de properties van de classes, aangevuld met de volgende kolommen:

attributes: een JSON met daarin alle attributen van de class
start_connectors: een JSON met daarin alle uitgaande relaties
end_connectors: een JSON met daarin alle inkomende relaties
"""


import os
import pandas as pd
import json
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import reflection



object_properties = ['object_id',
 'object_type', 'stereotype',
 'name',
 'alias',
 'author',
 'version',
 'objectnote',
 'pdata1',
 'ea_guid',
 'parentid',
 'package_id',
 'modifieddate',
 'note']
output_properties = ['object_id','object_type','stereotype',
 'name',
 'alias',
 'author',
 'version',
 'objectnote',
 'ea_guid',
 'modifieddate',
 'attributes',
 'start_connectors',
 'end_connectors', 'note', 'package_id']
#attribute_properties = ['attribute_Name', 'attribute_Type', 'attribute_Length', 'attribute_Precision', 'attribute_Scale', 'attribute_ea_guid']
attribute_properties = ['attribute_name', 'attribute_type', 'attribute_style', 'attribute_ea_guid']
#connector_properties = ['Connector_Name','Connector_Type','Start_object_id','End_object_id','Connector_SourceCard','Connector_DestCard','Connector_SourceRole','Connector_DestRole','Top_Start_Label','Top_Mid_Label','Top_End_Label','Connector_ea_guid']
connector_properties = ['connector_id',
 'connector_name',
 'connector_type',
 'connector_sourcecard',
 'connector_destcard',
 'connector_sourcerole',
 'connector_destrole',
 'top_start_label',
 'top_mid_label',
 'top_end_label',
 'connector_ea_guid',
 'start_object_name',
 'end_object_name',
 'start_object_id',
 'end_object_id',
 'note']

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
Where o.Object_Type IN (\'Package\', \'Class\', \'Enumeration\', \'DataType\')"""

sql_attributes = """select 
a.object_id as object_id,
a.Name as attribute_name,
a.Type as attribute_type,
a.Style as attribute_style,
a.Length as attribute_length,
a.Precision as attribute_precision,
a.Scale as attribute_scale,
a.ea_guid as attribute_ea_guid 
FROM t_attribute a"""

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
Where c.Connector_Type IN (\'Association\', \'Generalization\')
 AND so.object_id = c.Start_object_id
 AND eo.object_id = c.End_object_id"""


def cleanNullTerms(json_str):
    lst = json.loads(json_str)
    return list(filter(None, (dict(filter(lambda elem: elem[1] == elem[1] and not elem[1] == 'null', sub.items())) for sub in lst)))

def removeEmptyRecords(json_str):
    df = pd.DataFrame.from_records(json_str)
    df.dropna(how='all', inplace=True)
    return df.to_json(orient='records')

def merge_into_json(main_df, df_detail, merge_properties, on_left, on_right, column_name):
    
    df = pd.merge(main_df, df_detail, how='left', left_on=on_left, right_on=on_right)
    
    # Group records so that all attributes are put in a JSON colum
    df = df.groupby(object_properties, dropna=False)[merge_properties].apply(lambda x: x.to_json(orient='records')).reset_index().rename(columns={0: column_name})
    df[column_name] = df.apply(lambda x: cleanNullTerms(x[column_name]), axis=1)
    #df[column_name] = df.apply(lambda x: removeEmptyRecords(x[column_name]), axis=1)
    
    return df
    

 

# functie om in een kolom tree alle parents van een bepaald object te zetten. Steeds met een streepje er tussen, zoals: 282-281-268-44-43. Waarbij de laatste te hoogst gelegen parenmt is 
def get_parent(package_ID, df_objecten):
    pID = str(package_ID)
    df_package = df_objecten[df_objecten.pdata1 == pID]
    if not df_package.empty:
        value = str(df_package['package_id'].iloc[0])
        return str(pID + '-' + get_parent(value, df_objecten))
    else:
        return str(pID)

def get_children(df, root_guid, props=output_properties):
    select_columns = props + ['tree']
    rename_columns = {'name_y':'package_name'}

    df_package = df[df.object_type == 'Package'].copy()
    df_nonpackage = df[df.object_type != 'Package'].copy()

    # Set tree column 
    df_package["tree"] = df_package.apply(lambda x: get_parent(x.pdata1, df_package), axis=1)
    df_package['package_id'] = pd.to_numeric(df_package['pdata1'])
    #df_package['Package_Name'] = ''
    
    root_row = df_package[df_package.ea_guid.str.contains(root_guid)]
    root_tree = root_row.iloc[0]['tree']  
    
    df_combine = pd.merge(df_nonpackage, df_package, on='package_id', suffixes=('', '_y'))
    return pd.concat([df_combine[df_combine.tree.str.endswith(root_tree)].rename(columns=rename_columns)[select_columns], df_package[df_package.tree.str.endswith(root_tree)][select_columns]])



# Generieke functie om uit een access database resultaten van query als dataframe terug te geven 
def get_df(uri, sql):
    engine = create_engine(uri)
    connection = engine.connect()
    try: 
        df = pd.read_sql(sql,connection)
        return df
    finally:
        connection.close()
 
# Generieke functie om geheel voorbereide gegevens uit database te halen
def get_df_complete(uri, root_guid=None):
    df_classes = get_df(uri, sql_classes)
    df_attributes = get_df(uri, sql_attributes)
    df_connectors = get_df(uri, sql_connectors).dropna(subset=['connector_ea_guid'])
    df_classes = merge_into_json(df_classes.copy(), df_attributes, attribute_properties, 'object_id', 'attribute_object_id', 'attributes')
    df_classes['attributes'] = merge_into_json(df_classes.copy(), df_attributes, attribute_properties, 'object_id', 'attribute_object_id', 'attributes')['attributes']
    df_classes['start_connectors'] = merge_into_json(df_classes.copy(), df_connectors, connector_properties, 'object_id', 'start_object_id', 'start_connectors')['start_connectors']
    df_classes['end_connectors'] = merge_into_json(df_classes.copy(), df_connectors, connector_properties, 'object_id', 'end_object_id', 'end_connectors')['end_connectors']
    
    df_classes['attributes'] = df_classes.apply(lambda x: [item for item in x['attributes'] if not item['attribute_name'] is None], axis=1)
    df_classes['start_connectors'] = df_classes.apply(lambda x: [item for item in x['start_connectors'] if not item['connector_id'] is None], axis=1)
    df_classes['end_connectors'] = df_classes.apply(lambda x: [item for item in x['end_connectors'] if not item['connector_id'] is None], axis=1)
    
    if root_guid and df_classes[df_classes.ea_guid.str.contains(root_guid)].count()[0] == 1:
        return get_children(df_classes, root_guid)
    else:
        return df_classes
    
    

def get_df_objectsHierar(uri, root_guid=None):
    df_classes = get_df(uri, sql_classes)
    
    if root_guid and df_classes[df_classes.ea_guid.str.contains(root_guid)].count()[0] == 1:
        lst_prop = [item for item in output_properties if item not in ['attributes','start_connectors','end_connectors']]
        return get_children(df_classes, root_guid, props=lst_prop)
    else:
        print(f'Root Guid {root_guid} not found returning all') 
        return df_classes
    
    