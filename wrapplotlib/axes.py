"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from ._mixins import FakeIt
from .lines import WPLLine2D
from .text import WPLText


class BaseAxis(FakeIt):

    # @TODO Need to figure out figure sizing and the axis y label.

    def __init__(self, figure, axis):
        from .figures import BaseFigure

        if not isinstance(figure, BaseFigure):
            raise TypeError('WPL BaseAxis needs a parent figure of wrapplotlib.BaseFigure'
                            'or a subclass of BaseFigure to operate properly.')
        if not isinstance(axis, Axes):
            raise TypeError('WPL BaseAxis is meant to be initialized with an instance'
                            'of matplotlib.axes.Axes')

        self._parent_figure: Figure = figure
        self._fake_it: Axes = axis

        # Setup the Axis Title and wrap in WPLText
        self.title = WPLText(axis.set_title(''))
        self.title.x = 0.485

        # Setup the X and Y Labels
        self._xlabel = WPLText(self._fake_it.set_xlabel(''))
        self._ylabel = WPLText(self._fake_it.set_ylabel(''))

        # Setup the X and Y Scales: This is just setting to defaults
        # but I'm doing this to show where subclassing the scales might
        # be done.
        self._type = ["Linear", "Linear"]
        self._add_line = self._fake_it.plot

        self._lines = []

    def __iter__(self):
        return (l for l in self.lines)

    def plot(self, *args, scalex=True, scaley=True, **kwargs):
        lines = self._fake_it.plot(
            *args,
            scalex=scalex,
            scaley=scaley,
            **kwargs
        )
        self._lines += [WPLLine2D(l) for l in lines]
        # return lines

    @property
    def lines(self):
        self._sync_mpl_wpl_lines()
        return self._lines

    @lines.deleter
    def lines(self):
        pass

    @property
    def x_label(self):
        return self._xlabel

    @x_label.setter
    def x_label(self, value):
        self._xlabel.text = value

    @x_label.deleter
    def x_label(self):
        self._xlabel.text = ''

    @property
    def y_label(self):
        return self._ylabel

    @y_label.setter
    def y_label(self, value):
        self._ylabel.text = value

    @y_label.deleter
    def y_label(self):
        self._ylabel.text = ''

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
                self._lines.append(WPLLine2D(line))

