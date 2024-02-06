#!/usr/bin/python3
"""read file"""
def write_file(filename="", text=""):
    """reads files"""
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
