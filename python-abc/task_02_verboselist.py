#!/usr/bin/env python3

class VerboseList(list):
    """
    A verbose version of the built-in list class that prints messages
    when certain methods are called.

    This class inherits from the built-in list class and overrides common
    list operations to provide feedback when they are executed.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a message.

        Args:
            item: The item to be appended to the list.
        """
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, x):
        """
        Extend the list with elements from an iterable and print a message.

        Args:
            x: An iterable containing elements to be added to the list.
        """
        print("Extended the list with [{}] items.".format(len(x)))
        super().extend(x)

    def remove(self, item):
        """
        Remove the first occurrence of an item from the
        list and print a message.

        Args:
            item: The item to be removed from the list.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, item=-1):
        """
        Remove and return an item at the given position and print a message.

        Args:
            item: The index of the item to be removed (default is -1,
                 which removes the last item).

        Returns:
            The item that was removed from the list.
        """
        item_popped = self[item]
        super().pop(item)
        print("Popped [{}] from the list.".format(item_popped))
        return item_popped
