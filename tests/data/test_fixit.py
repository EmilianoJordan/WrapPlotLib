"""
Created: 4/4/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan

This is an important file to make sure that the FixIt Class is included
in all the classes it should be. This is a sanity check.
"""

from wrapplotlib.figures import BaseFigure, SinglePlotFigure
from wrapplotlib.text import WPLText
from wrapplotlib.plots import BasePlot


def test_BaseFigure():
    figure = BaseFigure()
    # check that some WPL methods are in __dir__
    assert "add_subplot" in figure.__dir__()
    assert "close" in figure.__dir__()
    assert "save" in figure.__dir__()

    # check that some MPL methods are there too.
    assert "get_facecolor" in figure.__dir__()
    assert "get_size_inches" in figure.__dir__()  # snicker snicker snicker
    assert "waitforbuttonpress" in figure.__dir__()

def test_SinglAxisFigure():
    figure = SinglePlotFigure()
    # check that some WPL methods are in __dir__
    assert "add_subplot" in figure.__dir__()
    assert "close" in figure.__dir__()
    assert "save" in figure.__dir__()

    # check that some MPL methods are there too.
    assert "get_facecolor" in figure.__dir__()
    assert "get_size_inches" in figure.__dir__()  # snicker snicker snicker
    assert "waitforbuttonpress" in figure.__dir__()


def test_WPLText():
    text = WPLText("test")
    # check that some WPL methods are in __dir__

    # There isn't really any new method's implemented by WPL yet.

    # check that some MPL methods are there too.
    str(text)

    pass


def test_BaseAxis():
    # check that some WPL methods are in __dir__

    # check that some MPL methods are there too.

    pass