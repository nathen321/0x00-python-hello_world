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
        self._Square__size = size
