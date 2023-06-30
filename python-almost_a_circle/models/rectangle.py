#!/usr/bin/python3
"""
author: alejandr088
"""

from models.base import Base


class Rectangle(Base):
    """
    class that represent a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialized class Rectangle
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter method for width attr
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attr
        """
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """
        Getter method for the height attr
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attr
        """
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError('height must be > 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def x(self):
        """
        Getter method for the x attr
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attr
        """
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError('x must be an integer')

    @property
    def y(self):
        """
        Getter method for the y attr
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attr
        """
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError('y must be an integer')

    def area(self):
        """
        function that returns area value
        """
        return self.width * self.height

    def display(self):
        """
        function that prints the rectangle
        """
        for a in range(self.__y):
            print('')
        for b in range(self.__height):
            for c in range(self.__x):
                print(' ', end='')
            for d in range(self.__width):
                print('#', end='')
            print('')

    def __str__(self):
        """
        function that returns a str
        """
        return f'[Rectangle] ({self.id}) {self.__x}\
/{self.__y} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """function that order the args"""
        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
