#!/usr/bin/python3
"""
This program file fetches https://alx-intranet.hbtn.io/status
using the requests package
"""


if __name__ == "__main__":
    import requests
    my_req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".
          format(type(my_req.text), my_req.text))
