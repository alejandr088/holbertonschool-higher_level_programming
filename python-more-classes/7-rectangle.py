#!/usr/bin/python3
"""
a function that defines a rectangle
"""


class Rectangle:
    """
    class that repr a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        initializate rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        returns the width
        """
        return self.__width

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        set the width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """
        set the height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        rectangle_str = ''
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + '\n'
        return rectangle_str[:-1]

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
