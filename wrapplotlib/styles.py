"""
Created: 4/15/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""


class BaseStyle:
    colors = [
        (0.0, 0.0, 1.0, 1.0),
        (0.0, 0.5, 0.0, 1.0),
        (1.0, 0.0, 0.0, 1.0),
        (0.0, 0.75, 0.75, 1.0),
        (0.75, 0.0, 0.75, 1.0),
        (0.75, 0.75, 0.0, 1.0),
        (0.0, 0.0, 0.0, 1.0),
    ]
    style_map = {
        'color': (0.0, 0.0, 0.0, 0.0),
        'line_width': 1,
        'marker': "D",
        'marker_edge_color': (0.0, 0.0, 0.0, 0.0),
        'marker_face_color': (1.0, 1.0, 1.0, 1.0),
        'style': '--'
    }

    def __call__(self, *args, **kwargs):
        return self.next()

    def __init__(self):
        self.count = 10
        self.color_index = 0
        self._color_count = len(self.colors)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        c = self.colors[self.color_index % self._color_count]
        self.color_index += 1

        i = (self.count % 10) / 10

        if self.color_index % self._color_count == 0:
            self.count += 1

        color = (c[0], c[1], c[2], c[3] - i)
        self.style_map['color'] = color
        self.style_map['marker_edge_color'] = color
        return self.style_map
