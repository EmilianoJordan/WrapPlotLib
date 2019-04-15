"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from matplotlib import use, get_backend
from matplotlib import pyplot as plt

from ._mixins import FakeIt
from .axes import BaseAxis
from .text import WPLText


class BaseFigure(FakeIt):

    def __init__(self, backend='QtAgg', *args, **kwargs):

        if backend is not None:
            use(backend, force=True)
        print(get_backend())
        # _fake_it is an internal variable used by the FakeIt class
        self._fake_it = plt.figure(*args, **kwargs)

        self.title = WPLText(self._fake_it.suptitle(''))

        # Need to keep track of axes. Only WPL Axis classes should be
        # added to this list.
        self._axes = []

        # See explanation in .show() method for _show property.
        self._shown = False

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
        axis = BaseAxis(self, self._fake_it.add_subplot(*args, **kwargs))
        self._axes.append(axis)
        return axis

    def close(self):
        plt.close(self._fake_it)

    def save(self, *args, **kwargs):
        return self._fake_it.savefig(*args, **kwargs)

    def show(self, close_on_user_input=False):

        if close_on_user_input:
            self._fake_it.show()
            plt.waitforbuttonpress()
            return

        '''
        There are some differences with how ktinker and Qt5 perform 
        multiple show() calls. For the most consistent functionality 
        it is best to use pyplot.show() for the first call amongst 
        both backends. For the second call Qt5Agg only works if
        Figure.show() is used.
        '''
        if self._shown and get_backend() == 'Qt5Agg':
            self._fake_it.show()
            return

        plt.show()

        if get_backend() == 'Qt5Agg':
            self._shown = True


class SingleAxisFigure(BaseFigure):

    def __init__(self, backend="Qt5Agg", *args, **kwargs):
        super().__init__(backend, *args, **kwargs)

        self.add_subplot(1,1,1)

    @property
    def axis(self):
        return self._axes[0]

    # @axis.setter
