#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list)
    if idx < 0 or idx >= n:
        return None
    else:
        print("Element at index {:d} is {:d}".format(idx, element_at(list, idx)))
