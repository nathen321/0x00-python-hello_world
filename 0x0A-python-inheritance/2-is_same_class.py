#!/usr/bin/python3
"""Exact same object."""

def is_same_class(obj, a_class):
    """returns the list of available attributes and methods of an object.
    Args:
        obj: is a class
    Returns:
        list: of attributes
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False
