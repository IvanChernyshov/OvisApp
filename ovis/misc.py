'''Some useful functions'''

#%% Imports

import os, json, pkgutil

import pandas as pd


#%% Functions

def get_app_dir() -> str:
    '''Returns path to the app's directory in user's home dir'''
    path = os.path.join(os.path.expanduser("~"), '.ovis')
    if not os.path.exists(path):
        os.mkdir(path)
    
    return path


def get_docs_path() -> str:
    '''
    Returns path to the PDF-formatted documentation in app's directory,
    and extracts it from the package data if it's not there
    '''
    path = os.path.join(get_app_dir(), 'ovis.pdf')
    if True: # not os.path.exists(path) or os.path.getsize(path) < 1000:
        pdf = pkgutil.get_data('ovis', 'data/ovis.pdf')
        with open(path, 'wb') as outf:
            outf.write(pdf)
    
    return path


def get_col_types() -> dict[str, str]:
    '''Returns dtypes for input CSV file'''
    content = pkgutil.get_data('ovis', 'data/column_types.json')
    dtypes = json.loads(content)
    
    return dtypes


def read_csv(inpf):
    '''Reads CSV with oil data'''
    df = pd.read_csv(inpf, dtype = get_col_types(), index_col = False)
    if 'unnamed' in df.columns[0].lower():
        df = df.iloc[:,1:]
    
    return df



#%% Misc

__all__ = ['read_csv', 'get_app_dir', 'get_docs_path', 'get_col_types']


