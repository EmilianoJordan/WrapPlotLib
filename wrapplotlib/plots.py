from typing import Union

from matplotlib.axes import Axes

from . import log
from .artists import WPLArtist
from .line_groups import WPL2DLineGroup
from .lines import WPL2DLine
from .styles import BaseLineStyle, StyleMeta
from .text import WPLText


class BasePlot(WPLArtist):

    def __init__(self, figure, axis, styler=BaseLineStyle):
        from .figures import BaseFigure

        if not isinstance(figure, BaseFigure):
            raise TypeError('WPL BasePlot needs a parent figure of wrapplotlib.BaseFigure'
                            'or a subclass of BaseFigure to operate properly.')
        if not isinstance(axis, Axes):
            raise TypeError('WPL BasePlot is meant to be initialized with an instance'
                            'of matplotlib.axes.Axes')

        self.figure: BaseFigure = figure
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

    def _get_x_lims(self):
        return self._fake_it.get_xlim()

    def _set_x_lims(self, value):
        self._fake_it.set_xlim(*value)

    def _del_x_lims(self):
        log.warning("y_lim deleter is not yet implemented.")

    # noinspection PyPropertyDefinition
    x_lims = property(
        fget=lambda self: self._get_x_lims(),
        fset=lambda self, value: self._set_x_lims(value),
        fdel=lambda self: self._del_x_lims()
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

    def _get_y_lims(self):
        return self._fake_it.get_ylim()

    def _set_y_lims(self, value: Union[tuple, list]):
        self._fake_it.set_ylim(*value)

    def _del_y_lims(self):
        log.warning("y_lim deleter is not yet implemented.")

    # noinspection PyPropertyDefinition
    y_lims = property(
        fget=lambda self: self._get_y_lims(),
        fset=lambda self, value: self._set_y_lims(value),
        fdel=lambda self: self._del_y_lims()
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


class BaseLinePlot(BasePlot):

    def __init__(self, figure, axis, styler=BaseLineStyle):
        super(BaseLinePlot, self).__init__(figure, axis)

        self._lines = []
        self._styler = styler()

    def __call__(self, *args, scalex=True, scaley=True, **kwargs):
        return self.plot(*args, scalex=True, scaley=True, **kwargs)

    def __iter__(self):
        return (l for l in self.lines)

    def __getitem__(self, item):
        """
        Lines can be accessed via their label as the key
        of the plot.


        :param item:
        :type item:
        :return:
        :rtype:
        """
        for l in self.lines:
            if l._label == item:
                return l

    def __setitem__(self, key, value):
        """
        Item access can be used to add a line with it's label
        where the key is the label value and the value should
        be a tuple or list x and y data:

        See: examples/single_plot_figures/dictionary_like_setter.py

        :param key:
        :type key:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        line = self.plot(*value)[0]
        line.label = key

    def plot(self, *args, scalex=True, scaley=True, **kwargs):
        lines = self._fake_it.plot(
            *args,
            scalex=scalex,
            scaley=scaley,
            **kwargs
        )
        if self._styler is None:
            wpl_lines = [WPL2DLine(self.figure, self, None, l) for l in lines]

        else:
            wpl_lines = [WPL2DLine(self.figure, self, self._styler(), l) for l in lines]

        self._lines += wpl_lines

        return wpl_lines

    def _get_line(self):
        return self.lines[-1]

    def _set_line(self, value):
        log.warning("line setter is not implemented as this is"
                    "an internally tracked attribute.")

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

    def _sync_mpl_wpl_lines(self):
        for line in self._fake_it.lines:
            if line not in self._lines:
                self._lines.append(WPL2DLine(self.figure, self,
                                             None, line))

    def update_axis_limits(self):
        x_min = self._fake_it.dataLim.x0
        x_max = self._fake_it.dataLim.x1
        y_min = self._fake_it.dataLim.y0
        y_max = self._fake_it.dataLim.y1

        for l in self.lines:
            x_min = min(x_min, min(l.data[0]))
            x_max = max(x_max, max(l.data[0]))
            y_min = min(y_min, min(l.data[1]))
            y_max = max(y_max, max(l.data[1]))

        self._fake_it.dataLim.x0 = x_min
        self._fake_it.dataLim.x1 = x_max
        self._fake_it.dataLim.y0 = y_min
        self._fake_it.dataLim.y1 = y_max

        self._fake_it.autoscale_view(scalex=True, scaley=True)


class BaseGroupPlot(BasePlot):

    def __init__(self, figure, axis, styler=BaseLineStyle):
        super(BaseGroupPlot, self).__init__(figure, axis)

        self._line_groups = {}
        self._styler = styler()

        '''
        Legend is always turned on for GroupLinePlots  if you're not
        going to use a legend the easiest way is just to use the LinePlot
        class.
        '''
        self._fake_it.legend()

    def __call__(self, *args, label=None, scalex=True, scaley=True, **kwargs):
        # if label is None or label == '':
        #     log.warning('A Label must be supplied when plotting with '
        #                 'wrapplotlib.plots.BaseGroupPlot')

        return self.plot(*args, scalex=True, scaley=True, **kwargs)

    def __getitem__(self, item):
        """
        Lines can be accessed via their label as the key
        of the plot.


        :param item:
        :type item:
        :return:
        :rtype:
        """
        self.sync_line_groups()

    def __setitem__(self, key, value):
        """
        Item access can be used to add a line with its label
        where the key is the label value and the value should
        be a tuple or list x and y data:

        See: examples/single_plot_figures/dictionary_like_setter.py

        :param key:
        :type key:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.plot(*value, label=key)

    def plot(self, *args, scalex=True, scaley=True, **kwargs):
        lines = self._fake_it.plot(
            *args,
            scalex=scalex,
            scaley=scaley,
            **kwargs
        )
        wpl_lines = []

        for line in lines:
            '''
            self._line_groups is a dictionary of callable WPL2DLineGroup
            objects and their labels as keys.
            
            This adds the line to a WPL2DLineGroup by calling the object.
            if the dictionary item does not exist a new one is created
            using setdefault() and then called. 
            '''
            try:
                wpl_lines.append(self._line_groups[line._label](line))
            except KeyError:
                line_group = WPL2DLineGroup(self.figure,
                                            self,
                                            self._styler()
                                            )
                self._line_groups[line._label] = line_group

                wpl_lines.append(line_group(line))

        return wpl_lines


def _sync_mpl_wpl_line_groups(self):
    """
    @TODO need to implement this
    This is a function that should look at all the labels of the
    lines in the line group and then sorts them to make sure there
    in the proper grouping.

    It should be called before any access to a line group is give.
    :return:
    :rtype:
    """
    pass
