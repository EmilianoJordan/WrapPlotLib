"""
Created: 4/7/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from collections import namedtuple
import numpy as np
import pytest

from wrapplotlib.figures import BaseFigure

ShockData = namedtuple("ShockData", ['time', 'acceleration'])

data = np.loadtxt('D:\gramming\WrapPlotLib\\tests\data\shock_00.csv', delimiter=',')
data = ShockData(data[:, 0], data[:, 1])

fig = BaseFigure()
a = fig.add_subplot(1, 1, 1)
# title = fig.suptitle('')
# fig.suptitle('Shock Data')
# title.set_size(32
# title.set_size(32)
# fig.title.set_text("Shock Data")
# fig.title.set_size('xx-large')

fig.title.text = "Shock Data"
fig.title.size = 'larger'
# print(fig.title.size)
# fig.title.size = 'xx-large'
a.plot(data.time, data.acceleration)
a.set_title("Basic Shock")
for line in a:
    print(line.get_data())
fig.show()