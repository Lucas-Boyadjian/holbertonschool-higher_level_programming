#!/usr/bin/python3
"""
Module for saving objects to JSON files
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation

    Args:
        my_obj: The Python object to be serialized and saved
        filename (str): The name of the file to save the JSON to

    Returns:
        None: The function writes to a file instead of returning a value
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
