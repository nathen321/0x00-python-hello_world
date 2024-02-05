#!/usr/bin/python3
"""BaseGeometry."""

class BaseGeometry:
    """BaseGeometry."""
    def area(self):
        """no area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate"""
        if type(value) not int:
            raise TypeError(name + " must be an integer")
        if value <= 0 :
            raise ValueError(name + " must be greater than 0")
