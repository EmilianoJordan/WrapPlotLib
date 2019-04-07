"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from matplotlib import use
from matplotlib import pyplot as plt

from ._mixins import FakeIt
from .axes import BaseAxis
from .text import WPLText


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

        self._title = WPLText(self._figure.suptitle(''))

        self._axes = []

    def __iter__(self):
        return (a for a in self._axes)

    def add_subplot(self, *args, **kwargs):
        """
        https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_subplot

        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        axis = BaseAxis(self, self._figure.add_subplot(*args, **kwargs))
        self._axes.append(axis)
        return axis

    def close(self):
        plt.close(self._figure)

    def save(self, *args, **kwargs):
        return self._figure.savefig(*args, **kwargs)

    def show(self, close_on_user_input=False, no_close_blocking=False):
        if close_on_user_input:
            self._figure.show()
            plt.waitforbuttonpress()
        elif no_close_blocking:
            self._figure.show()
        else:
            plt.show()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title.set_text()

    @title.deleter
    def title(self):
        self._title.set_text('')


class SingleAxisFigure(BaseFigure):

    def __init__(self, backend="Qt5Agg", *args, **kwargs):
        super().__init__(backend, *args, **kwargs)

    @property
    def axis(self):
        return self._axes[0]

    # @axis.setter
