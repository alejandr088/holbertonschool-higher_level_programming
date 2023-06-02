#!/usr/bin/python3
for abc in range(0, 10):
    for cba in range(abc + 1, 10):
        if (abc != 8 or cba != 9):
            print(f'{abc:01d}{cba:01d}', end=', ')
print('89')
