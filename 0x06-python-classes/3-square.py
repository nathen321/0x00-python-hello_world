#!/usr/bin/python3
"""Square Class

just a square

"""


class Square:
    """ init a square

    like i said a square

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    """ get area of a square

    like i said area of a square

    """
    def area(self):
        """ Return area of a square
        Return:
            area of the squar
        """
        return self.__size ** 2

