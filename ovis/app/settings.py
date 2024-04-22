'''Tab for viewing settings'''

#%% Imports

import os, webbrowser

import streamlit as st

import ovis


#%% Functions

def settings_tab() -> None:
    '''Settings tab'''
    if st.button('Документация'):
        path = os.path.join(os.path.dirname(ovis.__file__), 'docs', 'index.html')
        webbrowser.open(path, new = 2)
    
    return



#%% Misc

__all__ = ['settings_tab']


