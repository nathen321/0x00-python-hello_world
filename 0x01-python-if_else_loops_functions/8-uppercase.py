#!/usr/bin/python3
def uppercase(str):
    newone = ""
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            newone += chr(ord(str[i]) - 32)
        else:
            newone += str[i]
    print('{0}'.format(newone))
