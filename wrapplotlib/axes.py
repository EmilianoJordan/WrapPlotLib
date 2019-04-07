"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from matplotlib.axes import Axes

from ._mixins import FakeIt
from .titles import AxisTitle


class BaseAxis(FakeIt):

    def __init__(self, figure, axis):
        from .figures import BaseFigure

        if not isinstance(figure, BaseFigure):
            raise TypeError('WPL BaseAxis needs a parent figure of wrapplotlib.BaseFigure'
                            'or a subclass of BaseFigure to operate properly.')
        if not isinstance(axis, Axes):
            raise TypeError('WPL BaseAxis is meant to be initialized with an instance'
                            'of matplotlib.axes.Axes')

        self._parent_figure = figure
        self._fake_it = axis
        # This is purely for code readability as _fake_it in this case is an instance of
        # matplotlib.axes.Axes
        # https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes
        self.axis = self._fake_it

        # self._title = AxisTitle(self)

    # @property
    # def title(self):
    #     return self._title
    #
    # @title.setter
    # def title(self, val):
    #     self._title(val)
    #
    # @title.deleter
    # def title(self):
    #     self.title('')