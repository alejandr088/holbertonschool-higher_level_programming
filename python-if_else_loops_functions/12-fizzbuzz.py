#!/usr/bin/env python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            print('FizzBuzz', end=' ' if a != 100 else '')
        elif a % 5 == 0:
            print('Buzz', end=' ' if a != 100 else '')
        elif a % 3 == 0:
            print('Fizz', end=' ' if a != 100 else '')
        else:
            print(a, end=' ' if a != 100 else '')
