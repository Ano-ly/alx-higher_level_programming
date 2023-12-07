#!/usr/bin/python3
"""This module contains only one function."""


def from_json_string(my_str):
    """
    This function returns an object from a json rep

    Args:
        my_str: string to be converted to object
    """
    import json
    return (json.loads(my_str))
