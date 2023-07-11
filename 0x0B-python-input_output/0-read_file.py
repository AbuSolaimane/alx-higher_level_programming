#!/usr/bin/python3
"""this is module"""


def read_file(filename=""):
    """function"""
    with open(filename, encoding="utf-8") as fil:
        print(fil.read(), end="")
