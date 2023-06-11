#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
        prev_value = 0
        result = 0
        for symbol in roman_string:
            value = roman_values.get(symbol, 0)
            result += value if value <= prev_value else value - 2 * prev_value
            prev_value = value
        return result
    return 0
