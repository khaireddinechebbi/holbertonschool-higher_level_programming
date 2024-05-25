#!/usr/bin/python3
"""
This module define a class Mylist that inherits from list\
and provile a function that prints the list sorted ascendingly
"""


class MyList(list):
    """
    MyList inherits from list and provides an additional
    method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        Assumes all elements are of type int.
        """
        print(sorted(self))


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/1-my_list.txt")
