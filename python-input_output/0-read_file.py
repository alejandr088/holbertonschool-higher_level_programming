#!/usr/bin/python3
"""author: alejandr088"""


def read_file(filename=""):
    "function that reads a file"
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
