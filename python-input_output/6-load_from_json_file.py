#!/usr/bin/python3
"""
Module for creating objects from JSON files
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename (str): The path to the JSON file to read

    Returns:
        object: The Python object created from the JSON file
    """
    with open(filename, "r", encoding='utf8') as my_file:
        return json.load(my_file)
