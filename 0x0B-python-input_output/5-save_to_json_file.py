#!/usr/bin/python3
""" module """
import json


def save_to_json_file(my_obj, filename):
    """a function."""
    with open(filename, "w") as fil:
        json.dump(my_obj, fil)
