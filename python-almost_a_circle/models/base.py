#!/usr/bin/python3
"""
author: alejandr088
"""


class Base:
    """
    class that represent Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class that init Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
