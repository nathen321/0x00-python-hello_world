#!/usr/bin/python3
"""
the base classe of futer project
"""
from os import path

class Base:
    """
    this class initialse the id attribue of futer class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        this module is used to initalise the id attribu of futer child class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
