#!/usr/bin/env python3

import csv, json

def convert_csv_to_json(csv_file):
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
        