#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_file):
    """
    Converts data from a CSV file to JSON format and saves it to a file

    Args:
        csv_file: Path to the CSV file to convert

    Returns:
        True if the conversion was successful, False if the file was not found
    """
    my_list = []
    try:
        with open(csv_file, 'r') as data:
            for line in csv.DictReader(data):
                my_list.append(line)

        with open('data.json', 'w') as json_file:
            json.dump(my_list, json_file)
        return True

    except FileNotFoundError:
        return False
