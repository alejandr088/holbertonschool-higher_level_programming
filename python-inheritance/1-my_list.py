#!/usr/bin/python3
class MyList(list):
    """class that inherits list """
    def print_sorted(self):
        """function that prints itself but sorted"""
        copya = self.copy()
        copya.sort()
        print(copya)
