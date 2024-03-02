#!/usr/bin/python3
"""This program file fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        resp_read = resp.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".
                format(type(resp_read), resp_read, resp_read.decode('utf-8')))

