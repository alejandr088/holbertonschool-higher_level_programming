#!/usr/bin/python3
"""author: alejandr088"""


def append_write(filename='', text=''):
    """funct that append a text to a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        num_chars_added = len(text)
    return num_chars_added
