#!/usr/bin/python3
"""BaseGeometry."""

class BaseGeometry:
    """BaseGeometry."""
    def area(self):
        """no area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate
        Args:
            name (str): The name of the value.
            value (int): The value.
        Raises:
            TypeError: If `value` isn't a integer.
            ValueError: If `value` is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0 :
            raise ValueError(name + " must be greater than 0")

class Rectangle(BaseGeometry):
    """well, it's just a rectangle"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator("width", width)
        BaseGeometry.integer_validator("height", height)

        self.__width = width
        self.__height = height
