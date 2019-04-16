"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from matplotlib.axes import Axes

from ._mixins import FakeIt
from .lines import WPLLine2D
from .styles import BaseStyle
from .text import WPLText


class BaseAxis(FakeIt):

    def __init__(self, figure, axis, styler=BaseStyle):
        from .figures import BaseFigure

        if not isinstance(figure, BaseFigure):
            raise TypeError('WPL BaseAxis needs a parent figure of wrapplotlib.BaseFigure'
                            'or a subclass of BaseFigure to operate properly.')
        if not isinstance(axis, Axes):
            raise TypeError('WPL BaseAxis is meant to be initialized with an instance'
                            'of matplotlib.axes.Axes')

        self.figure: 'BaseFigure' = figure
        self._fake_it: Axes = axis

        # Setup the Axis Title and wrap in WPLText
        self.title = WPLText(axis.set_title(''))
        self.title.x = 0.485

        # Setup the X and Y Labels
        self.x_label = WPLText(self._fake_it.set_xlabel(''))
        self.y_label = WPLText(self._fake_it.set_ylabel(''))

        # Setup the X and Y Scales: This is just setting to defaults
        # but I'm doing this to show where subclassing the scales might
        # be done.
        self._type = ["Linear", "Linear"]
        self._add_line = self._fake_it.plot

        self._lines = []
        self._styler = styler()

    def __iter__(self):
        return (l for l in self.lines)

    def plot(self, *args, scalex=True, scaley=True, **kwargs):
        lines = self._fake_it.plot(
            *args,
            scalex=scalex,
            scaley=scaley,
            **kwargs
        )
        self._lines += [WPLLine2D(self.figure, self, self._styler(), l) for l in lines]


    @property
    def lines(self):
        self._sync_mpl_wpl_lines()
        return self._lines

    @lines.deleter
    def lines(self):
        pass

    @property
    def x_scale(self):
        return self._type[0]

    @x_scale.setter
    def x_scale(self, value: str):
        if value.lower() in ['linear', 'log']:
            self._type[0] = value
            return
        raise ("Error in setting x_scale property. Valid values are "
               "'Linear' or 'Log")

    @x_scale.deleter
    def x_scale(self):
        self._type[0] = 'Linear'

    @property
    def y_scale(self):
        return self._type[1]

    @y_scale.setter
    def y_scale(self, value: str):
        if value.lower() in ['linear', 'log']:
            self._type[1] = value
            return
        raise ("Error in setting y_scale property. Valid values are "
               "'Linear' or 'Log")

    @y_scale.deleter
    def y_scale(self):
        self._type[1] = 'Linear'

    def _sync_mpl_wpl_lines(self):
        for line in self._fake_it.lines:
            if line not in self._lines:
                self._lines.append(WPLLine2D(self.figure, self, line))

