'''Tab for visualising PSTP fitting'''

#%% Imports

import streamlit as st

from ovis.pstp import prepare_fv, find_intersection_point


#%% Functions

def pstp_tab():
    '''Contains functionality for PSTP search'''
    if not hasattr(st.session_state, 'df'):
        st.error('Загрузите данные на первой вкладке')
        return
    nrow = st.selectbox('Выберите номер измерения',
                        list(st.session_state.df.index))
    # check for negative values and prepare for plotting
    x, y = prepare_fv(st.session_state.df, nrow)
    count = sum([v <= 0 for v in y])
    if count:
        text = f'Обнаружено {count} предсказанных отрицательных значений вязкости, минимум = {min(y):.3f}'
        st.warning(text)
    y = [v if v > 0 else 0.1 for v in y]
    # plot
    fig, intersection_point = find_intersection_point(x, y)
    if fig:
        st.plotly_chart(fig)
        st.text(f'ТСФП = {intersection_point}')
    
    return


#%% Misc

__all__ = ['pstp_tab']


