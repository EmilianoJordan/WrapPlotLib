"""
Created: 4/10/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from typing import Union

from ._mixins import FakeIt

from matplotlib.lines import Line2D

class WPLLine(FakeIt):

    def __init__(self, line: Line2D):

        self._fake_it = line

    def __eq__(self, other: Union['WPLLine', Line2D]):
        """
        The equality of two lines is based solely on the data
        that defines it.

        It may be possible to create conditions based on the axis it
        belongs to and the figure that that belongs to later.

        """
        # If the lengths of the data are not the same than we can exit.
        # Lines must have equal length x and y data so checking x length
        # is all that's necessary.
        if(len(self.data[0]) != len(self.get_data()[0])):
            return False

        # Check the equality of each set of data. There may be a
        # tolerance problem here in rounding errors, but for now
        # let's assume that's not the case.
        x_equality = (self.data[0] == other.get_data()[0]).all()
        y_equality = (self.data[1] == other.get_data()[1]).all()
        return x_equality and y_equality

    @property
    def data(self):
        return self._fake_it.get_data()

    @data.setter
    def data(self, *value):
        self._fake_it.set_data(*value)
