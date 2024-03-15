#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # adds 2 tuples

    while len(tuple_a) < 2:
        tuple_a += (0,)

    while len(tuple_b) < 2:
        tuple_a += (0,)

    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return res
