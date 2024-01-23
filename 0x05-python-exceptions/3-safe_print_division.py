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


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
