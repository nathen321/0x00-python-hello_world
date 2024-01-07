#!/usr/bin/python3
def no_c(my_string):
    for x in range(len(my_string)):
        if my_string[x] == "c" or my_string[x] == "C":
            my_string.pop([x])

    return my_string
