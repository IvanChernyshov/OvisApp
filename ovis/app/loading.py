'''Tab for loading data'''

#%% Imports

import pandas as pd

import streamlit as st


#%% Functions

def loading_tab():
    '''Contains functionality for loading data and setting names of
    important columns'''
    # loading data
    inpf = st.file_uploader('Выберите файл')
    if inpf is None:
        return None, None
    df = pd.read_csv(inpf)
    # setting sidebar
    st.header('Выберите ключевые столбцы:')
    cols = {
        'Скважина': st.selectbox('Номер скважины', df.columns),
        'Ярус, горизонт': st.selectbox('Ярус, горизонт', df.columns),
        'Вязкость нефти в условиях пласта': st.selectbox('Вязкость нефти в условиях пласта', df.columns),
        'Вязкость дегазированной нефти': st.selectbox('Вязкость дегазированной нефти', df.columns),
        'Время': st.selectbox('Время', df.columns)
    }
    st.header('Датасет')
    st.write(df)
    
    return df, cols


#%% Misc

__all__ = ['loading_tab']


