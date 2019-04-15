"""
Created: 3/21/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from typing import Union

from matplotlib.text import Text

from ._mixins import FakeIt


class WPLText(FakeIt):
    """
    WrapPlotLib's Version of matplotlib.text.Text

    https://matplotlib.org/api/text_api.html#matplotlib.text.Text
    """
    def __init__(self, text: Union[str, Text] = ''):

        if isinstance(text, str):
            self._fake_it = Text(text=text)
        elif isinstance(text, Text):
            self._fake_it = text
        else:
            raise AttributeError("WPLText expects a string or matplotlib.text.Text "
                                 "instance for initialization.")

        # @TODO consider doing a defaults dict for a fall back for deleting things like size.

    def __get__(self, instance, owner):
        self._fake_it.get_text()

    def __set__(self, instance, value):
        self._fake_it.set_text(value)

    def __str__(self):
        return self._fake_it.get_text()

    @property
    def size(self):
        return self._fake_it.get_fontsize()

    @size.setter
    def size(self, value):
        """
        Sets the font-size of the text.

        Valid values are an integer for
        :param value: Size to set the font to. Valid values are:
        Integer (for representation in points), 'xx-small', 'x-small',
        'small', 'medium', 'large', 'x-large', 'xx-large'
        :type value: int, str
        """
        if isinstance(value, int):
            self._fake_it.set_fontsize(value)
            return
        if not isinstance(value, str):
            raise TypeError('Size must be a integer size or a str.')
        if value not in ['xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']:
            raise ValueError("Size is invalid. Valid font size are 'xx-small', 'x-small', "
                             "'small', 'medium', 'large', 'x-large', 'xx-large'")
        self._fake_it.set_fontsize(value)

    @property
    def text(self):
        return self._fake_it.get_text()

    @text.setter
    def text(self, value):
        self._fake_it.set_text(value)

    @text.deleter
    def text(self):
        self._fake_it.set_text('')

    @property
    def position(self):
        return self._fake_it.get_position()

    @position.setter
    def position(self, value):
        self._fake_it.set_position(value)

    @position.deleter
    def position(self):
        pass

    @property
    def x(self):
        return self._fake_it.get_position()[0]

    @x.setter
    def x(self, value):
        pos = self._fake_it.get_position()
        self._fake_it.set_position((value, pos[1]))

    @x.deleter
    def x(self):
        pass

    @property
    def y(self):
        return self._fake_it.get_position()[1]

    @y.setter
    def y(self, value):
        pos = self._fake_it.get_position()
        self._fake_it.set_position((pos[0], value))

    @y.deleter
    def y(self):
        pass