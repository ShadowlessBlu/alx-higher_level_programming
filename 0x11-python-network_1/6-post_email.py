#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    urll = sys.argv[1]

    requ = urllib.request.Request(urll)
    with urllib.request.urlopen(requ) as respo:
        print(dict(respo.headers).get("X-Request-Id"))
