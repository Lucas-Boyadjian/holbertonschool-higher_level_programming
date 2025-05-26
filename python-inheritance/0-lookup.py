#!/usr/bin/python3
"""Module that provides a function to list available attributes
    and methods of an object"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect

    Returns:
        A list containing the names of all attributes and methods of the object
    """
    return dir(obj)
