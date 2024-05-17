'''Tab for loading data'''

#%% Imports

import webbrowser

import pandas as pd

import streamlit as st

from ovis.misc import get_docs_path
from ovis.models import viscUniModel
from ovis.pstp import prepare_fv, find_intersection_point


#%% Functions

def loading_tab():
    '''Contains functionality for loading data and setting names of
    important columns'''
    if st.button('Как пользоваться приложением'):
        path = get_docs_path()
        webbrowser.open(path, new = 2)
    # loading data
    inpf = st.file_uploader('Выберите файл')
    if inpf is None:
        return None
    st.session_state.df = pd.read_csv(inpf)
    # predict viscosity
    if st.button('Рассчитать ТСФП'):
        df = st.session_state.df.copy()
        predicted_viscosity = viscUniModel.predict(df)
        df.insert(0, 'Вязкость, модель №1', predicted_viscosity)
        # compute pstp
        progress_text = 'Рассчитываем ТСФП ...'
        pbar = st.progress(0, text = progress_text)
        pstps = []
        for i, idx in enumerate(df.index):
            x, y = prepare_fv(df, idx)
            y = [v if v > 0 else 0.1 for v in y]
            pstps.append(find_intersection_point(x, y)[1])
            pbar.progress(i/len(df), text = progress_text)
        df.insert(1, 'ТСФП, модель №1', pstps)
        st.session_state.df = df
        pbar.empty()
    # show dataframe
    st.dataframe(st.session_state.df)
    
    return 


#%% Misc

__all__ = ['loading_tab']


