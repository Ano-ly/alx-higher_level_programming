#!/usr/bin/python3
"""Obtains the id of a user from using
GitHub API and accepts the username and password
or authentication token as command line arguments."""


if __name__ == "__main__":
    import requests
    import sys
    args = sys.argv
    url = "https://api.github.com/repos/" + str(args[1]) +\
          '/' + str(args[2]) + "/commits"
    resp = requests.get(url)
    resp_list = resp.json()
    times = 0
    for person in resp_list:
        if times == 10:
            break
        print("{}: {}".format(person['sha'],
              person['commit']['author']['name']))
        times += 1
    listt = resp.text.split(",")
