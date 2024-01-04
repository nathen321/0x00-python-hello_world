#!/usr/bin/python3
import sys

lise = sys.argv
siz = len(lise)
sum = 0

if __name__ == "__main__":
    for i in range(1, siz):
        sum += int(lise[i])
    print(sum)
