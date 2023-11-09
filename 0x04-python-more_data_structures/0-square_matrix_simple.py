#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = []
    for mat in matrix:
        mat_new = list(map(lambda x: x ** 2, mat))
        matrix_new.append(mat_new)
    return (matrix_new)
