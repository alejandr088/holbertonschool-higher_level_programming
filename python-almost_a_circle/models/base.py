#!/usr/bin/python3
"""
author: alejandr088
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string rep
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
