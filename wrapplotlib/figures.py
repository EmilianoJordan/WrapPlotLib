"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from matplotlib import use
from matplotlib import pyplot as plt

from .titles import FigureTitle
from ._mixins import FakeIt

class BaseFigure(FakeIt):

    def __init__(self, backend="Qt5Agg", *args, **kwargs):

        # Trying to force matplotlib to use a predictable
        # backend. It's recommended to use Qt5, WrapPlotLib is tested
        # on Qt5.
        try:
            use(backend)
        except ImportError:
            if backend == "Qt5Agg":
                raise ImportError("Failed to import Qt5. WrapPlotLib "
                                  "recommends using Qt5 as a backend. "
                                  "Might try 'pip install PyQt5'")
            else:
                raise

        # _fake_it is an internal variable used by the FakeIt class
        self._fake_it = plt.figure(*args, **kwargs)
        # This is purely for code readability as _fake_it in this case is an instance of
        # matplotlib's Figure
        # https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html
        self._figure = self._fake_it

        self._title = FigureTitle(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title(val)

    def close(self):
        plt.close(self._figure)

    def save(self, *args, **kwargs):
        return self._figure.savefig(*args, **kwargs)


