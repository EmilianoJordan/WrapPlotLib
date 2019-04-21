"""
Created: 4/10/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from typing import Union

from matplotlib.lines import Line2D

from . import log
from .artists import WPLArtist


class WPLLine2D(WPLArtist):

    def __init__(self,
                 figure: 'BaseFigure',
                 plot: 'BasePlot',
                 style_dict: Union[dict, None],
                 line: Line2D):
        self.figure = figure
        self.plot = plot
        self._fake_it: Line2D = line

        self.apply_styles_from_dict(style_dict)

    def __del__(self):
        self._fake_it.remove()
        super().__del__()

    def __eq__(self, other: Union['WPLLine2D', Line2D]):
        """
        The equality of two lines is based solely on the data
        that defines it.
        """
        # If the other instance is that of Line2D we can just check to
        # see if the underlying matplotlib.line.Line2D structure
        # saved in self._fake_it is the same.
        if isinstance(other, Line2D):
            return self._fake_it is other

        return self._fake_it is other._fake_it
        #
        # # If the line belongs to a different figure or plot it is
        # # probably not the same line, eh?
        # if self.plot is other.plot or self.figure is self.figure:
        #     return False
        #
        # # If the lengths of the data are not the same than we can exit.
        # # Lines must have equal length x and y data so checking x length
        # # is all that's necessary.
        # if len(self.data[0]) != len(self.get_data()[0]):
        #     return False
        #
        # # Check the equality of each set of data. There may be a
        # # tolerance problem here in rounding errors, but for now
        # # let's assume that's not the case.
        # x_equality = (self.data[0] == other.get_data()[0]).all()
        # y_equality = (self.data[1] == other.get_data()[1]).all()
        # return x_equality and y_equality

    def apply_styles_from_dict(self, styler_values):
        if not isinstance(styler_values, dict):
            return

        for k, v in styler_values.items():
            setattr(self, k, v)

    def _get_color(self):
        return self._fake_it.get_color()

    def _set_color(self, value):
        self._fake_it.set_color(value)

    def _del_color(self):
        log.warning("color deleter is not implemented.")

    # noinspection PyPropertyDefinition
    color = property(
        fget=lambda self: self._get_color(),
        fset=lambda self, value: self._set_color(value),
        fdel=lambda self: self._del_color()
    )

    def _get_data(self):
        return self._fake_it.get_data()

    def _set_data(self, value):
        self._fake_it.set_data(value)

    def _del_data(self):
        log.warning(".data deleter hasn't been implemented.")

    # noinspection PyPropertyDefinition
    data = property(
        fget=lambda self: self._get_data(),
        fset=lambda self, value: self._set_data(value),
        fdel=lambda self: self._del_data()
    )

    # Overrides the WPLArtist.label setter.
    def _set_label(self, value):
        super()._set_label(value)
        self.plot.legend()

    def _get_marker(self):
        return self._fake_it.get_marker()

    def _set_marker(self, value):
        """
        Set the marker shape. To see a complete list of possible
        markers: https://matplotlib.org/api/markers_api.html#module-matplotlib.markers
        :param value: Marker shape value
        :type value: str, int
        """
        self._fake_it.set_marker(value)

    def _del_marker(self):
        self._fake_it.set_marker('')

    # noinspection PyPropertyDefinition
    marker = property(
        fget=lambda self: self._get_marker(),
        fset=lambda self, value: self._set_marker(value),
        fdel=lambda self: self._del_marker()
    )

    def _get_marker_color(self):
        if self.marker_face_color != self.marker_edge_color:
            return self.marker_face_color, self.marker_edge_color
        return self.marker_face_color

    def _set_marker_color(self, value):
        self._fake_it.set_markerfacecolor(value)
        self._fake_it.set_markeredgecolor(value)

    def _del_marker_color(self):
        log.warning("marker_color deleter hasn't been implemented.")

    # noinspection PyPropertyDefinition
    marker_color = property(
        fget=lambda self: self._get_marker_color(),
        fset=lambda self, value: self._set_marker_color(value),
        fdel=lambda self: self._del_marker_color()
    )

    def _get_marker_edge_color(self):
        return self._fake_it.get_markeredgecolor()

    def _set_marker_edge_color(self, value):
        self._fake_it.set_markeredgecolor(value)

    def _del_marker_edge_color(self):
        log.warning('marker_edge_color deleter is not implemented')

    # noinspection PyPropertyDefinition
    marker_edge_color = property(
        fget=lambda self: self._get_marker_edge_color(),
        fset=lambda self, value: self._set_marker_edge_color(value),
        fdel=lambda self: self._del_marker_edge_color()
    )

    def _get_marker_edge_width(self):
        return self._fake_it.get_markeredgewidth()

    def _set_marker_edge_width(self, value):
        self._fake_it.set_markeredgewidth(value)

    def _del_marker_edge_width(self):
        self._fake_it.set_markeredgewidth(0)

    # noinspection PyPropertyDefinition
    marker_edge_width = property(
        fget=lambda self: self._get_marker_edge_width(),
        fset=lambda self, value: self._set_marker_edge_width(value),
        fdel=lambda self: self._del_marker_edge_width()
    )

    def _get_marker_face_color(self):
        return self._fake_it.get_markerfacecolor()

    def _set_marker_face_color(self, value):
        self._fake_it.set_markerfacecolor(value)

    def _del_marker_face_color(self):
        log.warning('marker_face_color deleter is not implemented')

    # noinspection PyPropertyDefinition
    marker_face_color = property(
        fget=lambda self: self._get_marker_face_color(),
        fset=lambda self, value: self._set_marker_face_color(value),
        fdel=lambda self: self._del_marker_face_color()
    )

    def _get_marker_size(self):
        return self._fake_it.get_markersize()

    def _set_marker_size(self, value):
        self._fake_it.set_markersize(value)

    def _del_marker_size(self):
        self._fake_it.set_markersize(0)

    # noinspection PyPropertyDefinition
    marker_size = property(
        fget=lambda self: self._get_marker_size(),
        fset=lambda self, value: self._set_marker_size(value),
        fdel=lambda self: self._del_marker_size()
    )

    def _get_style(self):
        return self._fake_it.get_linestyle()

    def _set_style(self, value):
        self._fake_it.set_linestyle(value)

    def _del_style(self):
        self._fake_it.set_linestyle('')

    # noinspection PyPropertyDefinition
    style = property(
        fget=lambda self: self._get_style(),
        fset=lambda self, value: self._set_style(value),
        fdel=lambda self: self._del_style()
    )

    def _get_width(self):
        """
        :return: Width of the line
        :rtype: float
        """
        return self._fake_it.get_linewidth()

    def _set_width(self, value):
        """
        :param value: Width to set the line to.
        :type value: float, int
        """
        self._fake_it.set_linewidth(value)

    def _del_width(self):
        self._fake_it.set_linewidth(0)

    # noinspection PyPropertyDefinition
    width = property(
        fget=lambda self: self._get_width(),
        fset=lambda self, value: self._set_width(value),
        fdel=lambda self: self._del_width()
    )
