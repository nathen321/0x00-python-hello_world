#!/usr/bin/python3
"""prints the name of a anything"""

def say_my_name(first_name, last_name=""):
    """you goddamn right"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is', first_name, last_name)
