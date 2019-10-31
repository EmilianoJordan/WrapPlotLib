# Created: 9/15/2019
# Author:  Emiliano Jordan,
# Project: WrapPlotLib
from functools import wraps

from .wpl_settings import settings
from ._settings import Settings

0
def extract_settings(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        args = list(args)
        for i, item in enumerate(args):
            if isinstance(item, Settings) and hasattr(item, 'val'):
                args[i] = item.val

        for key, item in kwargs.items():
            if isinstance(item, Settings) and hasattr(item, 'val'):
                kwargs[key] = item.val

        return f(*args, **kwargs)

    return wrapper()
