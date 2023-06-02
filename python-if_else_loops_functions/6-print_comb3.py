#!/usr/bin/python3
for abc in range(0, 10):
    for cba in range(abc + 1, 10):
        if ((abc != 8 or cba != 9) and cba > abc):
            print('{:01d}{:01d}'.format(abc, cba), end=', ')
print('89')
