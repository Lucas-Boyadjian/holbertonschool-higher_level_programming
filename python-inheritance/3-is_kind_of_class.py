#!/usr/bin/python3
"""Module that provides a function to check if an object is an instance of,
or inherited from, a specified class"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        Boolean: True if obj is an instance of a_class or inherits from it,
        False otherwise
    """
    return isinstance(obj, a_class)
