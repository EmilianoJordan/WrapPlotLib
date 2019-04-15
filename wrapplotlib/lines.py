"""
Created: 4/10/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from typing import Union

from matplotlib.lines import Line2D

from ._mixins import FakeIt

class WPLLine2D(FakeIt):

    def __init__(self, line: Line2D):

        self._fake_it: Line2D = line

    def __eq__(self, other: Union['WPLLine2D', Line2D]):
        """
        The equality of two lines is based solely on the data
        that defines it.

        It may be possible to create conditions based on the axis it
        belongs to and the figure that that belongs to later.
        """
        # If the lengths of the data are not the same than we can exit.
        # Lines must have equal length x and y data so checking x length
        # is all that's necessary.
        if len(self.data[0]) != len(self.get_data()[0]):
            return False

        # Check the equality of each set of data. There may be a
        # tolerance problem here in rounding errors, but for now
        # let's assume that's not the case.
        x_equality = (self.data[0] == other.get_data()[0]).all()
        y_equality = (self.data[1] == other.get_data()[1]).all()
        return x_equality and y_equality

    @property
    def data(self):
        return self._fake_it.get_data()

    @data.setter
    def data(self, *value):
        self._fake_it.set_data(*value)

    @property
    def marker(self):
        return self._fake_it.get_marker()

    @marker.setter
    def marker(self, value):
        """
        Set the marker shape. To see a complete list of possible
        markers: https://matplotlib.org/api/markers_api.html#module-matplotlib.markers
        :param value: Marker shape value
        :type value: str, int
        """
        self._fake_it.set_marker(value)

    @marker.deleter
    def marker(self):
        self._fake_it.set_marker('')

    @property
    def marker_edge_color(self):
        return self._fake_it.get_markeredgecolor()

    @marker_edge_color.setter
    def marker_edge_color(self, value):
        self._fake_it.set_markeredgecolor(value)

    @marker_edge_color.deleter
    def marker_edge_color(self):
        pass

    @property
    def marker_edge_width(self):
        return self._fake_it.get_markeredgewidth()

    @marker_edge_width.setter
    def marker_edge_width(self, value):
        self._fake_it.set_markeredgewidth(value)

    @marker_edge_width.deleter
    def marker_edge_width(self):
        self._fake_it.set_markeredgewidth(0)

    @property
    def marker_face_color(self):
        return self._fake_it.get_markerfacecolor()

    @marker_face_color.setter
    def marker_face_color(self, value):
        self._fake_it.set_markerfacecolor(value)

    @marker_face_color.deleter
    def marker_face_color(self):
        pass

    @property
    def marker_size(self):
        return self._fake_it.get_markersize()

    @marker_size.setter
    def marker_size(self, value):
        self._fake_it.set_markersize(value)

    @marker_size.deleter
    def marker_size(self):
        self._fake_it.set_markersize(0)

    @property
    def style(self):
        return self._fake_it.get_linestyle()

    @style.setter
    def style(self, value):
        self._fake_it.set_linestyle(value)

    @style.deleter
    def style(self):
        self._fake_it.set_linestyle('')

    @property
    def width(self):
        """
        :return: Width of the line
        :rtype: float
        """
        return self._fake_it.get_linewidth()

    @width.setter
    def width(self, value):
        """
        :param value: Width to set the line to.
        :type value: float, int
        """
        self._fake_it.set_linewidth(value)

    @width.deleter
    def width(self):
        self._fake_it.set_linewidth(0)