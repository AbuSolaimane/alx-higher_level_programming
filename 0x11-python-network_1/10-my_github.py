#!/usr/bin/python3
"""
    a python module
"""
from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
