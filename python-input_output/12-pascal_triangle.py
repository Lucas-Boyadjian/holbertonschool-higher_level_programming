#!/usr/bin/python3
"""
Module for Pascal's Triangle generation.
Contains a function that returns Pascal's triangle as a list of lists.
"""


def pascal_triangle(n):
    """Returns Pascal's triangle up to n rows

    Args:
        n (int): Number of rows to generate

    Returns:
        list: List of lists representing Pascal's triangle,
        empty list if n <= 0
    """
    if n <= 0:
        return []

    result_list = []

    for i in range(n):
        actual_list = []

        for j in range(i + 1):
            if j == 0 or j == i:
                actual_list.append(1)
            else:
                prev_list = result_list[i - 1]
                actual_list.append(prev_list[j - 1] + prev_list[j])

        result_list.append(actual_list)

    return result_list
