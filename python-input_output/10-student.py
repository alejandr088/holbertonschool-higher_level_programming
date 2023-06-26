#!/usr/bin/python3
"""author: alejandr088"""


class Student:
    """a class that represent a student"""
    def __init__(self, first_name, last_name, age):
        """a funct that init class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a funct that ret a dict representation"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
