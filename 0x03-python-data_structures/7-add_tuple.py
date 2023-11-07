#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    tuple_1 = (0, 0)
    if len_a == 1:
        tuple_1 = (tuple_a[0], 0)
    elif len_a == 2:
        tuple_1 = tuple_a
    elif len_a > 2:
        tuple_1 = (tuple_a[0], tuple_a[1])
    tuple_2 = (0, 0)
    if len_b == 1:
        tuple_2 = (tuple_b[0], 0)
    elif len_b == 2:
        tuple_2 = tuple_b
    elif len_b > 2:
        tuple_2 = (tuple_b[0], tuple_b[1])
    tuple_sum = (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
    return (tuple_sum)
