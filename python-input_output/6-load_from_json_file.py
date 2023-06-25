#!/usr/bin/python3
"""author: alejandr088"""
import json


def load_from_json_file(filename):
    """function that creates an obj / JSON file"""
    with open(filename, 'r') as file:
        my_obj = json.load(file)
    return my_obj
