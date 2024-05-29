'''Tab for visualising PSTP fitting'''

#%% Imports

import streamlit as st

from ovis.pstp import prepare_fv, get_intersection_point, plot_intersection_point
from ovis.models import viscUniModel, viscAccModel


#%% Functions

def pstp_tab():
    '''Contains functionality for PSTP search'''
    if not hasattr(st.session_state, 'df'):
        st.error('Загрузите данные на первой вкладке')
        return
    models = {'Точная модель': viscAccModel,
              'Универсальная модель': viscUniModel}
    model_name = st.selectbox(label = 'Выберите модель', key = 'pstp_model',
                              options = ['Точная модель', 'Универсальная модель'])
    model = models[model_name]
    nrow = st.selectbox('Выберите номер измерения',
                        [None] + list(st.session_state.df.index))
    # check for negative values and prepare for plotting
    if nrow is None:
        return
    x, y = prepare_fv(st.session_state.df, nrow, model)
    count = sum([v <= 0 for v in y])
    if count:
        text = f'Обнаружено {count} предсказанных отрицательных значений вязкости, минимум = {min(y):.3f}'
        st.warning(text)
    y = [v if v > 0 else 0.1 for v in y]
    # plot
    T_pst, mu_pst = get_intersection_point(x, y)
    st.plotly_chart(plot_intersection_point(x, y))
    if T_pst is not None:
        st.text(f'ТСФП = {T_pst:.1f} °C при μ = {mu_pst:.2f} мПа·с')
    else:
        st.text('Approximation failed')
    
    return


#%% Misc

__all__ = ['pstp_tab']


