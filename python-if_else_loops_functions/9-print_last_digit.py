#!/usr/bin/python3
def print_last_digit(number):
    copy = abs(number) % 10
    print(copy, end='')
    return copy
