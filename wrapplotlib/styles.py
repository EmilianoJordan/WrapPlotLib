"""
Created: 4/15/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from abc import ABCMeta, abstractmethod


class StyleMeta(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self):
        """
        The __call__ method should return the next set of styles in a
        dict. No parameters are passed into __call__. The
        __call__ and __next__ functions should return the same values
        and maintain the same internal state after being called.

        :return: Return a dict where the keys are attributes from
        wrapplotlib.lines.WPL2DLine and values are valid for the
        associated attribute.
        :rtype: dict
        """
        pass

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        """
        The __next__ method should return the next set of styles in a
        dict. No parameters are passed into __next__. The
        __call__ and __next__ functions should return the same values
        and maintain the same internal state after being called.

        :return: Return a dict where the keys are attributes from
        wrapplotlib.lines.WPL2DLine and values are valid for the
        associated attribute.
        :rtype: dict
        """

    @abstractmethod
    def reset(self):
        """
        The reset method should reset the internal state so that the
        __next__ and __call__ methods being returning values from the
        first value on.

        This method is used when redrawing plots. So it's important
        for this to be true.
        :return:
        :rtype:
        """
        pass


class BaseStyle(StyleMeta):
    """
    I believe BaseStyle is a perfect chance to learn metaclasses...
    But ABCs confuse me. Need to learn more about those.
    """
    colors = (
        (0.0, 0.0, 1.0, 1.0),
        (0.0, 0.5, 0.0, 1.0),
        (1.0, 0.0, 0.0, 1.0),
        (0.0, 0.75, 0.75, 1.0),
        (0.75, 0.0, 0.75, 1.0),
        (0.75, 0.75, 0.0, 1.0),
        (0.0, 0.0, 0.0, 1.0),
    )
    markers = (
        "o",
        "D",
        ">",
        "s",
        "^",
        "+",
        "<",
        "*",
        "v",
        "X",
    )
    style_map = {
        'color': (0.0, 0.0, 0.0, 0.0),
        'line_width': 1,
        'marker': "D",
        # 'marker_edge_color': (0.0, 0.0, 0.0, 0.0),
        # 'marker_face_color': (1.0, 1.0, 1.0, 1.0),
        # 'style': '--'
    }

    def __call__(self, *args, **kwargs):
        return self._next()

    def __init__(self):
        self.color_index = 0
        self.marker_index = 0
        self._color_count = len(self.colors)
        self._marker_count = len(self.markers)

    def __next__(self):
        return self._next()

    def _next(self):
        self.style_map['color'] = self.colors[self.color_index % self._color_count]
        self.color_index += 1

        self.style_map['marker'] = self.markers[self.marker_index % self._marker_count]
        if self.color_index % self._color_count == 0:
            self.marker_index += 1

        return self.style_map

    def reset(self):
        self.color_index = 0
        self.marker_index = 0
