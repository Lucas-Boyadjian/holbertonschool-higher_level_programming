#!/usr/bin/env python3

import json

def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(data))

def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
