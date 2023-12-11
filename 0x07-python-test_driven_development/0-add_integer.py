#!/usr/bin/python3
""" This contains the add_integer function"""


def add_integer(a, b=98):
    """
    print(__import__("my_module").my_function.__doc__)
    This function adds two integers
    Args:
        a: first number
        b: second number

    """
    print(type(a))

    if type(a) != "int" and type(a) != "float":
        raise TypeError("a must be an integer")
    if type(b) != "int" and type(b) != "float":
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    sum = a + b
    return (sum)
