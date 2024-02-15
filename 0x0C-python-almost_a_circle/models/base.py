#!/usr/bin/python3
"""

the base classe of futer project

"""

from os import path
import json


class Base:
    """
    this class initialse the id attribue of futer class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        this module is used to initalise the id attribu of futer child class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            attrs = []

            for elem in list_objs:
                attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(attrs))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        file_name = cls.__name__ + ".json"

        if path.exists(file_name) is False:
            return []

        with open(file_name, mode="r", encoding='utf-8') as f:
            obj = cls.from_json_string(f.read())
            new_inst = []
            for x in obj:
                new_inst.append(cls.create(**x))
            return new_inst
