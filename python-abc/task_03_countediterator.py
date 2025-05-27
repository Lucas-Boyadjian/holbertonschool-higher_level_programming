#!/usr/bin/env python3

class CountedIterator:
    """
    An iterator that counts the number of items that have been iterated over.

    This class wraps any iterable object and keeps track of how many items
    have been retrieved through the iterator.
    """

    def __init__(self, iterator_obj):
        """
        Initialize the CountedIterator with an iterable object.

        Args:
            iterator_obj: Any iterable object to be wrapped by this iterator.
        """
        self.iterator_obj = iter(iterator_obj)
        self.count_item = 0

    def __next__(self):
        """
        Get the next item from the iterator and increment the counter.

        Returns:
            The next item in the iterator.

        Raises:
            StopIteration: When there are no more items to iterate over.
        """
        try:
            next_iterator = next(self.iterator_obj)
            self.count_item += 1
            return next_iterator

        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Get the current count of items that have been iterated over.

        Returns:
            An integer representing the number of items that have been
            retrieved through calls to __next__.
        """
        return self.count_item
