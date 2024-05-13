#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    rev_list = my_list[-n + 1:]
    return rev_list