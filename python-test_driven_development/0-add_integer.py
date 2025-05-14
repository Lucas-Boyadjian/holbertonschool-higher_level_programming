#!/usr/bin/python3
"""
Module that provides an addition function for integers

This module contains a function to add two integers or floats
"""


def add_integer(a, b=98):
    """
    Add two integers and return the result

    Args:
        a (int, float): first number
        b (int, float): second number, defaults to 98

    Returns:
        int: The sum of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
