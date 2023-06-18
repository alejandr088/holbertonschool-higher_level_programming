#!/usr/bin/python3
def add_integer(a, b=98):
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int or float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int or float):
        raise TypeError('b must be an integer')
    return a + b
