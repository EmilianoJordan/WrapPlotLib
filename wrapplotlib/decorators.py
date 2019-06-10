"""
Created: 6/9/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""

from __future__ import print_function
from functools import wraps
import inspect


class _Signal(object):
    def __init__(self):

        self.slots = set()

    def __call__(self, *args, **kwargs):

        for obj, func in self.slots:
            args = list(args)  # Need mutable methods like pop()
            sig_args = []  # args list to build
            sig_kwargs = {}  # kwargs dict to build

            # args will have the 'self' argument. Remove it if the
            # called method object is the same as the signal object.
            if obj is not None and args[0] is obj:
                args.pop(0)

            for p in inspect.signature(func).parameters.values():
                if p.default is p.empty:  # Build args
                    sig_args.append(args.pop(0))
                elif p.name in kwargs:  # build kwargs
                    sig_kwargs[p.name] = kwargs[p.name]
                elif len(args) > 0:  # kwarg was defined positionally
                    sig_args.append(args.pop(0))

            func(*sig_args, **sig_kwargs)

    def clear(self):
        self.slots.clear()

    def connect(self, slot):

        obj = None if not inspect.ismethod(slot) else slot.__self__
        self.slots.add((obj, slot))

    def disconnect(self, slot):

        obj = None if not inspect.ismethod(slot) else slot.__self__

        self.slots.remove((obj, slot))


def add_hooks(func):
    """Decorator for adding a pre and post function call hook.

    :param func:
    :type func:
    :return:
    :rtype:
    """
    _pre = _Signal()
    _post = _Signal()

    @wraps(func)
    def wrapper(*args, **kwargs):

        _pre(*args, **kwargs)

        return_val = func(*args, **kwargs)

        _post(*args, **kwargs, func_return_val=return_val)

        return return_val

    wrapper.pre = _pre
    wrapper.post = _post

    return wrapper