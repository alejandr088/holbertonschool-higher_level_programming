#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
author: alejandr088
"""


class Square():
    """
    A Square represented with a size.
    """

    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
