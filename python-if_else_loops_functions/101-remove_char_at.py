#!/usr/bin/env python3
def remove_char_at(str, n):
    str_input = str
    if not isinstance(n, int) or n < 0 or n >= len(str_input):
        return str_input

    copy = str_input[:n] + str_input[n+1:]
    return copy
