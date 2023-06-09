#!/usr/bin/python3
def best_score(a_dictionary):
        if a_dictionary is None:
                return None
        high = max(a_dictionary, key=a_dictionary.get)
        return high
