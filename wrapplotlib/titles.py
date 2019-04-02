"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from typing import Union, Optional

from wrapplotlib.text import WPLText

from ._mixins import FakeIt

class FigureTitle:

    def __init__(self, figure):

        self._figure = figure
        self._fake_it: WPLText = WPLText(self._figure.suptitle(''))

        self._title = self._fake_it

    def __call__(self,
                 text: str = '',
                 x: Optional[float] = None,
                 y: Optional[float] = None,
                 horizontal_alignment: Optional[str] = None,
                 vertical_alignment: Optional[str] = None,
                 font_size: Optional[Union[str, float]] = None,
                 font_weight: Optional[Union[str, float]] = None,
                 font_properties: Optional[dict] = None,
                 **kwargs):

        if x is not None:
            kwargs['x'] = x

        if y is not None:
            kwargs['y'] = y

        if horizontal_alignment is not None:
            kwargs['horizontalalignment'] = horizontal_alignment

        if vertical_alignment is not None:
            kwargs['verticalalignment'] = vertical_alignment

        if font_size is not None:
            kwargs['fontsize'] = font_size

        if font_weight is not None:
            kwargs['fontweight'] = font_weight

        if font_properties is not None:
            kwargs['fontproperties'] = font_properties

        self._title: WPLText = WPLText(self._figure.suptitle(text, **kwargs))

        return self._title

    def __str__(self):
        return str(self._title)


class AxisTitle():
    pass
