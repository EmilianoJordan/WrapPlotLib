"""
Created: 4/2/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from collections import namedtuple
import numpy as np
import pytest

ShockData = namedtuple("ShockData", ['time', 'acceleration'], verbose=True)


@pytest.fixture(scope='session')
def shock_data():
    data = np.loadtxt('data/shock_00.csv', delimiter=',')
    return ShockData(data[:, 0], data[:, 1])
