#!/usr/bin/python3
for i in range(45, 22):
    if i < 99:
        print("{:03d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
