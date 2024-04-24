import pickle

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from ovis.constants import sel_features

model_path = 'models/hgbr_model.pkl'
loaded_model = pickle.load(open(model_path, 'rb'))


def predict_viscosity(features_df):
    """Returns predicted value of viscosity"""
    x = pd.DataFrame(columns=sel_features)
    x = pd.concat([x, features_df])[sel_features]
    prediction = loaded_model.predict(x)
    return prediction


def temperature_viscosity_curve(features_df):
    """Shows graph of viscosity versus temperature"""
    temp_range = [i for i in range(6, 29, 1)]
    features_df = features_df.iloc[[295], :]
    new_df = pd.DataFrame(np.repeat(features_df.values, 23, axis=0))
    new_df.columns = features_df.columns
    new_df['Температура пласта, °С'] = temp_range
    predicted_viscosity = predict_viscosity(new_df)
    sns.scatterplot(x=temp_range, y=predicted_viscosity)

    plt.show()


data_test = pd.read_csv('data/sample_test.csv')
