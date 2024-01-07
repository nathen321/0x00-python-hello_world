#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for x in row:
                print("{:d} ".format(x), end="")
            print()
    else:
        print()

print_matrix_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
