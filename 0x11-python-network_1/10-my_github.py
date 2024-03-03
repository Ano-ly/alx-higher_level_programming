#!/usr/bin/python3
"""Obtains the id of a user from using
GitHub API and accepts the username and password
or authentication token as command line arguments."""


if __name__ == "__main__":
    import requests
    import sys
    args = sys.argv
    resp = requests.get("https://api.github.com/user", auth=(args[1], args[2]))
    if resp.status_code >= 400:
        print("None")
    else:
        my_str = resp.text
        my_list = my_str.split(',')
        for item in my_list:
            if "\"id\"" in item:
                item_dic = item.split(":")
                print(item_dic[1])
