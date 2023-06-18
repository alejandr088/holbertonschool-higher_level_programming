#!/usr/bin/python3
"""
function that print a name
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints first_name and last_name
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    if isinstance(first_name, str) and \
       isinstance(last_name, str):
        print(f'My name is {first_name} {last_name}')
