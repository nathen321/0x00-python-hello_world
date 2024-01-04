#!/usr/bin/python3
import hidden_4

lise = dir(hidden_4)
siz = len(lise)

if __name__ == "__main__":
    for i in range(siz):
        if lise[i][:2] != '__':
            print(lise[i])
