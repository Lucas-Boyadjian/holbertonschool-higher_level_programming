#!/usr/bin/python3
"""
Module for file appending operations
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns
    the number of characters added

    Args:
        filename (str): The name of the file to append to,
        default is empty string
        text (str): The text to append to the file, default is empty string

    Returns:
        int: The number of characters appended to the file
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)
