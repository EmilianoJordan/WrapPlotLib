"""
One of the things that continues to bother me after years of working
with MATLAB and Matplotlib is the fact that it's tedious to group
lines together under one legend. I know an inline if statement can be
used to control the legend yet I'd prefer to have an object to control
line groups. This way it would be simple to extend the line group to
include other features like averages or 95% CI.
(More tutorials coming on that soon.)

"""
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

# The default styler is currently being used. But any style can be
# changed on an entire ling group at once. Here's a quick demonstration
# by changing the markers
'''
# @TODO this is not working. The legend is showing the old artist styles
not the new styles. It has to do with when legend is called.
I need to work on that but it may involve callbacks being implemented
sooooooo... some design decisions need to be made and I'm going to 
kick the can on that and think about it a lot more. 
Although it is probably the next thing to do as
I need to figure this out before getting too far down the rabbit hole.
'''
fig.plot['X-Axis'].marker = ''
fig.plot['Y-Axis'].marker = 'D'
fig.plot['Z-Axis'].marker = 'X'

fig.plot['X-Axis'].color = 'k'

fig.show()