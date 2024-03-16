#!/usr/bin/python3
"""
This program file fetches https://alx-intranet.hbtn.io/statu and displays
the value of a variable found under the response.
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        print(resp.getheader('X-Request-Id'))
