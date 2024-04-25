'''ML models for oil viscosity'''

#%% Improts

from __future__ import annotations

import pkgutil, pickle, json

import pandas as pd
import numpy as np


#%% Basic class

class Model():
    '''Wrapper for viscosity models'''
    
    def __init__(self, model_path: str, features: list[str],
                 all_features_required: bool) -> Model:
        self.features = features
        self.all_features_required = all_features_required
        content = pkgutil.get_data('ovis', model_path)
        self.model = pickle.loads(content)
    
    def predict(self, feature_vectors: pd.core.frame.DataFrame) -> np.ndarray:
        '''Predicts viscosity for the given feature vectors'''
        x = feature_vectors.copy()
        missing_cols = [col for col in self.features if col not in feature_vectors]
        if missing_cols and self.all_features_required:
            raise ValueError(f'Some features are missing from the feature vector: {", ".join(missing_cols)}')
        if missing_cols:
            empty = pd.DataFrame({col: np.nan for col in self.features \
                                  if col not in feature_vectors},
                                 feature_vectors.index)
            x = pd.concat([feature_vectors, empty])
        x = x[self.features]
        
        return self.model.predict(x)


def model_from_model_name(name: str) -> Model:
    '''Constructs Model from model's name'''
    info = json.loads(pkgutil.get_data('ovis', 'data/model_parameters.json'))
    model = Model(info[name]['model_path'],
                  info[name]['features'],
                  info[name]['all_features_required'])
    
    return model



#%% Models

viscUniModel = model_from_model_name('viscUniModel')


#%% Misc

__all__ = ['viscUniModel', 'Model', 'model_from_model_name']


