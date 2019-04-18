"""
Created: 4/15/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""


class BaseStyle:
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
        return self.next()

    def __init__(self):
        self.color_index = 0
        self.marker_index = 0
        self._color_count = len(self.colors)
        self._marker_count = len(self.markers)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        self.style_map['color'] = self.colors[self.color_index % self._color_count]
        self.color_index += 1

        self.style_map['marker'] = self.markers[self.marker_index % self._marker_count]

        if self.color_index % self._color_count == 0:
            self.marker_index += 1

        return self.style_map
