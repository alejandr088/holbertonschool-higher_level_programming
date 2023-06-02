#!/usr/bin/env python3
def remove_char_at(str, n):
    copy = str
    result = ''
    for i in range(len(copy)):
        if i != n:
            result += copy[i]
    return result
