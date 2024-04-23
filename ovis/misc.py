'''Some useful functions'''

#%% Imports

import os, pkgutil

from ovis.parameters import get_app_dir


#%% Functions

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



#%% Misc

__all__ = ['get_docs_path']


