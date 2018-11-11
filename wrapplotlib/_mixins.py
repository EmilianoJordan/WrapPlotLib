"""

License: GNU General Public License v3.0
Created: 11/10/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""


class AttributeLookup:

    def __init__(self):
        self.lookup_objects = []

    def __getattr__(self, item):

        def interceptor(attr):

            def wrapper(*args, **kwargs):

                return attr(*args, **kwargs)

            return wrapper

        for obj in self.lookup_objects:

            if item in obj.__dir__():
                break

        else:

            raise AttributeError(
                f"'{self.__class__}' object has no attribute '{item}'"
            )

        item = getattr(obj, item)

        if callable(item):
            return interceptor(item)

        return item
