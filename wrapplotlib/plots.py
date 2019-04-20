"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from matplotlib.axes import Axes

from .artists import WPLArtist
from .lines import WPLLine2D
from .styles import BaseStyle
from .text import WPLText


class BasePlot(WPLArtist):

    def __init__(self, figure, axis, styler=BaseStyle):
        from .figures import BaseFigure

        if not isinstance(figure, BaseFigure):
            raise TypeError('WPL BasePlot needs a parent figure of wrapplotlib.BaseFigure'
                            'or a subclass of BaseFigure to operate properly.')
        if not isinstance(axis, Axes):
            raise TypeError('WPL BasePlot is meant to be initialized with an instance'
                            'of matplotlib.axes.Axes')

        self.figure: 'BaseFigure' = figure
        self._fake_it: Axes = axis

        # Setup the Axis Title and wrap in WPLText
        self.__class__.title = WPLText(axis.set_title(''))
        self.title.x = 0.485

        # Setup the X and Y Labels
        self.__class__.x_label = WPLText(self._fake_it.set_xlabel(''))
        self.__class__.y_label = WPLText(self._fake_it.set_ylabel(''))

        # Setup the X and Y Scales: This is just setting to defaults
        # but I'm doing this to show where subclassing the scales might
        # be done.
        self._type = ["Linear", "Linear"]

        self._lines = []
        self._styler = styler()

    def __call__(self, *args, scalex=True, scaley=True, **kwargs):
        self.plot(*args, scalex=True, scaley=True, **kwargs)

    def __iter__(self):
        return (l for l in self.lines)

    def plot(self, *args, scalex=True, scaley=True, **kwargs):
        lines = self._fake_it.plot(
            *args,
            scalex=scalex,
            scaley=scaley,
            **kwargs
        )
        if self._styler is None:
            self._lines += [WPLLine2D(self.figure, self, None, l) for l in lines]
        else:
            self._lines += [WPLLine2D(self.figure, self, self._styler(), l) for l in lines]

    @property
    def line(self):
        return self.lines[-1]

    @line.deleter
    def line(self):
        # @TODO need to edit this method once it's figured out how I'm going to delete lines.
        del self.lines[-1]

    @property
    def lines(self):
        self._sync_mpl_wpl_lines()
        return self._lines

    @lines.deleter
    def lines(self):
        [l.__del__() for l in self._lines]
        self._lines = []

    @property
    def styler(self):
        return self._styler

    @styler.setter
    def styler(self, value: BaseStyle):
        styler = value()
        if not callable(styler):
            raise BaseException('Styler needs to be a callable object. See __call__')
        if not isinstance(styler(), dict):
            raise BaseException('Styler needs to return a dict of key value pairs for WPLLine '
                                'attributes')
        if not hasattr(styler, 'reset') and callable(styler.reset):
            raise BaseException('Styler needs to have a reset method that resets the order '
                                'of the styles being generated. This is called when '
                                'replotting to make sure lines maintain style order.')
        styler.reset()
        self._styler = styler

    @styler.deleter
    def styler(self):
        self._styler = None

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
                self._lines.append(WPLLine2D(self.figure, self,
                                             None, line))
