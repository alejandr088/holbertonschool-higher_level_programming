#!/usr/bin/python3
"""author: alejandr088"""


def write_file(filename='', text=''):
    """function that writes a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
