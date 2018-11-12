"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from matplotlib.text import Text
from typing import Union, Optional


class FigureTitle:

    def __init__(self,
                 figure,
                 text: str = '',
                 x: Optional[float] = None,
                 y: Optional[float] = None,
                 horizontal_alignment: Optional[str] = None,
                 verticcal_alignment: Optional[str] = None,
                 font_size: Optional[Union[str, float]] = None,
                 font_weight: Optional[Union[str, float]] = None,
                 fontproperties: Optional[dict] = None,
                 **kwargs):
        """
        :param text:
        :type text:
        :param x:
        :type x:
        :param y:
        :type y:
        :param horizontal_alignment:
        :type horizontal_alignment:
        :param verticcal_alignment:
        :type verticcal_alignment:
        :param font_size:
        :type font_size:
        :param font_weight:
        :type font_weight:
        :param fontproperties:
        :type fontproperties:
        :param kwargs: The remaining kwargs can be any arguments
            from matplotlib's `text api <https://matplotlib.org/api/te\
            xt_api.html#matplotlib.text.Text>`_
        :type kwargs:
        """
        self._figure = figure
        self._title: Text = self(text, x, y, horizontal_alignment,
                                 verticcal_alignment, font_size, font_weight,
                                 fontproperties, **kwargs)

    def __getattr__(self, item):

        def interceptor(attr):

            def wrapper(*args, **kwargs):
                return attr(*args, **kwargs)

            return wrapper

        if item not in self._title.__dir__():
            raise AttributeError(
                f"'{self.__class__}' object has no attribute '{item}'"
            )

        item = getattr(self._title, item)

        if callable(item):
            return interceptor(item)

        return item

    def __call__(self,
                 text: str = '',
                 x: Optional[float] = None,
                 y: Optional[float] = None,
                 horizontal_alignment: Optional[str] = None,
                 verticcal_alignment: Optional[str] = None,
                 font_size: Optional[Union[str, float]] = None,
                 font_weight: Optional[Union[str, float]] = None,
                 fontproperties: Optional[dict] = None,
                 **kwargs):

        if x is not None:
            kwargs['x'] = x

        if y is not None:
            kwargs['y'] = y

        if horizontal_alignment is not None:
            kwargs['horizontalalignment'] = horizontal_alignment

        if verticcal_alignment is not None:
            kwargs['verticcalalignment'] = verticcal_alignment

        if font_size is not None:
            kwargs['fontsize'] = font_size

        if font_weight is not None:
            kwargs['weight'] = font_weight

        if fontproperties is not None:
            kwargs['fontproperties'] = fontproperties

        self._title = self._figure._fig.suptitle(text, **kwargs)

        return self._title

    def __str__(self):
        return self._title.get_text()

    def __dir__(self):
        return list((
            super(FigureTitle, self).__dir__()
            + self._title.__dir__()
        ))


class AxisTitle():
    pass
