#!/usr/bin/python3
"""author: alejandr088"""
import json


def save_to_json_file(my_obj, filename):
    """function that saves to json"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
