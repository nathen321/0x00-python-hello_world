#!/usr/bin/python3
"""

Rectangle that does nothing

"""


class Rectangle:
    """ it's a rectangle pls work """

    def __init__(self, width=0, height=0):
        """ initaisation """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        
        self.height = height
        self.width = width

    @property
    def width(self):
        """return the W"""
        return self.__width

    @width.setter
    def width(self, value):
        """sette de W"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """return the H"""
        return self.__height

    @height.setter
    def height(self, value):
        """sette the H"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
