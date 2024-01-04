#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        newone = (number * -1) % 10
    else:
        newone = number % 10
    print('{0}'.format(newone), end="")
    return(newone)
