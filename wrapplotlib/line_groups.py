"""
Created: 4/21/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from typing import Union

from matplotlib.lines import Line2D

from .lines import WPL2DLine
from . import log


class WPL2DLineGroup:

    def __init__(self,
                 figure: 'BaseFigure',
                 plot: 'BasePlot',
                 style_dict: Union[dict, None],
                 line: Union[WPL2DLine, Line2D]):

        self.figure = figure
        self.plot = plot

        self._style_dict = style_dict

        if isinstance(line, Line2D):
            line = WPL2DLine(figure, plot, style_dict, line)

        self._lines = [line]
        self._label = line.label

    def _get_color(self):
        return self._style_dict.setdefault('color', self._lines[0].color)

    def _set_color(self, value):

        for l in self._lines:
            l.color = value

        self._style_dict['color'] = value

    def _del_color(self):
        log.warning("color deleter is not implemented.")

    # noinspection PyPropertyDefinition
    color = property(
        fget=lambda self: self._get_color(),
        fset=lambda self, value: self._set_color(value),
        fdel=lambda self: self._del_color()
    )

    def _get_label(self):
        self._label = self._lines[0].label
        return self._label

    def _set_label(self, value):
        self._lines[0].label = value
        self._label = value

    def _del_label(self):
        del self._lines[0].label
        self._label = self._lines[0].label

    # noinspection PyPropertyDefinition
    label = property(
        fget=lambda self: self._get_label(),
        fset=lambda self, value: self._set_label(value),
        fdel=lambda self: self._del_label()
    )

    def _get_marker(self):
        return self._style_dict.setdefault('marker', self._lines[0].marker)

    def _set_marker(self, value):
        for l in self._lines:
            l.marker = value

        self._style_dict['marker'] = value

    def _del_marker(self):
        for l in self._lines:
            del l.marker

        self._style_dict['marker'] = self._lines[0].marker

    # noinspection PyPropertyDefinition
    marker = property(
        fget=lambda self: self._get_marker(),
        fset=lambda self, value: self._set_marker(value),
        fdel=lambda self: self._del_marker()
    )

    def _get_marker_color(self):
        return self._style_dict.setdefault('marker_color', self._lines[0].marker_color)

    def _set_marker_color(self, value):
        for l in self._lines:
            l.marker_color = value

        self._style_dict['marker_color'] = value

    def _del_marker_color(self):
        log.warning("marker_color deleter hasn't been implemented.")

    # noinspection PyPropertyDefinition
    marker_color = property(
        fget=lambda self: self._get_marker_color(),
        fset=lambda self, value: self._set_marker_color(value),
        fdel=lambda self: self._del_marker_color()
    )

    def _get_marker_edge_color(self):
        return self._style_dict.setdefault('marker_edge_color', self._lines[0].marker_edge_color)

    def _set_marker_edge_color(self, value):
        for l in self._lines:
            l.marker_edge_color = value

        self._style_dict['marker_edge_color'] = value

    def _del_marker_edge_color(self):
        for l in self._lines:
            del l.marker_edge_color

        self._style_dict['marker_edge_color'] = self._lines[0].marker_edge_color

    # noinspection PyPropertyDefinition
    marker_edge_color = property(
        fget=lambda self: self._get_marker_edge_color(),
        fset=lambda self, value: self._set_marker_edge_color(value),
        fdel=lambda self: self._del_marker_edge_color()
    )

    def _get_marker_edge_width(self):
        return self._style_dict.setdefault('marker_edge_width', self._lines[0].marker_edge_width)

    def _set_marker_edge_width(self, value):
        for l in self._lines:
            l.marker_edge_width = value

        self._style_dict['marker_edge_width'] = value

    def _del_marker_edge_width(self):
        for l in self._lines:
            del l.marker_edge_width

        self._style_dict['marker_edge_width'] = self._lines[0].marker_edge_width

    # noinspection PyPropertyDefinition
    marker_edge_width = property(
        fget=lambda self: self._get_marker_edge_width(),
        fset=lambda self, value: self._set_marker_edge_width(value),
        fdel=lambda self: self._del_marker_edge_width()
    )

    def _get_marker_face_color(self):
        return self._style_dict.setdefault('marker_face_color', self._lines[0].marker_face_color)

    def _set_marker_face_color(self, value):
        for l in self._lines:
            l.marker_face_color = value

        self._style_dict['marker_face_color'] = value

    def _del_marker_face_color(self):
        for l in self._lines:
            del l.marker_face_color

        self._style_dict['marker_face_color'] = self._lines[0].marker_face_color

    # noinspection PyPropertyDefinition
    marker_face_color = property(
        fget=lambda self: self._get_marker_face_color(),
        fset=lambda self, value: self._set_marker_face_color(value),
        fdel=lambda self: self._del_marker_face_color()
    )

    def _get_marker_size(self):
        return self._style_dict.setdefault('marker_size', self._lines[0].marker_size)

    def _set_marker_size(self, value):
        for l in self._lines:
            l.marker_size = value

        self._style_dict['marker_size'] = value

    def _del_marker_size(self):
        for l in self._lines:
            del l.marker_size

        self._style_dict['marker_size'] = self._lines[0].marker_size

    # noinspection PyPropertyDefinition
    marker_size = property(
        fget=lambda self: self._get_marker_size(),
        fset=lambda self, value: self._set_marker_size(value),
        fdel=lambda self: self._del_marker_size()
    )

    def _get_style(self):
        return self._style_dict.setdefault('style', self._lines[0].style)

    def _set_style(self, value):
        for l in self._lines:
            l.style = value

        self._style_dict['style'] = value

    def _del_style(self):
        for l in self._lines:
            del l.style

        self._style_dict['style'] = self._lines[0].style

    # noinspection PyPropertyDefinition
    style = property(
        fget=lambda self: self._get_style(),
        fset=lambda self, value: self._set_style(value),
        fdel=lambda self: self._del_style()
    )

    def _get_style_dict(self):
        return self._style_dict

    def _set_style_dict(self, value):
        if not isinstance(value, dict):
            log.warning('style_dict must be a dictionary with keys'
                        'of attributes of wrapplotlib.lines.WPL2DLine'
                        'and values.')

        for l in self._lines:
            l.style_dict = value

        self._style_dict = value

    def _del_style_dict(self):
        log.warning('style_dict deleter is not implemented')

    # noinspection PyPropertyDefinition
    style_dict = property(
        fget=lambda self: self._get_style_dict(),
        fset=lambda self, value: self._set_style_dict(value),
        fdel=lambda self: self._del_style_dict()
    )

    def _get_width(self):
        return self._style_dict.setdefault('width', self._lines[0].width)

    def _set_width(self, value):
        for l in self._lines:
            l.width = value

        self._style_dict['width'] = value

    def _del_width(self):
        for l in self._lines:
            del l.width

        self._style_dict['width'] = self._lines[0].width

    # noinspection PyPropertyDefinition
    width = property(
        fget=lambda self: self._get_width(),
        fset=lambda self, value: self._set_width(value),
        fdel=lambda self: self._del_width()
    )
