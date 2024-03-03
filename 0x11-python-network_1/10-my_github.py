#!/usr/bin/python3
"""Obtains the id of a user from using
GitHub API and accepts the username and password
or authentication token as command line arguments."""


if __name__ == "__main__":
    import requests
    import sys
    args = sys.argv
    resp = requests.get("https://api.github.com/user", auth=(args[1], args[2]))
    print(resp)
