#!/usr/bin/python3
"""
This program file sends request to a URL and displays the value of
a variable in the http response header
"""


if __name__ == "__main__":
    import requests
    import sys
    args = sys.argv
    val_dic = {"email": args[2])
    my_req = requests.post(argv[1], param=val_dic)
    print(my_req.content)
