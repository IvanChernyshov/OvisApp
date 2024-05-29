'''Tab for visualising PSTP fitting with dependence on numeric parameters'''

#%% Imports

import pandas as pd

import streamlit as st

from ovis.pstp import prepare_fv, get_intersection_point, plot_intersection_point
from ovis.models import viscUniModel, viscAccModel


#%% Functions

def pstp2_tab():
    '''Contains functionality for PSTP search'''
    # select model
    models = {'Точная модель': viscAccModel,
              'Универсальная модель': viscUniModel}
    model_name = st.selectbox(label = 'Выберите модель', key = 'pstp2_model',
                              options = ['Точная модель', 'Универсальная модель'])
    model = models[model_name]
    # set numeric parameters
    col1, col2 = st.columns(2)
    columns = {
        'Давление пласта, МПа': {
            'min_value': 0.0, 'max_value': 50.0,
            'value': 0.0, 'step': 0.1,
            'format': '%f'
        },
        'Дегазированная нефть при 20 °С плотность, кг/м3': {
            'min_value': 0.0, 'max_value': 50.0,
            'value': 4.05, 'step': 0.01,
            'format': '%f'
        },
        'Дегазированная нефть при 20 °С кинематическая вязкость, мм2/с': {
            'min_value': 0.0, 'max_value': 20000.0,
            'value': 50.0, 'step': 0.1,
            'format': '%f'
        },
        'Массовое содержание, % серы': {
            'min_value': 0.0, 'max_value': 20.0,
            'value': 3.0, 'step': 0.01,
            'format': '%f'
        },
        'Массовое содержание, % асфальтенов': {
            'min_value': 0.0, 'max_value': 50.0,
            'value': 5.0, 'step': 0.01,
            'format': '%f'
        },
        'Массовое содержание, % смол': {
            'min_value': 0.0, 'max_value': 50.0,
            'value': 12.0, 'step': 0.01,
            'format': '%f'
        },
        'Массовое содержание, % парафинов': {
            'min_value': 0.0, 'max_value': 50.0,
            'value': 3.0, 'step': 0.01,
            'format': '%f'
        }
    }
    data = {}
    with col1:
        for colname in ['Давление пласта, МПа',
                        'Дегазированная нефть при 20 °С плотность, кг/м3',
                        'Дегазированная нефть при 20 °С кинематическая вязкость, мм2/с']:
            data[colname] = st.number_input(label = colname, **columns[colname])
    with col2:
        for colname in ['Массовое содержание, % серы',
                        'Массовое содержание, % асфальтенов',
                        'Массовое содержание, % смол',
                        'Массовое содержание, % парафинов']:
            data[colname] = st.number_input(label = colname, **columns[colname])
    # check for negative values and prepare for plotting
    df = pd.DataFrame(data, index = [0])
    x, y = prepare_fv(df, 0, model)
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

__all__ = ['pstp2_tab']


