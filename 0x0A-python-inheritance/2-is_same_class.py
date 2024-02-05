#!/usr/bin/python3
"""Exact same object."""

def is_same_class(obj, a_class):
    """see if obj is a subclasse of a_class
    Args:
        obj: is a class
        a_class: annother class
    Returns:
        True or False
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False
