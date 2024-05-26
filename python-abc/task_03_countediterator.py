#!/usr/bin/python3
"""
This module defines the CountedIterator class, which extends the built-in\
 iterator.
The CountedIterator class keeps track of the number of items iterated over.
"""


class CountedIterator:
    """
    CountedIterator is a custom iterator that keeps track of the number \
    of items that have been iterated over.

    Attributes:
        iterator (iterator): The original iterator object.
        count (int): A counter to track the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable and a counter.

        Args:
            iterable: An iterable to be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items.")

    def get_count(self):
        """
        Return the current value of the counter.

        Returns:
            int: The number of items iterated over so far.
        """
        return self.count
