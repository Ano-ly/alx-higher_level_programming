#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_total = 0
    n = 0
    if not my_list:
        return (0)
    for tup in my_list:
        sum_total += tup[0] * tup[1]
        n += tup[1]
    return (sum_total/n)
