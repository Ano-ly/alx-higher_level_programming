#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            print("\n", end="")
            return (i)
        except ValueError:
            i += 1
            continue
        else:
            i += 1
            continue
    print("\n", end="")
    return (i)
