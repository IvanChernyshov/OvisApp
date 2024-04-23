'''Tab for viewing settings'''

#%% Imports

import webbrowser

import streamlit as st

from ovis.misc import get_docs_path


#%% Functions

def settings_tab() -> None:
    '''Settings tab'''
    if st.button('Документация'):
        path = get_docs_path()
        webbrowser.open(path, new = 2)
    
    return



#%% Misc

__all__ = ['settings_tab']


