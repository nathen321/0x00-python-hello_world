#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tor = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            tor += 1
        except (IndexError, ValueError, TypeError):
            continue
    print()
    return tor
