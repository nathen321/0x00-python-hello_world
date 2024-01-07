#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            lrow = len(row)
            for x in range(lrow):
                if x != lrow - 1:
                    print("{:d} ".format(row[x]), end="")
                else:
                    print("{:d}".format(row[x]), end="")
            print()


