#!/usr/bin/python3
"""This contains a function that prints a textfile"""


def read_file(filename=""):
    """
    This function reads a file

    Args:
        filename: name of file to be read
    """

    with open(filename, "r") as file:
        readd = file.read()
        print(readd, end="")
