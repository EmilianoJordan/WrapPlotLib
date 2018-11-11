"""

License: GNU General Public License v3.0
Created: 11/10/2018
Author: Emiliano Jordan, 
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
import pytest
from wrapplotlib._mixins import AttributeLookup
from matplotlib import pyplot
import pathlib, os


class WrapFig(AttributeLookup):

    def __init__(self):
        self._fig = pyplot.figure()
        self._cwd = pathlib.Path().cwd()

        self.lookup_objects.append(self._fig)
        self.lookup_objects.append(self._cwd)

        self.test_attr = 'return test attr'

        self._test_prop = None

    @property
    def test_prop(self):
        return self._test_prop

    @test_prop.setter
    def test_prop(self, val):
        self._test_prop = val

    @test_prop.deleter
    def test_prop(self):
        self._test_prop = None

    def test_method(self, string):
        return string


class SubWrapFig(WrapFig):

    def __init__(self):
        super().__init__()

        self._os = os

        self.lookup_objects.append(self._os)


class TestAttributeLookup:

    def test_single_inheritance(self):

        obj = WrapFig()

        assert obj.test_prop is None

        obj.test_prop = 'test'

        assert isinstance(obj.test_prop, str)
        assert obj.test_prop == 'test'

        del obj.test_prop

        assert obj.test_prop is None

        with pytest.raises(AttributeError):
            assert obj.does_not_exist

        try:
            assert obj.is_dir()
        except AttributeError:
            assert False

    def test_double_inheritance(self):

        obj = SubWrapFig()

        assert obj.test_prop is None

        obj.test_prop = 'test'

        assert isinstance(obj.test_prop, str)
        assert obj.test_prop == 'test'

        del obj.test_prop

        assert obj.test_prop is None

        with pytest.raises(AttributeError):
            assert obj.does_not_exist

        try:
            assert obj.is_dir()
        except AttributeError:
            assert False

        assert obj.getlogin() == os.getlogin()

        assert len(obj.lookup_objects) == 3

