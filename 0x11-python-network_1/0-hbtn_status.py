#!/usr/bin/python3
"""
    a python module
"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as res:
        body = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
