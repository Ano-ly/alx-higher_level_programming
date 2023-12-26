#!/usr/bin/python3
"""This document contains a class Square"""


class Square:
    """This is a class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        This function initialises the square

        Args -
            size: size to be initialised with
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if (type(value) is not tuple) or (len(value) != 2):
            raise ValueError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int) or (type(value[1]) is not int):
            raise ValueError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) or (value[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This function computes the area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """This function prints a square"""
        if self.__size == 0:
            print()
        else:
            for y in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for i in range(0, self.__size):
                    print("#", end="")
                print()
