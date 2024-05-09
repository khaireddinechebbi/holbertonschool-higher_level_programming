#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number) % 10
    if number < 0:
        n = n * -1
    print(n, end='')
