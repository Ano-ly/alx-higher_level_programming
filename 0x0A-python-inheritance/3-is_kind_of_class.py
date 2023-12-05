#!/usr/bin/python3
"""This module contains only one function"""


def is_kind_of_class(obj, a_class):
    """This function checks if an object is instance of a class

    Args:
        obj: object involved
        a_class: class involved
    """
    return (isinstance(obj, a_class))
