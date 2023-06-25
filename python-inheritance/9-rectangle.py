#!/usr/bin/python3
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
        """function that represent area"""
        return self.__width * self.__height

    def __str__(self):
        """function that return a str"""
        return f'[Rectangle] {self.__width}/{self.__height}'
