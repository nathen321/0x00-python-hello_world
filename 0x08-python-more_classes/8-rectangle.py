#!/usr/bin/python3
"""

Rectangle that does nothing

"""


class Rectangle:
    """ it's a rectangle pls work """
    number_of_instances = 0
    print_symbol = "#"

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
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """del msg"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

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

    def area(self):
        """return area"""
        return self.__height * self.__width

    def perimeter(self):
        """return P"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """draw"""
        rect_str = ''
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rect_str

        for i in range(h):
            for j in range(w):
                rect_str += str(self.print_symbol)

            if i != h - 1:
                rect_str += '\n'

        return rect_str

    def __repr__(self):
        """return a string representation rectangle"""
        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'

    @staticmethod
        def bigger_or_equal(rect_1, rect_2):
            """comparing to rec"""
            if isinstance(rect_1, Rectangle) is False:
                raise TypeError('rect_1 must be an instance of Rectangle')

            if isinstance(rect_2, Rectangle) is False:
                raise TypeError('rect_2 must be an instance of Rectangle')

            if rect_1.area() > rect_2.area():
                return rect_1.area()
            return rect_2.area()
