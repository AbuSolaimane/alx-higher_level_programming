#!/usr/bin/python3
"""
    a python module
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = argv[1]
    res = get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
