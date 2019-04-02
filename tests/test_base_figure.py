"""

License: GNU General Public License v3.0
Created: 11/11/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
import matplotlib.pyplot as plt

from wrapplotlib.figures import BaseFigure


def test_basic_initialization(shock_data):
    fig = BaseFigure()
    a = fig.add_subplot(1, 1, 1)
    fig.title = "Shock Data"
    a.plot(shock_data.time, shock_data.acceleration)
    a.set_title("Basic Shock")
    plt.show()

def test_dir():
    fig = BaseFigure()
    assert isinstance(fig.__dir__(), list)

