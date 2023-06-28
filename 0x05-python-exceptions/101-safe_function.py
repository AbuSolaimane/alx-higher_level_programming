#!/usr/bin/python3
from __future__ import print_function
from sys import stderr
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
        return (None)
    else:
        return (result)
