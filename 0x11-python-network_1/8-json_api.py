#!/usr/bin/python3
"""
    a python module
"""
from sys import argv
from requests import post


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}

    res = post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
