#!/usr/bin/python3
"""
Module for file reading operations
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout

    Args:
        filename (str): The name of the file to read, default is empty string

    Returns:
        None: This function prints the content instead of returning it
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
