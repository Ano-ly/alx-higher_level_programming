#!/usr/bin/python3

"""
This module takes in a url and email, sends a request 
and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    args = sys.argv
    url_sup = args[1]
    my_values = {'email': args[2]}

    my_data = urllib.parse.urlencode(my_values)
    my_data = my_data.encode('ascii')
    message = urllib.request.Request(url_sup, my_data)
    with urllib.request.urlopen(message) as in_resp:
        print(in_resp.decode('utf-8'))
