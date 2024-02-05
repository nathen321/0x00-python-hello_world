#!/usr/bin/python3
""" is_same_class """
def is_same_class(obj, a_class):
    """see if obj is a subclasse of a_class
    Args:
        obj: is a class
        a_class: annother class
    Returns:
        True or False
    """
    return type(obj) == a_class
