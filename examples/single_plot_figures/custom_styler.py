"""
This is a simple file to show how to create a figure class with a plot
that overrides the base styler created in wrapplotlib.styles.BaseStyle.

Created: 4/19/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from collections import namedtuple

import numpy as np

from wrapplotlib.figures import SinglePlotFigure
from wrapplotlib.styles import BaseStyle


class CustomStyle(BaseStyle):
    """
    Custom Styler will yield a black line ever single call.
    """
    style_map = {
        'color': (0.0, 0.0, 0.0, 1.0),
        'line_width': .05,
    }

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return self.style_map

    def next(self):
        return self.style_map

    def reset(self):
        pass


# Need to load some data first.
ShockData = namedtuple("ShockData", ['time', 'acceleration'])
data = np.loadtxt('../../tests/data/shock_00.csv', delimiter=',')
shock_data = ShockData(data[:, 0], data[:, 1])

# Loading of data is done. This is now the plotting part.
fig = SinglePlotFigure()
fig.plot.styler = CustomStyle
fig.title = "Basic Time History Plot"
fig.plot(shock_data.time, shock_data.acceleration)
fig.plot.title = "Shock Data"
fig.plot.x_label = "Time (s)"
fig.plot.y_label = "Acceleration (G)"
fig.show()