#!/usr/bin/python3
"""this is a module."""
import json


def load_from_json_file(filename):
    """a function."""
    with open(filename) as fil:
        return json.load(fil)
