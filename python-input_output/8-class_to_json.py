#!/usr/bin/python3
"""
Module for converting class instance to JSON dictionary
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: An instance of a Class with serializable attributes

    Returns:
        dict: Dictionary containing all serializable attributes of obj
    """
    return obj.__dict__
