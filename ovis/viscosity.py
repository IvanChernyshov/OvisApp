'''Predicting viscosity and related features'''

#%% Imports

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from ovis.models import Model


#%% Functions

def test_visc_temp_curve(model: Model, feature_vectors: pd.core.frame.DataFrame,
                         row_idx: int) -> None:
    """Shows graph of viscosity versus temperature"""
    temp_range = [i for i in range(6, 29, 1)]
    row = feature_vectors.iloc[[row_idx], :]
    fvs = pd.DataFrame(np.repeat(row.values, 23, axis=0))
    fvs.columns = feature_vectors.columns
    fvs['Температура пласта, °С'] = temp_range
    predicted_viscosity = model.predict(fvs)
    sns.scatterplot(x=temp_range, y=predicted_viscosity)
    
    plt.show()


#%% Misc

__all__ = ['test_visc_temp_curve']

