#!/usr/bin/python3
"""This module sends a letter supplied as an argument, in
a post request, to the url http://0.0.0.0:5000/search_user
and prints the JSON response in a certain format, or
other messages if the JSON response is invalid or empty.
"""


if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={"q": letter})
    try:
        j_dic = req.json()
        if j_dic == {}:
            print("No result")
        else:
            print("[{}] {}".format(j_dic['id'], j_dic['name']))
    except requests.exceptions.JSONDecodeError:
            print("Not a valid JSON")
