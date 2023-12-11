#!/usr/bin/python3
"""This function is for my experimentation on test driven development"""


def sub(a, b):
    """
    This function adds two numbers

    Args:
        a: first number
        b: second number
    """
    if (a < 0) or (b < 0):
        raise ValueError("None of the arguments should be negative")
    print("\n", (a + b) , "\t")


#if __name__ == "__main__":
#   import doctest
#    doctest.testfile("try_test.txt")
