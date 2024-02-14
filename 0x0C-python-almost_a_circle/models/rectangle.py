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

    def area(self):
        """doc"""
        return self.__height * self.__width

    def display(self):
        """doc"""
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """return a descroptionof the rectangle

        >>> r1 = Rectangle(4, 6, 2, 1, 12)
        >>> print(r1)
        [Rectangle] (12) 2/1 - 4/6

        >>> r2 = Rectangle(5, 5, 1)
        >>> print(r2)
        [Rectangle] (1) 1/0 - 5/5

        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """doc"""
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
