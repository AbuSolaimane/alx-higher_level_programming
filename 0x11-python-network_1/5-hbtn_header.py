#!/usr/bin/python3
"""
    a python module
"""
from sys import argv
from requests import get


if __name__ == "__main__": 
    url = argv[1]
    res = get(url)
    print(res.headers.get("X-Request-Id"))
