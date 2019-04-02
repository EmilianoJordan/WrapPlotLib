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
            self._fake_it = Text(text)
        elif isinstance(text, Text):
            self._fake_it = text
        else:
            raise AttributeError("WPLText expects a string or matplotlib.text.Text "
                                 "instance for initialization.")

        self._title = self._fake_it

    def __str__(self):
        self._title.get_text()