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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        self.__width = value

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
        self.__height = value

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
        self.__x = value

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
        self.__y = value
