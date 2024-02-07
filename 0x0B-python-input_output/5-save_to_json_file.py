#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""

import json

def save_to_json_file(my_obj, filename):
    """"writ object to file """
    with open(filename, 'w', encodin="utf-8") as fl:
        json.dump(my_obj, fl)
