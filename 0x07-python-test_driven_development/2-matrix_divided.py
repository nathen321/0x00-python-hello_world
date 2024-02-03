#!/usr/bin/python3
"""divides all elements of a matrix"""
def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    check_for_list(matrix)
    check_for_divisor(div)

    elem_sizes = set()
    new_list = list()

    for elem in matrix:
        if check_for_list(elem) is False:
            raises_matrix_type_error()

        elem_sizes = check_row_size_inconsistency(elem_sizes, elem)
        values = []

        for value in elem:
            if check_for_number(value) is False:
                raises_matrix_type_error()

            values.append(round(value / div, 2))
        new_list.append(values)
    return new_list

def check_for_list(value):
    """check the list"""
    if type(value) is not list or len(value) == 0:
        raise TypeError('matrix must be a matrix \
                (list of lists) of integers/floats')

def check_for_divisor(div):
    """check for divisor"""
    if check_for_number(div) is False:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

def check_for_number(value):
    """chech for number"""
    if type(value) is not int and type(value) is not float:
        return False
    if value != value:
        return False
    return True

def check_row_size_inconsistency(elem_sizes, row):
    """check row size inconsistency"""
    elem_sizes.add(len(row))

    if len(elem_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    return elem_sizes
