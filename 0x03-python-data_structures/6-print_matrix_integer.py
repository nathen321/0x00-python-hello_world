#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            lrow = len(row)
            for x in range(lrow):
                if x != lrow:
                    print("{:d} ".format(x), end="")
                else:
                    print("{:d}".format(x))
    else:
        print()

print_matrix_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("_--_")
print_matrix_integer()
