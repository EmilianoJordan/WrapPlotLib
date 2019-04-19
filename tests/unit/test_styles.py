"""
Created: 4/18/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from wrapplotlib.styles import BaseStyle


def test_base_style_initialization():
    s = BaseStyle()

    # Both s and the call to s() should be iterable.
    assert iter(s())
    assert iter(s)


def test_base_style_output():
    s = BaseStyle()
    test_styles = {
        'color': (0.0, 0.0, 1.0, 1.0),
        'line_width': 1,
        'marker': "o",
    }
    styles = s()

    for key, val in test_styles.items():
        assert styles[key] == val