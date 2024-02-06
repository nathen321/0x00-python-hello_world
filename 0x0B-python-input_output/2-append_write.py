#!/usr/bin/python3
"""read file"""
def append_write(filename="", text=""):
    """
    reads files
    """
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
