#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""

import json

def from_json_string(my_str):
    """" representation """
    return json.loads(my_str)
