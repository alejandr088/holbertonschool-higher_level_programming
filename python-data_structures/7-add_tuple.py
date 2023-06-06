#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) < 2):
        tuple_a += (0, 0)
    elif (len(tuple_b) < 2):
        tuple_b += (0, 0)
    el_1a = tuple_a[0]
    el_1b = tuple_b[0]
    eladd = el_1a + el_1b

    tuple_f = (eladd, tuple_a[1] + tuple_b[1])

    return tuple_f
