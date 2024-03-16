#!/usr/bin/python3
"""
This program file sends request to a URL and displays the error
code if it is greater than or equal to 400
"""


if __name__ == "__main__":
    import requests
    import sys
    args = sys.argv
    try:
        my_req = requests.get(args[1])
        my_req.raise_for_status()
        print(my_req.text)
    except requests.exceptions.HTTPError:
        if my_req.status_code >= 400:
            print("Error code: {}".format(my_req.status_code))
