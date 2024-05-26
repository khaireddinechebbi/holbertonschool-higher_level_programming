#!/usr/bin/python3
"""
This module defines the VerboseList class, which extends \
the built-in list class.
The VerboseList class prints notifications for append, extend, \
remove, and pop operations.
"""


class VerboseList(list):
    """
    VerboseList is a subclass of the built-in list class \
    that prints notifications for append, extend, remove, and pop operations.
    """

    def append(self, item):
        """
        Append an item to the end of the list and print a notification.

        Args:
            item: The item to be appended to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Extend the list by appending all the items from the iterable \
    and print a notification.

        Args:
            items: An iterable of items to be added to the list.
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of the item from the list \
    and print a notification.

        Args:
            item: The item to be removed from the list.

        Raises:
            ValueError: If the item is not in the list.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        Remove and return the item at the given index (default last).
        Print a notification for the popped item.

        Args:
            index (int, optional): The index of the item to be removed. \
Default is -1.

        Returns:
            The item removed from the list.

        Raises:
            IndexError: If the list is empty or the index is out of range.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
