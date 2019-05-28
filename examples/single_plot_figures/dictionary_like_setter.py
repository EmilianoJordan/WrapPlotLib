"""
Created: 5/6/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
import numpy as np

from wrapplotlib.figures import SinglePlotFigure

x_data = np.array(range(5))
y_data = 1 + x_data * 2

fig = SinglePlotFigure()
fig.plot['Test'] = x_data, y_data

fig.show()