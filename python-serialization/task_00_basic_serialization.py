#!/usr/bin/env python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes data to JSON format and saves it to a file

    Args:
        data: The data to serialize (dict, list, etc.)
        filename: Path to the output file
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(data))


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it

    Args:
        filename: Path to the JSON file

    Returns:
        The deserialized data (dict, list, etc.)
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
