#!/usr/bin/python3
"""read file"""
def read_file(filename=""):
    """reads files"""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
