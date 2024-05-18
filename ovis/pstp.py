'''Functionality to analyze mu(T) dependence and to determine
a phase structural transition point'''

#%% Imports

import pandas as pd
import numpy as np
from scipy.optimize import fsolve
from sklearn.metrics import r2_score

import plotly.graph_objects as go


#%% Functions

def prepare_fv(df, nrow, model):
    '''Prepares mu(temp) ~ y(x) for fitting two exponents'''
    # predict mu
    temp_range = [i for i in range(6, 29, 1)]
    row = df.loc[[nrow], :]
    fvs = pd.DataFrame(np.repeat(row.values, len(temp_range), axis = 0))
    fvs.columns = df.columns
    fvs['Температура пласта, °С'] = temp_range
    fvs = fvs.astype(dtype = df.dtypes)
    predicted_viscosity = model.predict(fvs)
    x, y = np.array(temp_range), np.array(predicted_viscosity)
    
    return x, y


def exponential(x, a, b):
    return a * np.exp(b * x)


def fit_exponential(x, y):
    b, log_a = np.linalg.lstsq(np.c_[x, np.ones_like(x)],
                               np.log(y),
                               rcond=None)[0]
    a = np.exp(log_a)

    return [a, b]


def get_intersection_point(x, y):
    '''Get parameters of intersection of two exponents for mu(T)'''
    # find fitting parameters
    popt1 = fit_exponential(x[:15], y[:15])
    popt2 = fit_exponential(x[14:], y[14:])
    error1 = r2_score(y[:15], exponential(x[:15], *popt1))
    error2 = r2_score(y[14:], exponential(x[14:], *popt2))
    accepted_total_error = (error1 > 0.8) & (error2 > 0.8)
    
    # find intersection
    if accepted_total_error:
        
        def equations(variables):
            x0, y0 = variables
            eq1 = exponential(x0, *popt1) - y0
            eq2 = exponential(x0, *popt2) - y0
            return [eq1, eq2]

        T_pst, mu_pst = fsolve(equations, (20, 200))
    else:
        T_pst, mu_pst = None, None
    
    return T_pst, mu_pst


def plot_intersection_point(x, y):
    
    popt1 = fit_exponential(x[:15], y[:15])
    popt2 = fit_exponential(x[14:], y[14:])
    error1 = r2_score(y[:15], exponential(x[:15], *popt1))
    error2 = r2_score(y[14:], exponential(x[14:], *popt2))

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x[:15],
                             y=y[:15],
                             mode='markers',
                             name='Измерения от 6°C до 20°C',
                             marker=dict(color='#F0A58F',
                                         size=8,
                                         line=dict(width=1,
                                                   color='DarkSlateGrey'))))

    fig.add_trace(go.Scatter(x=x[14:],
                             y=y[14:],
                             mode='markers',
                             name='Измерения от 20°C до 28°C',
                             marker=dict(color='#AF4BCE',
                                         size=8,
                                         line=dict(width=1,
                                                   color='DarkSlateGrey'))))

    fig.add_trace(go.Scatter(x=x[:20],
                             y=exponential(x[:20], *popt1),
                             mode='lines',
                             line=dict(dash='dash',
                                       color='#F0A58F'),
                             name=f'{round(popt1[0], 2)} * exp({round(popt1[1], 3)} * x) | R^2 = {round(error1, 3)}'))

    fig.add_trace(go.Scatter(x=x[9:],
                             y=exponential(x[9:], *popt2),
                             mode='lines',
                             line=dict(dash='dash',
                                       color='#AF4BCE'),
                             name=f'{round(popt2[0], 2)} * exp({round(popt2[1], 3)} * x) | R^2 = {round(error2, 3)}'))

    fig.update_layout(xaxis_title='Температура, °C',
                      yaxis_title='Вязкость пластовой нефти, мПа⋅с',
                      autosize=False,
                      width=900,
                      height=500,
                      plot_bgcolor='white')

    fig.update_xaxes(mirror=True,
                     ticks='outside',
                     showline=True,
                     linecolor='black',
                     gridcolor='lightgrey')

    fig.update_yaxes(mirror=True,
                     ticks='outside',
                     showline=True,
                     linecolor='black',
                     gridcolor='lightgrey')

    accepted_total_error = (error1 > 0.8) & (error2 > 0.8)
    if accepted_total_error:
        def equations(variables):
            x0, y0 = variables
            eq1 = exponential(x0, *popt1) - y0
            eq2 = exponential(x0, *popt2) - y0
            return [eq1, eq2]

        intersection_point = fsolve(equations, (20, 200))

        fig.add_trace(go.Scatter(x=[intersection_point[0], intersection_point[0]],
                                 y=[intersection_point[1], np.max(y) / 2],
                                 mode='lines',
                                 line=dict(color='black',
                                           dash='dash',
                                           width=1.25),
                                 showlegend=False))

        label = f'ТСФП = {round(intersection_point[0], 3)} °С'

        fig.add_annotation(x=intersection_point[0],
                           y=np.max(y) / 2,
                           text=label,
                           showarrow=False,
                           yshift=10,
                           xshift=50,
                           font=dict(size=15))

    else:
        intersection_point = 'Approximation failed'

    return fig



#%% Misc

__all__ = ['prepare_fv', 'get_intersection_point', 'plot_intersection_point']


