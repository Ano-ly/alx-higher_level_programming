#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    new_list = []
    length = len(my_list)
    while i < length:
        if (my_list[i] % 2) == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        i += 1
    return (new_list)
