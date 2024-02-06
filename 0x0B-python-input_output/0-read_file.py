#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="utf-8") as fl:
        for line in fl:
            print(line, end="")
