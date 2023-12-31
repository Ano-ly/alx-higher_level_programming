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
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This function computes the area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """This function prints a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for i in range(0, self.__size):
                    print("#", end="")
                print()
