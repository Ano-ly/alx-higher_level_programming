#!/usr/bin/python3
"""This file contains only one function that appends strings to files"""


def append_write(filename="", text=""):
    """
    This function appends stuff to files.

    Args:
        filename: name of file to be written to
        text: stuff to be appended

    """
    try:
        open(filename)
    except FileNotFoundError:
        with open(filename, "w") as file:
            written_no = file.write(text)
            return (written_no)
    else:
        with open(filename, "a") as file:
            written_no = file.write(text)
            return (written_no)
