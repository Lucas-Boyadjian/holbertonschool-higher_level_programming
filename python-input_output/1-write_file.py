#!/usr/bin/python3
"""
Module for file writing operations
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns
    the number of characters written

    Args:
        filename (str): The name of the file to write to,
        default is empty string
        text (str): The text to write to the file, default is empty string

    Returns:
        int: The number of characters written to the file
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)
