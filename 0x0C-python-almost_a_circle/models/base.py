#!/usr/bin/python3
""" doc """
from os import path

class Base:
    """ doc """
    __nb_objects = 0

    def __init__(self, id=None):
        """ doc """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
