#!/usr/bin/python3
"""This module contains the class square"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """This class defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """This function initialises the square instance"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This overrides the __str__ method"""

        return(f"[Square] ({self.id}) {self.x}/{self.y} - "+
	f"{self.width}")

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This function updates class attributes"""

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except (IndexError):
            pass
        if len(args) == 0:
            for item in kwargs:
                if item == "size":
                    self.size = kwargs[item]
                elif item == "id":
                    self.id = kwargs[item]
                elif item == "x":
                    self.x = kwargs[item]
                elif item == "y":
                    self.y = kwargs[item]
