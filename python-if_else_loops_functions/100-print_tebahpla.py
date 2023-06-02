#!/usr/bin/python3
for abc in range(90, 64, -1):
    print('{}'.format(chr(abc + 32 if abc % 2 == 0 else abc)), end='')
