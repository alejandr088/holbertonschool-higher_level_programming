#!/usr/bin/python3
"""
author: alejandr088
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class that represents a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialized Square class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter method for size attr
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for size attr
        """
        self.width = value
        self.height = self.width

    def __str__(self):
        """
        returns a string rep of Square
        """
        return f'[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}'
