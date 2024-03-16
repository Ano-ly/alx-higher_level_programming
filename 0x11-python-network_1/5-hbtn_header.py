#!/usr/bin/python3
"""
This program file sends request to a URL and displays the value of
A variable in the http response header
"""


if __name__ == "__main__":
    import requests
    import sys
    args = sys.argv
    my_req = requests.get(args[1])
    val = my_req.headers.get('X-Request-Id')
    print(val)
