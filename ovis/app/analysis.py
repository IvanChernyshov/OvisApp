'''GUI predicting the phase transition point of the oil in place'''

#%% Imports

import streamlit as st


#%% Functions

def analysis_tab(df, cols):
    '''Runs exploratory data analysis on the input data'''
    if df is None:
        st.error('Загрузите данные на первой вкладке')
        return
    gvar = st.selectbox('Выберите способ группировки данных',
                        ['Скважина', 'Ярус, горизонт'])
    gcol = cols[gvar]
    df[gcol] = df[gcol].astype('str')
    groups = sorted(df.loc[:,gcol].unique())
    group = st.selectbox('Выберите группу данных', groups)
    sub = df.loc[df[gvar] == group]
    st.scatter_chart(sub, y = cols['Вязкость нефти в условиях пласта'], x = cols['Время'])
    
    return


#%% Misc

__all__ = ['analysis_tab']


