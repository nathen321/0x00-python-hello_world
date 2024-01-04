#!/usr/bin/python3
def print_last_digit(number):
    newone = number % 10
    print('{0}'.format(newone), end="")
    return(newone)
