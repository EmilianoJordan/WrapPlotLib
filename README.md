# WrapPlotLib

WrapPlotLib is meant to be a wrapper for the matplotlib library. 
This isn't an attempt to make it better this is just to impose my 
opinion of how I'd want plotting in Python to work. This is a very brief
attempt to flush out a concept so far. I'm looking for opinions, good
and constructive, and if you'd like some contributions. 

Thanks!

Also, here's what WrapPlotLib Looks like. 

`# Need to load some data first.
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
fig.show()`

