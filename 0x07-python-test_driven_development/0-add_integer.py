#!/usr/bin/python3
"""add two number"""


def add_integer(a, b=98):
    """add two number"""
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    a = make_them_int(a)
    b = make_them_int(b)
    return a + b

def make_them_int(num):
    """make them int"""
    if type(num) is float:
        num = int(num)
        return num
    return num
