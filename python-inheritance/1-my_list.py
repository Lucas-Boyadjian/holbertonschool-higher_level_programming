#!/usr/bin/python3
"""Module containing the MyList class"""


class MyList(list):
    """
    MyList class that inherits from list

    This class extends the built-in list class with
    additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order

        This method does not modify the original list,
        it creates a sorted copy and prints it.
        """
        print(sorted(self))
