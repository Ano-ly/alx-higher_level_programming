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
        my_req = requests.get(argv[1])
    except HTTPError as err:
        if my_req.status_code >= 400:
            print("Error code: {}".format(my_req.status_code))
