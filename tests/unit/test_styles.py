from wrapplotlib.styles import BaseLineStyle


def test_base_style_initialization():
    s = BaseLineStyle()

    # Both s and the call to s() should be iterable.
    assert iter(s())
    assert iter(s)


def test_base_style_output():
    s = BaseLineStyle()
    test_styles = {
        'color': (0.0, 0.0, 1.0, 1.0),
        'line_width': 1,
        'marker': "o",
    }
    styles = s()

    for key, val in test_styles.items():
        assert styles[key] == val