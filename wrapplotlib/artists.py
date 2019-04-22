"""
Created: 4/20/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from abc import ABCMeta
from matplotlib.artist import Artist

from ._mixins import FakeIt


class WPLArtist(FakeIt, metaclass=ABCMeta):
    """
    The WPLArtist class is never meant to be initialized itself.
    It provides some basic attributes to all classes that subclass the
    WPLArtist class. So far attributes that have been implemented are:

    .label
    .visible
    .alpha

    """
    _fake_it: Artist

    def __del__(self):
        try:
            self._fake_it.remove()
        except NotImplementedError:
            pass
        del self._fake_it

    def _get_label(self):
        return self._fake_it.get_label()

    def _set_label(self, value):
        self._fake_it.set_label(value)

    def _del_label(self):
        self._fake_it.set_label(None)

    # noinspection PyPropertyDefinition
    label = property(
        fget=lambda self: self._get_label(),
        fset=lambda self, value: self._set_label(value),
        fdel=lambda self: self._del_label()
    )

    def _get_visible(self):
        return self._fake_it.get_visible()

    def _set_visible(self, value):
        self._fake_it.set_visible(value)

    def _del_visible(self):
        self._fake_it.set_visible(False)

    # noinspection PyPropertyDefinition
    visible = property(
        fget=lambda self: self._get_visible(),
        fset=lambda self, value: self._set_visible(value),
        fdel=lambda self: self._del_visible()
    )

    def _get_alpha(self):
        return self._fake_it.get_alpha()

    def _set_alpha(self, value):
        self._fake_it.set_alpha(value)

    def _del_alpha(self):
        self._fake_it.set_alpha(0)

    # noinspection PyPropertyDefinition
    alpha = property(
        fget=lambda self: self._get_alpha(),
        fset=lambda self, value: self._set_alpha(value),
        fdel=lambda self: self._del_alpha()
    )