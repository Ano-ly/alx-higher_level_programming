#!/usr/bin/python3
"""This document contains a class Square"""


class Square:
    """This is a class Square"""
    def __init__(self, size=0):
        """
        This function initialises the square

        Args -
            size: size to be initialised with
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This function computes the area of the square"""

        return (self.__size ** 2)
