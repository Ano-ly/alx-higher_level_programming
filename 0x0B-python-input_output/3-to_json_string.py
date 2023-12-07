#!/usr/bin/python3
"""This module contains only one function"""


def to_json_string(my_obj):
    """
    This function returns the json representation of an object.
    Args:
        my_obj: This is the object

    """
    import json
    json_str = json.dumps(my_obj)
    return (json_str)
