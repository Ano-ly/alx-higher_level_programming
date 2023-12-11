#!/usr/bin/python3
"""This module contains the base class"""


class Base:
    """This is the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the initialisation function."""

        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to their json string representation"""

        import json
        if list_dictionaries is not None and len(list_dictionaries) != 0:
            return (json.dumps(list_dictionaries))
        else:
            return ("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """
	This function writes the json representation of
	 a list of instances of a class to a file
	"""
        with open (f"{cls.__name__}.json", "w") as open_file:
            new_list = []
            for i in list_objs:
                that_dic = i.to_dictionary()
                new_list.append(that_dic)
            json_str = cls.to_json_string(new_list)
            open_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
	This function returns the json representation of a list back to its
	original form

	"""

        import json
        new_list = json.loads(json_string)
        return (new_list)
