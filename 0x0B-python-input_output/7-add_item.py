#!/usr/bin/python3
"""ex:7"""
from sys import argv
from os import path
load_json = __import__('6-load_from_json_file').load_from_json_file
save_json = __import__('5-save_to_json_file').save_to_json_file

if path.exists('add_item.json'):
    json_file = load_json('add_item.json')
else:
    json_file = []

for i range(1, len(argv)):
    json_file.append(argv[i])

save_json(json_file, 'add_item.json')
