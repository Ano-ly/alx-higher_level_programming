#!/usr/bin/python3
"""A rectangle is defined below"""


class Rectangle:
    """This is a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialises rectangle

        Args:
            width (int): rectangle width
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Used to set or get width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        try:
            value - 1
        except TypeError:
            raise TypeError("width must be an integer")
        else:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Used to get or set height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        try:
            value - 1
        except TypeError:
            raise TypeError("height must be an integer")
        else:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")

    def area(self):
        """Returns the area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Returns the perimeter of rectangle"""
        if (self.width == 0) or (self.height == 0):
            return (0)
        else:
            return (2 * (self.width + self.height))
