#!/usr/bin/python3
"""Contains the function lookup"""


def lookup(obj):
    """ Returns list of object methods and variables"""
    return (list(obj.__dict__))
