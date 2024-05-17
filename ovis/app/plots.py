'''Tab for visualization of time dependences'''

#%% Imports

import streamlit as st

import plotly.graph_objects as go


#%% Functions

def plots_tab():
    '''Contains functionality for vizualization of time dependences'''
    # loading data
    if not hasattr(st.session_state, 'df'):
        st.error('Загрузите данные на первой вкладке')
        return
    df = st.session_state.df
    # select plotting parameters
    cols = list(df.columns)
    col = 'Год исследования'
    lab_x = st.selectbox(label = 'Выберите ось Ox', options = cols,
                         index = cols.index(col) if col in cols else None)
    col = 'Вязкость нефти в условиях пласта, мПа·с'
    lab_y = st.selectbox(label = 'Выберите ось Oy', options = cols,
                         index = cols.index(col) if col in cols else None)
    # get data for plotting
    data = df.loc[:,[lab_x, lab_y]].dropna()
    # select labs for point colors
    default_labs = ['Месторождение', 'Ярус, горизонт']
    default_labs = [l for l in default_labs if l in cols]
    labs = st.multiselect('Выберите колонки для группирования данных',
                          options = cols, default = default_labs)
    if labs:
        lab_values = df[labs].apply(lambda row: '_'.join(row.values.astype(str)), axis = 1)
        data['labs'] = lab_values
        data['labs'] = data['labs'].astype(str)
        options = list(sorted(set(data['labs'])))
        selected = st.multiselect('Выберите группы данных для построения',
                                  options = options,
                                  default = options[:1])
        data = data.loc[data['labs'].isin(selected)]
    # plot
    fig = go.Figure()
    fig.update_layout(xaxis_title = lab_x, yaxis_title = lab_y,
                      autosize = False, width = 700, height = 500,
                      plot_bgcolor = 'white')
    fig.update_xaxes(mirror = True,
                     ticks = 'outside',
                     showline = True,
                     linecolor = 'black',
                     gridcolor = 'lightgrey')
    fig.update_yaxes(mirror = True,
                     ticks = 'outside',
                     showline = True,
                     linecolor = 'black',
                     gridcolor = 'lightgrey')
    fig.add_trace(go.Scatter(x = data[lab_x], y = data[lab_y], mode = 'markers'))
    # show figure
    st.plotly_chart(fig)
    
    return


#%% Misc

__all__ = ['plots_tab']


