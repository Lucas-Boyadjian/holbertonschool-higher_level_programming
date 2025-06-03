#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)