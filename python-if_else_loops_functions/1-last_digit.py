#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

digit = 'Last digit of'
greater = 'and is greater than 5'
zero = 'and is 0'
lower = 'and is less than 6 and not 0'
last = abs(number) % 10

if last == 0:
    print(digit, number, 'is', last, zero)

elif last > 5:
    print(digit, number, 'is', last, greater)

elif last < 6:
    print(digit, number, 'is', last, lower)
