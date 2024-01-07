#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxe = my_list[0]
        for x in my_list:
            if maxe < my_list[x]:
                maxe = my_list[x]
        return maxe
    else:
        return None
