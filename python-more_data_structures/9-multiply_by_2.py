#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        mult = value * 2
        new_dictionary[key] = mult
    return new_dictionary
