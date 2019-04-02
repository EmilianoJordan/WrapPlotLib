"""
Created: 4/2/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
class FakeIt:

    def __getattr__(self, item):

        def interceptor(attr):

            def wrapper(*args, **kwargs):

                return attr(*args, **kwargs)

            return wrapper

        if item not in self._fake_it.__dir__():

            raise AttributeError(
                f"'{self.__class__}' object has no attribute '{item}'"
            )

        item = getattr(self._fake_it, item)

        if callable(item):
            return interceptor(item)

        return item

    def __dir__(self):
        return list(set(
            list(self._fake_it.__dir__())
            + list(super().__dir__())
        ))