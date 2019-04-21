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

from wrapplotlib.figures import SinglePlotFigure

ShockData = namedtuple("ShockData", ['time', 'acceleration'], verbose=True)


@pytest.fixture(scope='session')
def shock_data():
    data = np.loadtxt('data/shock_00.csv', delimiter=',')
    return ShockData(data[:, 0], data[:, 1])

@pytest.fixture(scope='function')
def shock_single_figure(shock_data):
    fig = SinglePlotFigure()
    fig.title = "Basic Time History Plot"
    fig.plot(shock_data.time, shock_data.acceleration)
    fig.plot.title = "Shock Data"
    fig.plot.x_label = "Time (s)"
    fig.plot.y_label = "Acceleration (G)"
    yield fig
    del fig
