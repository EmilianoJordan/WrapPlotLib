"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from matplotlib import pyplot

from .titles import FigureTitle

class BaseFigure:

    def __init__(self, *args, **kwargs):

        self._fig = pyplot.figure(*args, **kwargs)
        self._title = FigureTitle(self)

    def __getattr__(self, item):

        def interceptor(attr):

            def wrapper(*args, **kwargs):

                return attr(*args, **kwargs)

            return wrapper

        if item not in self._fig.__dir__():

            raise AttributeError(
                f"'{self.__class__}' object has no attribute '{item}'"
            )

        item = getattr(self._fig, item)

        if callable(item):
            return interceptor(item)

        return item

    def __dir__(self):
        return list((
                super(BaseFigure, self).__dir__()
                + self._fig.__dir__()
        ))

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title(val)

    def close(self):
        pyplot.close(self._fig)

    def save(self, *args, **kwargs):
        return self._fig.savefig(*args, **kwargs)