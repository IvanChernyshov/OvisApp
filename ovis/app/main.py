'''GUI predicting the phase transition point of the oil in place'''

#%% Imports

import streamlit as st

from ovis.app.loading import loading_tab
from ovis.app.pstp import pstp_tab
from ovis.app.pstp2 import pstp2_tab
from ovis.app.plots import plots_tab


#%% Functions

def main():
    '''App function'''
    st.title('Ovis: анализ СФП нефти')
    tabs = st.tabs(['Загрузка данных',
                    'Проверка определения ТСФП',
                    'Временные зависимости',
                    'Анализ ТСФП'])
    with tabs[0]:
        loading_tab()
    with tabs[1]:
        pstp_tab()
    with tabs[2]:
        plots_tab()
    with tabs[3]:
        pstp2_tab()
    
    return


#%% Main

if __name__ == '__main__':
    
    main()


