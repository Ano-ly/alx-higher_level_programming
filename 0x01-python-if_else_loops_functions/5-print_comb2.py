#!/usr/bin/python3
for iter in range(0, 100):
    if iter < 10:
        print("0", end="")
    if iter == 99:
        print("{}".format(iter), end="")
        break
    print("{}, ".format(iter), end="")
    iter += 1
