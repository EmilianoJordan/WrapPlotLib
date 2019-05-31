# WrapPlotLib

WrapPlotLib is meant to be a wrapper for the matplotlib library. 
This isn't an attempt to make it better this is just to impose my 
opinion of how I'd want plotting in Python to work. This is a very brief
attempt to flush out a concept so far. I'm looking for opinions, good
and constructive, and if you'd like some contributions. 

WPL also is meant to work with the Anaconda distribution and tries to
use PyQT5. This is because it's the most reliable backend that I've 
found for matplotlib. The decision to try and enforce this is to try 
and maintain consistency in plots. I'm sure that I've missed a lot
as even trying to get .show() to work properly has been a headache just
between running file through the executable and in the Python console.

Thanks!

Also, if you're curious here's what WrapPlotLib Looks like:

## WPL Example

```python
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

# Edit style of the line. The last plotted line is always stored in
# the plot's line attribute. Therefor we can easily access lines as they
# are plotted.
fig.plot.line.color = 'k'
fig.plot.line.marker = ''
fig.show()
```

![Basic Plot](https://raw.githubusercontent.com/EmilianoJordan/WrapPlotLib/master/examples/single_plot_figures/images/line_styles_after_plotting.png)


As you can see settings for the plot that were once hidden behind
getters and setters are now accessed via the more pythonic way of using
attributes.

Work is ongoing but there is a way to insert custom style generators
so that the lines are controllable by you in an OOP, pythonic way.

## WPL Grouped Lines Example

One of the things that continues to bother me after years of working
with MATLAB and Matplotlib is the fact that it's tedious to group
lines together under one legend. I know an inline if statement can be
used to control the legend yet I'd prefer to have an object to control
line groups. This way it would be simple to extend the line group to
include other features like averages or 95% CI. 
(More tutorials coming on that soon.)

```python
import numpy as np

from wrapplotlib.figures import SingleGroupPlotFigure

# First let's create some sample data.
data_time = np.array(range(10))

data_x_axis = data_time
data_y_axis = data_time + 5
data_z_axis = data_time * 3

# Normally in my use cases this would be stored in data files pulled
# from sensors but for now storing them as a list demonstrates the 
# looping functionality.
tests = [
    {
        'time': data_time,
        'x_axis': data_x_axis,
        'y_axis': data_y_axis,
        'z_axis': data_z_axis,
    },
    {
        'time': data_time,
        'x_axis': data_x_axis * 0.95,
        'y_axis': data_y_axis * 0.95,
        'z_axis': data_z_axis * 0.95,
    },
    {
        'time': data_time,
        'x_axis': data_x_axis * 1.05,
        'y_axis': data_y_axis * 1.05,
        'z_axis': data_z_axis * 1.05,
    },
]

fig = SingleGroupPlotFigure()

for test in tests:
    # By using the plot's item functionality we can group lines
    # together under the same label.
    fig.plot['X-Axis'] = test['time'], test['x_axis']
    fig.plot['Y-Axis'] = test['time'], test['y_axis']
    fig.plot['Z-Axis'] = test['time'], test['z_axis']

fig.show()

```

![Grouped Lines Plot](https://raw.githubusercontent.com/EmilianoJordan/WrapPlotLib/master/examples/single_plot_figures/images/grouped_lines.png)