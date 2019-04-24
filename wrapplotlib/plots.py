from typing import Union

from matplotlib.axes import Axes

from . import log
from .artists import WPLArtist
from .lines import WPL2DLine
from .styles import BaseStyle, StyleMeta
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
            self._lines += [WPL2DLine(self.figure, self, None, l) for l in lines]
        else:
            self._lines += [WPL2DLine(self.figure, self, self._styler(), l) for l in lines]

    def _get_line(self):
        return self.lines[-1]

    def _set_line(self, value):
        log.warning("line setter is not implemented as this is"
                    "an internally tracked variable.")

    def _del_line(self):
        del self.lines[-1]

    # noinspection PyPropertyDefinition
    line = property(
        fget=lambda self: self._get_line(),
        fdel=lambda self: self._del_line(),
        fset=lambda self: self._set_line()
    )

    def _get_lines(self):
        self._sync_mpl_wpl_lines()
        return self._lines

    def _set_lines(self, value):
        log.warning("lines setter is not implemented as this is"
                    "an internally tracked variable.")

    def _del_lines(self):
        [l.__del__() for l in self._lines]
        self._lines = []

    # noinspection PyPropertyDefinition
    lines = property(
        fget=lambda self: self._get_lines(),
        fset=lambda self, value: self._set_lines(value),
        fdel=lambda self: self._del_lines()
    )

    def _get_styler(self):
        return self._styler

    def _set_styler(self, value):
        if not issubclass(value, StyleMeta):
            raise TypeError('A Style needs to be derived from wrapplotlib.styles.StyleMeta '
                            'this is to ensure that the styler works as expected within the'
                            'rest of WPL classes.')
        self._styler = value()

    def _del_styler(self):
        self._styler = None

    # noinspection PyPropertyDefinition
    styler = property(
        fget=lambda self: self._get_styler(),
        fset=lambda self, value: self._set_styler(value),
        fdel=lambda self: self._del_styler()
    )

    def _get_x_scale(self):
        return self._type[0]

    def _set_x_scale(self, value):
        if value.lower() not in ['linear', 'log']:
            raise ("Error in setting x_scale property. Valid values are "
                   "'Linear' or 'Log")
        self._type[0] = value.lower()

    def _del_x_scale(self):
        self._type[0] = 'Linear'

    # noinspection PyPropertyDefinition
    x_scale = property(
        fget=lambda self: self._get_x_scale(),
        fset=lambda self, value: self._set_x_scale(value),
        fdel=lambda self: self._del_x_scale()
    )

    def _get_y_scale(self):
        return self._type[1]

    def _set_y_scale(self, value):
        if value.lower() not in ['linear', 'log']:
            raise ("Error in setting y_scale property. Valid values are "
                   "'Linear' or 'Log")
        self._type[1] = value

    def _del_y_scale(self):
        self._type[1] = 'Linear'

    # noinspection PyPropertyDefinition
    y_scale = property(
        fget=lambda self: self._get_y_scale(),
        fset=lambda self, value: self._set_y_scale(value),
        fdel=lambda self: self._del_y_scale()
    )

    def _sync_mpl_wpl_lines(self):
        for line in self._fake_it.lines:
            if line not in self._lines:
                self._lines.append(WPL2DLine(self.figure, self,
                                             None, line))



