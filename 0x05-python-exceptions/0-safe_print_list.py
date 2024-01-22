#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tor = 0
    for y in range(x):
        try:
            print(my_list[y], end="")
            tor += 1
        except IndexError:
            pass
    print()
    return tor
