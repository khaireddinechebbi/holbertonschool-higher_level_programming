#!/usr/bin/python3
from sys import argv
from calculator_1 import add, mul, div, sub
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print(f"{a} {operator} {b} = {result}")
