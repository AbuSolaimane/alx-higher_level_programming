#!/usr/bin/python3
"""this is module"""


def write_file(filename="", text=""):
    """function"""
    with open(filename, "w", encoding="utf-8") as fil:
        return fil.write(text)
