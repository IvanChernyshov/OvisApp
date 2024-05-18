'''Tab for loading data'''

#%% Imports

import webbrowser

import streamlit as st

from ovis.misc import get_docs_path
from ovis.models import viscUniModel, viscAccModel
from ovis.pstp import prepare_fv, get_intersection_point
from ovis.misc import read_csv


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
    st.session_state.df = read_csv(inpf)
    # predict
    if st.button('Рассчитать вязкость и ТСФП'):
        # viscosity
        df = st.session_state.df.copy()
        predicted_viscosity = viscUniModel.predict(df)
        if 'Вязкость, универсальная модель' not in df.columns:
            df.insert(0, 'Вязкость, универсальная модель', predicted_viscosity)
        else:
            df.loc[:,'Вязкость, универсальная модель'] = predicted_viscosity
        predicted_viscosity = viscAccModel.predict(df)
        if 'Вязкость, точная модель' not in df.columns:
            df.insert(0, 'Вязкость, точная модель', predicted_viscosity)
        else:
            df.loc[:,'Вязкость, точная модель'] = predicted_viscosity
        # pstp
        progress_text = 'Рассчитываем ТСФП ...'
        pbar = st.progress(0, text = progress_text)
        pstps = []
        for i, idx in enumerate(df.index):
            x, y = prepare_fv(df, idx, viscAccModel)
            y = [v if v > 0 else 0.1 for v in y]
            pstps.append(get_intersection_point(x, y)[0])
            pbar.progress(i/len(df), text = progress_text)
        if 'ТСФП, точная модель' not in df.columns:
            df.insert(0, 'ТСФП, точная модель', pstps)
        else:
            df.loc[:,'ТСФП, точная модель'] = pstps
        st.session_state.df = df
        pbar.empty()
    # show dataframe
    st.dataframe(st.session_state.df)
    
    return 


#%% Misc

__all__ = ['loading_tab']


