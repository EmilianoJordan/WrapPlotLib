# Created: 8/31/2019
# Author:  Emiliano Jordan,
# Project: WrapPlotLib
from matplotlib.figure import Figure

from .. import settings
from .artist import WplArtist
from ..utils import extract_settings

class WplFigure(Figure, WplArtist):

    @extract_settings
    def __init__(self,
                 figsize=settings.figure.figsize,
                 dpi=settings.figure.dpi,
                 facecolor=settings.figure.facecolor,
                 edgecolor=settings.figure.edgecolor,
                 linewidth=0.0,  # the default linewidth of the frame
                 frameon=None,  # whether or not to draw the figure frame
                 subplotpars=None,  # default to rc
                 tight_layout=None,  # default to rc figure.autolayout
                 constrained_layout=None,
                 ):
        pass