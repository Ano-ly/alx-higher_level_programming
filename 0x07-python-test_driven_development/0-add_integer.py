#!/usr/bin/python3
""" This contains the add_integer function"""


def add_integer(a, b=98):
    """
    This function adds two integers
    Args:
        a: first number
        b: second number

    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    sum = a + b
    return (sum)
