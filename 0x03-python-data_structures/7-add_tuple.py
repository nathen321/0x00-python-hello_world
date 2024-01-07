#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = validate_tuple(tuple_a)
    tuple_b = validate_tuple(tuple_b)
    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))

def validate(v_tuple=()):
    if len(v_tuple) < 2:
        if len(v_tuple) == 1:
            v_tuple = (v_tuple[0], 0)
        elif len(v_tuple) == 0:
            v_tuple = (0, 0)
    elif len(_tuple) > 2:
        v_tuple = (v_tuple[0], v_tuple[1])
    return v_tuple
