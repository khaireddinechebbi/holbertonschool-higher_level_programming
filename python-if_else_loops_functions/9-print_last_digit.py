#!/usr/bin/python3
def print_last_digit(number):
    n = number % 10
    if number < 0:
        n *= -1
    print(n, end="")
    return n
