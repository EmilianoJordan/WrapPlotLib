from typing import Union

from matplotlib import use, get_backend
from matplotlib import pyplot as plt

from .artists import WPLArtist
from .plots import BasePlot, BaseGroupPlot, BaseLinePlot
from .styles import BaseLineStyle
from .text import WPLText


class BaseFigure(WPLArtist):

    def __init__(self, backend='Qt5Agg', *args, **kwargs):
        """

        :param backend: One of matplotlib's backends.
        This defaults to QtAgg as I've noticed fewer rendering
        errors vs KtAgg in terms of spacing etc.
        :type backend: str
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        """
        if backend is not None:
            use(backend, force=True)

        # _fake_it is an internal variable used by the FakeIt class
        self._fake_it = plt.figure(*args, **kwargs)

        self.__class__.title = WPLText(self._fake_it.suptitle('', size='xx-large'))

        # Need to keep track of plots. Only WPL Plot classes should be
        # added to this list.
        self._plots = []

        # See explanation in .show() method for _show property.
        self._shown = False

    def __iter__(self):
        return (a for a in self._plots)

    def __getitem__(self, item):
        for p in self._plots:
            if item == p.label:
                return p

    def add_subplot(self,
                    *args,
                    plot_type = BaseLinePlot,
                    styler=BaseLineStyle,
                    **kwargs):
        """
        https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_subplot
        :param args:
        :type args:
        :param plot_type:
        :type plot_type:
        :param styler:
        :type styler:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        axis = plot_type(self, self._fake_it.add_subplot(*args, **kwargs), styler=styler)
        self._plots.append(axis)
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


class SinglePlotFigure(BaseFigure):

    def __init__(self, backend="Qt5Agg", *args, **kwargs):
        super().__init__(backend, *args, **kwargs)

        self.add_subplot(1, 1, 1)

    @property
    def plot(self):
        return self._plots[-1]


class SingleGroupPlotFigure(BaseFigure):

    def __init__(self, backend="Qt5Agg", *args, **kwargs):
        super().__init__(backend, *args, **kwargs)

        self.add_subplot(1, 1, 1)

    @property
    def plot(self):
        return self._plots[-1]

    def add_subplot(self,
                    *args,
                    plot_type=BaseGroupPlot,
                    styler=BaseLineStyle,
                    **kwargs):
        return super(SingleGroupPlotFigure, self).add_subplot(
            *args,
            plot_type=BaseGroupPlot,
            styler=BaseLineStyle,
            **kwargs
        )
