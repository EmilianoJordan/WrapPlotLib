"""
Created: 6/10/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
from wrapplotlib.decorators import add_hooks


class A_1_1:

    def __init__(self):
        self.label = 'This is an object of A'

    @add_hooks
    def hooked_1_1(self, name, save_dir=None):
        return self, name, save_dir

    @hooked_1_1
    def pre_0_0(self):
        return self

    @hooked_1_1
    def pre_0_1(self, save_dir):
        return self, save_dir

    @hooked_1_1
    def pre_1_1(self, name, save_dir):
        return self, name, save_dir

    @hooked_1_1
    def post_0_0_0(self):
        return self

    @hooked_1_1
    def post_0_1_0(self, save_dir=...):
        return self, save_dir

    @hooked_1_1
    def post_1_0_0(self, name, ):
        return self, name

    @hooked_1_1
    def post_1_1_0(self, name, save_dir=...):
        return self, name, save_dir

    @hooked_1_1
    def post_0_0_1(self, wpl_hfrv=...):
        return self, wpl_hfrv

    @hooked_1_1
    def post_0_1_1(self, save_dir=..., wpl_hfrv=...):
        return self, save_dir, wpl_hfrv

    @hooked_1_1
    def post_1_0_1(self, name, wpl_hfrv):
        return self, name, wpl_hfrv

    @hooked_1_1
    def post_1_1_1(self, name, save_dir=..., wpl_hfrl=...):
        return self, name, save_dir, wpl_hfrl


class A_0_1:

    def __init__(self):
        self.label = 'This is an object of A'

    @add_hooks
    def hooked_0_1(self, save_dir=None):
        return self, save_dir

    @hooked_0_1
    def pre_0_0(self):
        return self

    @hooked_0_1
    def pre_0_1(self, save_dir):
        return self, save_dir

    @hooked_0_1
    def post_0_0_0(self):
        return self

    @hooked_0_1
    def post_0_1_0(self, save_dir=...):
        return self, save_dir

    @hooked_0_1
    def post_0_0_1(self, wpl_hfrv=...):
        return self, wpl_hfrv

    @hooked_0_1
    def post_0_1_1(self, save_dir=..., wpl_hfrv=...):
        return self, save_dir, wpl_hfrv

class A_1_0:

    def __init__(self):
        self.label = 'This is an object of A'

    @add_hooks
    def hooked_1_0(self, name):
        return self, name

    @hooked_1_0
    def pre_0_0(self):
        return self

    @hooked_1_0
    def post_0_0_0(self):
        return self

    @hooked_1_0
    def post_1_0_0(self, name):
        return self, name

    @hooked_1_0
    def post_0_0_1(self, wpl_hfrv=...):
        return self, wpl_hfrv

    @hooked_1_0
    def post_1_0_1(self, name, wpl_hfrv):
        return self, name, wpl_hfrv

class B:

    def __init__(self):
        self.label = 'This is an object of A'
