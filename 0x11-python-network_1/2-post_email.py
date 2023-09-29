#!/usr/bin/python3
"""
    a python module
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")
    req = Request(url, data)
    with urlopen(req) as res:
        print(res.read().decode("utf-8"))
