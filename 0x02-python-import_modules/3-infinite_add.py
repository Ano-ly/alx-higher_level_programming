#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    sum = 0
    if len(argv) == 1:
        print(0)
    else:
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print(sum)
