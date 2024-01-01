#!/usr/bin/python3
"""This module contains a function that prints a square"""


def print_square(size):
    """
    This function prints a square

    Args:

        size: size of square

     """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for i in range(0, size):
            print("#", end="")
        print()
