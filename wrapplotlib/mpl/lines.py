# Created: 9/1/2019
# Author:  Emiliano Jordan,
# Project: WrapPlotLib
from matplotlib.lines import Line2D
from sejings import extract_sejings

from wrapplotlib.mpl.artist import WplArtist
from wrapplotlib.settings import settings


class WplLine2D(Line2D, WplArtist):

    @extract_sejings
    def __init__(
            self,
            xdata,
            ydata,

            linewidth=settings.lines.linewidth,
            linestyle=settings.lines.linestyle,
            color=settings.lines.color,
            marker=settings.lines.marker,
            markersize=settings.lines.markersize,
            markeredgewidth=settings.lines.markeredgewidth,
            markeredgecolor=settings.lines.markeredgecolor,
            markerfacecolor=settings.lines.markerfacecolor,
            markerfacecoloralt='none',
            fillstyle=settings.markers.fillstyle,
            antialiased=settings.lines.antialiased,
            dash_capstyle=settings.lines.dash_capstyle,
            solid_capstyle=settings.lines.solid_capstyle,
            dash_joinstyle=settings.lines.dash_joinstyle,
            solid_joinstyle=settings.lines.solid_joinstyle,
            pickradius=settings.lines.pickradius,
            drawstyle=settings.lines.drawstyle,
            markevery=settings.lines.markerevery,
            **kwargs
    ):
        super().__init__(
            xdata,
            ydata,
            linewidth=linewidth,
            linestyle=linestyle,
            color=color,
            marker=marker,
            markersize=markersize,
            markeredgewidth=markeredgewidth,
            markeredgecolor=markeredgecolor,
            markerfacecolor=markerfacecolor,
            markerfacecoloralt=markerfacecoloralt,
            fillstyle=fillstyle,
            antialiased=antialiased,
            dash_capstyle=dash_capstyle,
            solid_capstyle=solid_capstyle,
            dash_joinstyle=dash_joinstyle,
            solid_joinstyle=solid_joinstyle,
            pickradius=pickradius,
            drawstyle=drawstyle,
            markevery=markevery,
            **kwargs
        )

    def __str__(self):
        return 'Wpl' + super().__str__()
