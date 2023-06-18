#!/usr/bin/python3
"""
add function
"""


def add_integer(a, b=98):
    """
    add 2 integers
    """
    if not isinstance(a, (int or float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int or float)):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b
