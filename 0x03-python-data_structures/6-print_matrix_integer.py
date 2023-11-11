#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("\n", end="")
    for list_ in matrix:
        len_ = len(list_)
        i = 0
        for int_ in list_:
            if i == len_ - 1:
                print("{:d}".format(int_), end="\n")
            else:
                print("{:d} ".format(int_), end="")
            i += 1
