#!/usr/bin/python3
"""is a module"""


def inherits_from(obj, a_class):
    """is a method"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
