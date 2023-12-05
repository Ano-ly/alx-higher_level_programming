#!/usr/bin/python3

"""This contains one class"""


class BaseGeometry:
    """This is a basic class"""

    def area(self):
        """ Raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value

        Args:
            name: name of value
            value: the value itself

        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
