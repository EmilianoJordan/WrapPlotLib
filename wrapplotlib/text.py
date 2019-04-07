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

    def __init__(self, text: Union[str, Text] = ''):

        if isinstance(text, str):
            self._fake_it = Text(text=text)
        elif isinstance(text, Text):
            self._fake_it = text
        else:
            raise AttributeError("WPLText expects a string or matplotlib.text.Text "
                                 "instance for initialization.")

        self._text = self._fake_it

    def __str__(self):
        return self._text.get_text()

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
    def size(self):
        return self._fake_it.get_fontsize()

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._fake_it.set_fontsize(value)
        if not isinstance(value, str):
            raise TypeError('Size must be a integer size or a str.')
        if not value in ['xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']:
            raise ValueError("Valid sizes are 'xx-small', 'x-small', 'small', "
                             "'medium', 'large', 'x-large', 'xx-large'")
        self._fake_it.set_fontsize(value)
        self._fake_it.draw()