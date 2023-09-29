#!/usr/bin/python3
"""
    a python module
"""

import sys
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    with urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
