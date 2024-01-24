#!/usr/bin/python3
"""Square Class

just a square

"""


class Square:
    """ init a square

    The __init__ method initializes the size value of the square.

    Attributes:
       size (:obj:`int`, optional): The size of the square.

    Raises:
        TypeError: If `size` type is not `int`.

        ValueError: If `size` is less than `0`.

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
    
    def area(self):
        """Returns the current square area

        """
        return self._Square__size ** 2

