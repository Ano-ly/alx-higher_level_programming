#!/usr/bin/python3

def lookup(obj):
    """ Returns list of object methods and variables"""
    return (list(obj.__dict__))
