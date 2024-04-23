'''Functionality for saving and setting program's parameters'''

#%% Imports

import os


#%% Functions

def get_app_dir() -> str:
    '''Returns path to the app's directory in user's home dir'''
    path = os.path.join(os.path.expanduser("~"), '.ovis')
    if not os.path.exists(path):
        os.mkdir(path)
    
    return path



#%% Misc

__all__ = ['get_app_dir']


