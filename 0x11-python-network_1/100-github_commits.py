#!/usr/bin/python3
"""
    a python module
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    res = get(url)
    commits = res.json()
    for i in range(10):
        print("{}: {}".format(
            commits[i].get("sha"),
            commits[i].get("commit").get("author").get("name")))
