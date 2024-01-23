#!/usr/bin/python3
def safe_print_division(a, b):
    tor = 0
    try:
        tor = a / b
        print("Inside result: {}".format(tor))
    except ZeroDivisionError:
        tor = None
        print("Inside result: {}".format(tor))
    finally:
        return tor
