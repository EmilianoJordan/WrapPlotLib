"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from wrapplotlib.text import WPLText

from ._mixins import FakeIt


class FigureTitle(FakeIt):

    def __init__(self, figure):

        self._figure = figure
        self._fake_it: WPLText = WPLText(self._figure.suptitle(''))

        self._title = self._fake_it

    def __str__(self):
        return str(self._title)


class AxisTitle(FigureTitle):
    pass
