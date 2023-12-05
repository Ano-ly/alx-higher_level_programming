#!/usr/bin/python3
"""This module contains only one function"""


def is_same_class(obj, a_class):
    """This function checks if an object is instance of a class

    Args:
        obj: object involved
        a_class: class involved
    """
    return (type(obj) is a_class)
