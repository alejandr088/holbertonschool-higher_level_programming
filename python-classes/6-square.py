#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
author: alejandr088
"""


class Square():
    """
    A Square represented with a size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
