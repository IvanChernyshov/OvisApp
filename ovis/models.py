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
                 all_features_required: bool, predicts_log: bool) -> Model:
        self.features = features
        self.all_features_required = all_features_required
        self.predicts_log = predicts_log
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
            x = pd.concat([feature_vectors, empty], axis = 1)
        x = x[self.features]
        outp = self.model.predict(x)
        if self.predicts_log:
            outp = [10**x for x in outp]
        
        return outp


def model_from_model_name(name: str) -> Model:
    '''Constructs Model from model's name'''
    info = json.loads(pkgutil.get_data('ovis', 'data/model_parameters.json'))
    model = Model(info[name]['model_path'],
                  info[name]['features'],
                  info[name]['all_features_required'],
                  info[name]['predicts_log'])
    
    return model



#%% Models

viscUniModel = model_from_model_name('viscUniModel')
viscAccModel = model_from_model_name('viscAccModel')


#%% Misc

__all__ = ['viscUniModel', 'viscAccModel',
           'Model', 'model_from_model_name']


