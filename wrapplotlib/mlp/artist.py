# Created: 8/31/2019
# Author:  Emiliano Jordan,
# Project: WrapPlotLib
from matplotlib.artist import Artist

from .. import settings

class WplArtist(Artist):

    def __int__(self, args):
        # noinspection PyUnresolvedReferences
        super().__int__()

        self._sketch = settings.path.sketch
        self._path_effects = settings.path.effects

    def _get_label(self):
        return self.get_label()

    def _set_label(self, value):
        self.set_label(value)

    def _del_label(self):
        self.set_label(None)

    # noinspection PyPropertyDefinition
    label = property(
        fget=lambda self: self._get_label(),
        fset=lambda self, value: self._set_label(value),
        fdel=lambda self: self._del_label()
    )

    def _get_visible(self):
        return self.get_visible()

    def _set_visible(self, value):
        self.set_visible(value)

    def _del_visible(self):
        self.set_visible(False)

    # noinspection PyPropertyDefinition
    visible = property(
        fget=lambda self: self._get_visible(),
        fset=lambda self, value: self._set_visible(value),
        fdel=lambda self: self._del_visible()
    )

    def _get_alpha(self):
        return self.get_alpha()

    def _set_alpha(self, value):
        self.set_alpha(value)

    def _del_alpha(self):
        self.set_alpha(0)

    # noinspection PyPropertyDefinition
    alpha = property(
        fget=lambda self: self._get_alpha(),
        fset=lambda self, value: self._set_alpha(value),
        fdel=lambda self: self._del_alpha()
    )