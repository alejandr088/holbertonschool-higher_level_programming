#!/usr/bin/python3
def uppercase(str):
    up = ""
    for abc in str:
        if 'a' <= abc <= 'z':
            abc = chr(ord(abc) - 32)
        up += abc
    print(f'{up}')
