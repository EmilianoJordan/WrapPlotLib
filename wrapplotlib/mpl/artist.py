# Created: 8/31/2019
# Author:  Emiliano Jordan,
# Project: WrapPlotLib
from matplotlib.artist import Artist

from .. import settings


class WplArtist(Artist):

    def __int__(self):
        # noinspection PyUnresolvedReferences
        super().__int__()

        self._sketch = settings.path.sketch
        self._path_effects = settings.path.effects

    # noinspection PyPropertyDefinition
    alpha = property(
        fget=lambda self: self.get_alpha(),
        fset=lambda self, value: self.set_alpha(value),
        fdel=lambda self: self.set_alpha(0)
    )
    
    # noinspection PyPropertyDefinition    
    animated = property(
        fget=lambda self: self.get_animated(),
        fset=lambda self, value: self.set_animated(value),
        fdel=lambda self: self.set_animated(False)
    )
    
    # noinspection PyPropertyDefinition    
    clip_box = property(
        fget=lambda self: self.get_clip_box(),
        fset=lambda self, value: self.set_clip_box(value),
    )

    # noinspection PyPropertyDefinition    
    clip_path = property(
        fget=lambda self: self.get_clip_path(),
        fset=lambda self, value: self.set_clip_path(value),
    )
    
    # noinspection PyPropertyDefinition
    contains = property(
        fget=lambda self: self.get_contains(),
        fset=lambda self, value: self.set_contains(value),
    )

    # noinspection PyPropertyDefinition    
    figure = property(
        fget=lambda self: self.get_figure(),
        fset=lambda self, value: self.set_figure(value),
    )
    
    # noinspection PyPropertyDefinition    
    gid = property(
        fget=lambda self: self.get_gid(),
        fset=lambda self, value: self.set_gid(value),
    )
    
    # noinspection PyPropertyDefinition
    label = property(
        fget=lambda self: self.get_label(),
        fset=lambda self, value: self.set_label(value),
        fdel=lambda self: self.set_label(None)
    )
    
    # noinspection PyPropertyDefinition
    picker = property(
        fget=lambda self: self.get_picker(),
        fset=lambda self, value: self.set_picker(value),
        fdel=lambda self: self.set_picker(None),
    )
    
    # noinspection PyPropertyDefinition
    transform = property(
        fget=lambda self: self.get_transform(),
        fset=lambda self, value: self.set_transform(value),
    )
    
    # noinspection PyPropertyDefinition
    visible = property(
        fget=lambda self: self.get_visible(),
        fset=lambda self, value: self.set_visible(value),
        fdel=lambda self: self.set_visible(False)
    )

    # noinspection PyPropertyDefinition
    url = property(
        fget=lambda self: self.get_url(),
        fset=lambda self, value: self.set_url(value),
    )

    # noinspection PyPropertyDefinition    
    snap = property(
        fget=lambda self: self.get_snap(),
        fset=lambda self, value: self.set_snap(value),
        fdel=lambda self: self.set_snap(None)
    )

    # noinspection PyPropertyDefinition    
    path_effects = property(
        fget=lambda self: self.get_path_effects(),
        fset=lambda self, value: self.set_path_effects(value),
    )
