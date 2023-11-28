#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
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
