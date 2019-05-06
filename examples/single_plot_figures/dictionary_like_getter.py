"""
Created: 5/6/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
import numpy as np

from wrapplotlib.figures import SinglePlotFigure

data = np.array(range(5))

fig = SinglePlotFigure()
lines = fig.plot(data, data)

fig.plot.line.label = "Test"

line = fig.plot['Test']