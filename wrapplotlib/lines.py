from typing import Union

from matplotlib.lines import Line2D

from . import log
from .artists import WPLArtist


class WPL2DLine(WPLArtist):

    def __init__(self,
                 figure: 'BaseFigure',
                 plot: 'BasePlot',
                 style_dict: Union[dict, None],
                 line: Line2D):
        self.figure = figure
        self.plot = plot
        self._fake_it: Line2D = line

        self.style_dict = style_dict

    def __eq__(self, other: Union['WPL2DLine', Line2D]):
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
        self.plot.update_axis_limits()

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
        self._fake_it.set_markeredgecolor(self.marker_face_color)

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
        self._fake_it.set_markerfacecolor(self.marker_edge_color)

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

    def _get_style_dict(self):
        return {
            'alpha': self.alpha,
            'color': self.color,
            'marker': self.marker,
            'marker_edge_color': self.marker_edge_color,
            'marker_edge_width': self.marker_edge_width,
            'marker_face_color': self.marker_face_color,
            'marker_size': self.marker_size,
            'style': self.style,
            'visible': self.visible,
            'width': self.width,
        }

    def _set_style_dict(self, value):
        if not isinstance(value, dict):
            log.warning('style_dict must be a dictionary with keys'
                        'of attributes of wrapplotlib.lines.WPL2DLine'
                        'and values.')

        for k, v in value.items():
            setattr(self, k, v)

    def _del_style_dict(self):
        log.warning('style_dict deleter is not implemented')

    # noinspection PyPropertyDefinition
    style_dict = property(
        fget=lambda self: self._get_style_dict(),
        fset=lambda self, value: self._set_style_dict(value),
        fdel=lambda self: self._del_style_dict()
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
