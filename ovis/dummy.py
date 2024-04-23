'''Dummy module'''

#%% Imports

import math
import pickle, pkgutil


#%% Functions

def mycosdeg(deg: float) -> float:
    '''Returns cosine of the input angle given in degrees'''
    return math.cos(math.radians(deg))


def load_model_dummy() -> float:
    '''Loads dummy text from test pickle in models dir'''
    content = pkgutil.get_data('ovis', 'data/test.pickle')
    text = pickle.loads(content)
    
    return text



#%% Misc

__all__ = ['mycosdeg', 'load_model_dummy']


