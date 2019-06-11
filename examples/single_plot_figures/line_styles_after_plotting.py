"""
This is going to take advantage of the fact that in WrapPlotLib
the most resent plotted line is stored into the plot.line attribute.
It shows how to set line styles accessing the
wrapplotlib.line.WPL2DLine object directly.
"""
from collections import namedtuple

import numpy as np

from wrapplotlib.figures import SinglePlotFigure

# Need to load some data first.
ShockData = namedtuple("ShockData", ['time', 'acceleration'])
data = np.loadtxt('../../tests/data/shock_00.csv', delimiter=',')
shock_data = ShockData(data[:, 0], data[:, 1])

# Loading of data is done. This is now the plotting part.
fig = SinglePlotFigure()
fig.title = "Basic Time History Plot"
fig.plot(shock_data.time, shock_data.acceleration)
fig.plot.title = "Shock Data"
fig.plot.x_label = "Time (s)"
fig.plot.y_label = "Acceleration (G)"

# Edit the style of the line the last plotted line is always stored in
# the plot's line attribute. Therefor we can easily access the lines.
fig.plot.line.color = 'k'
fig.plot.line.marker = ''

# Also we can simply update the styles from a dictionary where the keys
# are attributes in wrapplotlib.line.WPL2DLine and values are valid
# values for the line.
style_dict = {
    'color': 'k',
    'marker': ''
}
fig.plot.line.style_dict = style_dict

fig.show()