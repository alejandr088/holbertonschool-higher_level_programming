#!/usr/bin/env python3
def fizzbuzz():
    for a in range(1, 101):
        none = (a % 3) != 0 and (a % 5) != 0
        both = (a % 3) == 0 and (a % 5) == 0
        mul5 = (a % 5) == 0

        if none:
            print(a, end=' ')
        elif both:
            print('FizzBuzz', end=' ')
        elif mul5:
            print('Buzz', end=' ')
        else:
            print('Fizz', end=' ')
