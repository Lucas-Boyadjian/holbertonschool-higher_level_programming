#!/usr/bin/python3
"""
Module for text_indentation function
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of '.', '?', and ':' characters

    Args:
        text (str): The text to be indented

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = [".", "?", ":"]
    current_line = ""

    i = 0
    while i < len(text):
        current_line += text[i]

        if text[i] in special_chars:
            print(current_line.strip())
            print()
            current_line = ""

            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1

    if current_line.strip():
        print(current_line.strip(), end="")
