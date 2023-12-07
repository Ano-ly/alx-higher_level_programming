#!/usr/bin/python3
"""This file contains only one function that writes to files"""


def write_file(filename="", text=""):
    """
    This function writes stuff to files.

    Args:
        filename: name of file to be written to
	text: stuff to be written

    """
    with open(filename, "w") as file:
        written_no = file.write(text)
        return (written_no)

