#!/usr/bin/python3
"""
this is scripte of a representation of a rectangle
"""

from base import Base

class Rectangle(Base):
    """
    this class is arepresentio of a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        this module initialase attribute of tje obj
        """
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
        """
        function thas return the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        function thas sette the value of width
        """
        self.chek_valid(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        function thas return the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        function thas sette the value of height
        """
        self.chek_valid(value, "height")
        self.__height = value

    @property
    def x(self):
        """
        function thas return the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        function thas sette the value of x
        """
        self.chek_valid(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        function thas return the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        function thas sette the value of y
        """
        self.chek_valid(value, "y")
        self.__y = value

    def chek_valid(self, value, tp):
        """
        this functiontion check the validity of the data
        """
        if type(value) is not int:
            raise TypeError(tp + " must be an integer")
        if value <= 0 and tp in ("width", "height"):
            raise ValueError(tp + ' must be > 0')
        if value < 0 and tp in ('x', 'y'):
            raise ValueError(tp + ' must be >= 0')

    def area(self):
        """
        return the area oof the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        display a rectangle at x,y cordinate
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """
        return a descroptionof the rectangle
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        reset the attribute of the rectengle
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)
