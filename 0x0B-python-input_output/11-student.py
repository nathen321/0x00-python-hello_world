#!/usr/bin/python3
'''ex: 9 work in progress'''

class Student:
    """norma student"""
    def __init__(self, first_name, last_name, age):
        """initiaisation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retyvin the dict"""
        dic = self.__dict__
        seld = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return dic
                    
                if attr in dic:
                    seld[attr] = dic[attr]

            return seld
        return dic

def reload_from_json(self, json):
    """taske: 11"""
    for key, value in json.items:
        if key in self.__dict__.keys():
            self.__dict__[key] = value
