#!/usr/bin/python3
"""This module contains the rectangle class"""


from models.base import Base


class Rectangle(Base):
    """This class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This function initialises the class

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: a certain parameter
            y: yet another certain parameter

        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This function returns the area of the rectangle."""
        return (self.height * self.width)

    def display(self):
        """This function displays the rectange using hashtags"""
        for k in range(self.y):
            print("\n", end="")
        for i in range(self.height):
            for one in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("\n", end="")

    def __str__(self):
        """
        This function returns a formatted
        version of the printed rectangle
        """

        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - " +
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """This function updates class attributes"""

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except (IndexError):
            pass
        if len(args) == 0:
            for item in kwargs:
                if item == "width":
                    self.width = kwargs[item]
                elif item == "height":
                    self.height = kwargs[item]
                elif item == "id":
                    self.id = kwargs[item]
                elif item == "x":
                    self.x = kwargs[item]
                elif item == "y":
                    self.y = kwargs[item]

    def to_dictionary(self):
        """Returns a dictionary representation"""

        a_dict = {}
        a_dict["width"] = self.width
        a_dict["height"] = self.height
        a_dict["id"] = self.id
        a_dict["x"] = self.x
        a_dict["y"] = self.y
        return (a_dict)
