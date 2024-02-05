#!/usr/bin/python3
""" is_same_class """
def inherits_from(obj, a_class):
    """see if obj is a subclasse
    Args:
        obj: is a class
        a_class: annother class
    Returns:
        True or False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
