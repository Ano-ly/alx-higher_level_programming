#!/usr/bin/python3
"""This module contains just one function"""


def save_to_json_file(my_obj, filename):
    """
    This function saves an object to a file
    Using json representation

    Args:
        my_obj: Object to be saved to file
        filename: Name of file to be saved to
    """
    import json
    with open(filename, "w") as file:
        json.dump(my_obj, file)
