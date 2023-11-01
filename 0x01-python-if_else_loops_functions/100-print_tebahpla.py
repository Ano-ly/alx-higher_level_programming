#!/usr/bin/python3
start = 122
while start >= 97:
    print("{}".format(chr(start) if start % 2 == 0 else chr(start-32)), end="")
    start -= 1
