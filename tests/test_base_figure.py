"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
import pytest
import numpy as np
from matplotlib import pyplot as plt

import cv2


from wrapplotlib.figures import BaseFigure


class TestBaseFigure:

    fig_id = None

    @classmethod
    def setup_class(cls):

        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        cls.base_fig = BaseFigure()

        ax = cls.base_fig.add_subplot(1,1,1)

        ax.plot(t, s)

    @classmethod
    def teardown_class(cls):

        plt.close(cls.base_fig._fig)

        del cls.base_fig

    def test_setup(self):
        """
        I wasn't 100% sure of the setup and teardown methods
        so I wanted to test the test. Liiike, meta ma'an.
        :return:
        :rtype:
        """
        assert isinstance(self.base_fig, BaseFigure)

        self.fig_id = id(self.base_fig)

    def test_teardown(self):
        """
        Test the teardown method.

        :return:
        :rtype:
        """
        assert self.fig_id != id(self.base_fig)

