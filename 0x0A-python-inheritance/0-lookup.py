#!/usr/bin/python3
"""  returns: list of available attributes
and methods of an object
"""


def lookup(obj):
    """returns: list of available attributes"""
    return dir(obj)
