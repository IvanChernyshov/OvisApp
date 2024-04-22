'''Unit tests for smth'''

#%% Imports

import sys, os
sys.path.append(os.path.join(os.path.abspath(__file__), '../../'))

import pytest

import ovis


#%% Tests

class TestDummy():
    
    ##### Initialization #####
    
    def test_cosdeg(self):
        assert ovis.mycosdeg(30) == pytest.approx(0.8660254037, 10**-6)
        assert ovis.mycosdeg(60) == pytest.approx(0.5, 10**-6)


