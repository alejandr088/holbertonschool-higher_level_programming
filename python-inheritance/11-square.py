#!/usr/bin/python3
"""author: alejandr088"""


class BaseGeometry():
    """class with objects"""
    def area(self):
        """function that represent area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """function that check integers"""
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """class initialized"""
    def __init__(self, width, height):
        """function that init a rectangle"""
        self.__width = 0
        self.__height = 0
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """functiont that return area value"""
        return self.__width * self.__height

    def __str__(self):
        """function that returns a str"""
        return f'[Rectangle] {self.__width}/{self.__height}'


class Square(Rectangle):
    """class initialized"""
    def __init__(self, size):
        """function that init the square"""
        self.__size = 0
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """function that return a str"""
        return f'[Square] {self.__size}/{self.__size}'
