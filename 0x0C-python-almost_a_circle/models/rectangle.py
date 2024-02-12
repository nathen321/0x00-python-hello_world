#!/usr/bin/python3
"""dooc"""

from base import Base

class Rectangle(Base):
    """doc"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """doc"""
        super().__init__(id)
        self.chek_valid(width, 'width')
        self.chek_valid(height, 'height')
        self.chek_valid(x, 'x')
        self.chek_valid(y, 'y')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.chek_valid(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.chek_valid(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.chek_valid(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.chek_valid(value, "y")
        self.__y = value

    def chek_valid(self, value, tp):
        """ doc """
        if type(value) is not int:
            raise TypeError(tp + " must be an integer")
        if value <= 0 and tp in ("width", "height"):
            raise ValueError(tp + ' must be > 0')
        if value < 0 and tp in ('x', 'y'):
            raise ValueError(tp + ' must be >= 0')
