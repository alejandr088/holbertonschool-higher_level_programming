#!/usr/bin/python3
"""author: alejandr088"""


def inherits_from(obj, a_class):
    """function that compare subclasses"""
    if issubclass(type(obj), a_class) and \
       type(obj) is not a_class:
        return True
    else:
        return False
