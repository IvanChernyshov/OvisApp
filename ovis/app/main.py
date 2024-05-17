'''GUI predicting the phase transition point of the oil in place'''

#%% Imports

import streamlit as st

from ovis.app.loading import loading_tab
from ovis.app.pstp import pstp_tab
from ovis.app.plots import plots_tab


#%% Functions

def main():
    '''App function'''
    st.title('Ovis: анализ СФП нефти')
    tab1, tab2, tab3 = st.tabs(['Загрузка данных',
                                'Проверка определения ТСФП',
                                'Временные зависимости'])
    with tab1:
        loading_tab()
    with tab2:
        pstp_tab()
    with tab3:
        plots_tab()
    
    return


#%% Main

if __name__ == '__main__':
    
    main()


