#!/usr/bin/python3
iter = 0
while iter < 100:
    if iter < 10:
        print("0", end="")
    if iter == 99:
        print(f"{iter}")
        break
    print(f"{iter}, ", end="")
    iter += 1
