#!/usr/bin/python3
"""This module contains the function matrix_divided"""


def matrix_divided(matrix, div):
    """
    This function divides all the values in a matrix
    by div.

    Args:

        matrix: matrix to be divided
        div: divisor

    """
    new_arr = []
    if matrix is None or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        for val in row:
            if type(val) is not int and type(val) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    mat_size = len(matrix[0])
    for row in matrix:
        if len(row) != mat_size:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        for val in row:
            new_row.append(round(val/div, 2))
        new_arr.append(new_row)
    return (new_arr)
