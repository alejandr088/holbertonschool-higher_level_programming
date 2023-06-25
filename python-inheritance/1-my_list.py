#!/usr/bin/python3
"""author: alejandr088"""


class MyList(list):
    """class that inherits list """
    def print_sorted(self):
        """function that prints itself but sorted"""
        copya = sorted(self)
        print(copya)
