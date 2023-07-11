#!/usr/bin/python3
"""is a module"""


class MyInt(int):
    """is a class"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
