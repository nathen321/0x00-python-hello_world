#!/usr/bin/python3
import sys

lise = sys.argv
siz = len(lise) - 1
i = 1

if siz == 0:
    print("0 arguments.")
elif siz> 0:
    print("{:d} arguments:".format(siz))
    for i in range(1, siz + 1):
        print("{:d}: {}".format(i, lise[i]))

