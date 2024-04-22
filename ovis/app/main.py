'''GUI predicting the phase transition point of the oil in place'''

#%% Imports

import streamlit as st

from ovis.app.loading import loading_tab
from ovis.app.analysis import analysis_tab
from ovis.app.settings import settings_tab


#%% Functions

def main():
    '''App function'''
    df, cols = None, None
    tab1, tab2, tab3 = st.tabs(['Загрузка', 'Анализ', 'Настройки'])
    with tab1:
        df, cols = loading_tab()
    with tab2:
        analysis_tab(df, cols)
    with tab3:
        settings_tab()
    
    return


#%% Main

if __name__ == '__main__':
    
    main()


