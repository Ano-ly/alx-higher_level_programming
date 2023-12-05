#!/usr/bin/python3
"""This module contains only one function"""


def inherits_from(obj, a_class):
    """This function checks if an object is instance of a class or other

    Args:
        obj: object involved
        a_class: class involved
    """
    if (type(obj) is a_class) or (isinstance(obj, a_class)):
        return True
    if (type(obj) is not a_class):
        return False
