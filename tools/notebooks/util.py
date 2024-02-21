from treelib import Node, Tree
import re

# Script voor het schoonmaken van de Strings van de packages
def verwijder_getallen_en_blanks_vooraan(s):
    s = str(s)
    return re.sub(r'^[0-9\s]+', '', s)

def addToTree(df, tree, item_ID, child_column, parent_column, tag_column, parent=None):
    '''
    Recursive method to extract items from a dataframe into tree structure. To be used from DataframeToTree. 
    '''
    df_item = df[df[child_column] == item_ID]
    if len(df_item) == 0:
        return None
    item = df_item.iloc[0]
    tree.create_node(tag=item[tag_column], identifier=item[child_column], parent=parent, data=item)
    
    df_children = df[df[parent_column] == item_ID]
    for index, child in df_children.iterrows():
        addToTree(df, tree, child[child_column], child_column, parent_column, tag_column, item_ID)
    s = 1



def exportColumns(df, col_list:list, col_mapping:dict=None):
    '''
    Exports all columns from dataframe that are present in col_list and adds the ones that are not present. Also renames columns from col_mapping
    '''    
    df_export = df.copy()
    if col_mapping:
        df_export.drop(columns=[col for col in col_mapping.values() if col not in df_export.columns and 'GEMMA' in col], inplace=True, errors='ignore')
        df_export = df_export.rename(columns=col_mapping)

    #filter benodigde kolommen en voeg niet bestaande toe
    full_cols = [col for col in col_list if col in list(df_export.columns)]
    empty_cols = [col for col in col_list if col not in full_cols]

    df_export = df_export[full_cols]
    for col in empty_cols:
        df_export[col] = ''
        
    return df_export

def DataframeToTree(df, child_column, parent_column, rootID, tag_column=None):
    '''
    Extracts a tree structure from a dataframe
    '''
    tree = Tree()
    tag_column = 'Name' if not tag_column else tag_column
    addToTree(df, tree, rootID, child_column, parent_column, verwijder_getallen_en_blanks_vooraan(tag_column), parent=None)
    return tree


def combineerColumns(df, to_col, col_list:list):
    '''
    Combineert de waarden uit een lijst kolommen en plaatst ze in een nieuwe kolom
    '''    
    for col in reversed(col_list):
        df[to_col] = df[col]
    df.drop(columns=[col for col in col_list if col != to_col])
    return df
    
def combineerColumnsOnTerm(df, term):    
    columns = [col for col in list(df.columns) if term in col]
    return combineerColumns(df, term, columns)