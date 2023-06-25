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
