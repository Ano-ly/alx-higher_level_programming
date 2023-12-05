#!/usr/bin/python3
""" This is Mylist"""


class MyList(list):
    """This is the class that inherits from list"""

    """This functions prints the list"""
    def print_sorted(self):
        sort_list = sorted(self)
        print(sort_list)
