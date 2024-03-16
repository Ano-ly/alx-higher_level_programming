#!/usr/bin/python3

"""
This module takes in a url, sends a request
and handles a httperror if it occurs.
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import urllib.parse
    import sys

    args = sys.argv
    url_sup = args[1]

    try:
        with urllib.request.urlopen(url_sup) as in_resp:
            print(in_resp.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}". format(err.code))
