#!/usr/bin/python3
"""
    a python module
"""
from sys import argv
from requests import post


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    res = post(url, data=value)
    print(res.text)
