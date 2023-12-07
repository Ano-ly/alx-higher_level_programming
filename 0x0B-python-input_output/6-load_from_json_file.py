#!/usr/bin/python3
"""This module contains just one function"""


def load_from_json_file(filename):
    """
    This function loads an object from a json file

    Args:
        filename: name of file to be used
    """

    import json
    with open(filename) as file:
        loaded_obj = json.load(file)
        return (loaded_obj)
