#!/usr/bin/python3
"""read file"""
def write_file(filename="", text=""):
    """reads files"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
