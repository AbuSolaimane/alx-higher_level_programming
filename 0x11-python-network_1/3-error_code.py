#!/usr/bin/python3
"""
    a python module
"""
from sys import argv
from urllib.error import HTTPError
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as res:
            print(res.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
