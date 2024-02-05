#!/usr/bin/python3
"""function that returns the list of available attributes"""

def lookup(obj):
    """returns the list of available attributes and methods of an object.
    Args:
        obj: is a class
    Returns:
        list: of attributes
    """

    return dir(obj)
