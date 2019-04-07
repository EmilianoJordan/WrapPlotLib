"""
Created: 3/20/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np

from wrapplotlib.figures import BaseFigure

ShockData = namedtuple("ShockData", ['time', 'acceleration'])

data = np.loadtxt('../tests/data/shock_00.csv', delimiter=',')
shock_data = ShockData(data[:, 0], data[:, 1])

fig = BaseFigure()
a = fig.add_subplot(1, 1, 1)
fig.title = "Shock Data"
a.plot(shock_data.time, shock_data.acceleration)
a.set_title("Basic Shock")
fig._title.get_position()
a._title.get_position()
fig.show()
fig.show()
