#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """function that compare classes / inherit"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
