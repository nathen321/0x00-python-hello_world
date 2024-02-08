#!/usr/bin/python3
'''ex: 9 work in progress'''

class Student:
    """norma student"""
    def __init__(self, first_name, last_name, age):
        """initiaisation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retyvin the dict"""
        return self.__dict__
