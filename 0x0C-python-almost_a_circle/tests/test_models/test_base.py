#!/usr/bin/python3
"""This is a unittest module"""


import unittest


from models.base import Base

class Test_base(unittest.TestCase):
    """This class tests the Base class"""

    def setUp(self):
        """Sets up the enviroment for testing"""

        self.base_one = Base()
        self.base_two = Base()
        self.base_three = Base()
        self.base_four = Base(23)

    def test_default_id_value(self):
        """Tests the default values of id"""

        self.assertEqual(self.base_three.id, 3)

    def test_spec_id_value(self):
        """Tests the specified values of id"""

        self.assertEqual(self.base_four.id, 23)

    def test_nb_objects_default(self):
        """Tests the default value of nb_objects"""

        self.assertEqual(Base.nb_objects, 0)

if __name__ == "__main__":
    unittest.main()
