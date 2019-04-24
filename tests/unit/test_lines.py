from wrapplotlib.lines import WPL2DLine


def test_line_dict(shock_single_figure):
    fig = shock_single_figure
    line: WPL2DLine = fig.plot.line

    # If the style dict generator creates an invalid k,v pair
    # This will raise an exception.
    line.style_dict = line.style_dict