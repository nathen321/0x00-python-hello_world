#!/usr/bin/python3
import sys

lise = sys.argv
siz = len(lise) - 1
i = 1

if siz == 0:
    print("0 arguments.")
elif siz> 0:
    print("{:d} arguments:".format(siz))
    for i in range(siz):
        if i == 0:
            continue
        print("{:d}: {}".format(i, lise[i]))

