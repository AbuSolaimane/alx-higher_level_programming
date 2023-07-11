#!/usr/bin/python3
"""is a module"""


def add_attribute(obj, att, value):
    """is a method"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
