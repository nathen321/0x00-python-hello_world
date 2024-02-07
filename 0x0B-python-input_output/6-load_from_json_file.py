#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""

import json

def load_from_json_file(filename):
    """"writ object to file """
    with open(filename, 'r', encoding="utf-8") as fl:
        return json.load(fl)
