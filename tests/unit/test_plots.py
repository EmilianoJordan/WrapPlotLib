"""
Created: 5/6/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
import numpy as np

from wrapplotlib.figures import SinglePlotFigure
from wrapplotlib.lines import WPL2DLine

def test_plot_resize_limits():
    """
    When the data is changed the window should be resized on the plot.
    """
    data = np.array(range(5))
    data_2 = np.array(range(7)) - 1

    fig = SinglePlotFigure()
    fig.plot(data, data)

    x_min, x_max = fig.plot.x_lims
    y_min, y_max = fig.plot.y_lims

    fig.plot.line.data = data_2, data_2

    new_x_min, new_x_max = fig.plot.x_lims
    new_y_min, new_y_max = fig.plot.y_lims

    # Make sure the padding is added to the data
    assert new_y_max > max(data_2)
    assert new_x_max > max(data_2)
    assert new_y_min < min(data_2)
    assert new_x_min < min(data_2)

    # Make sure the new limits are different than the old ones.
    assert x_min > new_x_min
    assert x_max < new_x_max
    assert y_min > new_y_min
    assert y_max < new_y_max


def test_iteration():
    """
    When iterating over a plot lines should be returned.
    """
    data = np.array(range(5))
    data_2 = np.array(range(7)) - 1

    fig = SinglePlotFigure()
    fig.plot(data, data)
    fig.plot(data_2, data_2)

    for l in fig.plot:
        assert isinstance(l, WPL2DLine)


def test_line_returns_last_plotted_line():
    """
    when lines are plotted the most recently plotted line should be
    stored in fig.plot.line
    """
    data = np.array(range(5))

    fig = SinglePlotFigure()
    lines = fig.plot(data, data)

    assert fig.plot.line == lines[0]


def test_item_getter():
    data = np.array(range(5))

    fig = SinglePlotFigure()
    lines = fig.plot(data, data)

    fig.plot.line.label = "Test"

    line = fig.plot['Test']

    assert line == lines[0]

def test_item_setter():
