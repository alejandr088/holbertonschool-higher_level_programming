#!/usr/bin/python3
for abcNotEq in range(97, 123):
    if chr(abcNotEq) not in ('e', 'q'):
        print(chr(abcNotEq), end='')
