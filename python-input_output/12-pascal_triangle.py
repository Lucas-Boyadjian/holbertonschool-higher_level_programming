#!/usr/bin/python3

def pascal_triangle(n):
    """Returns Pascal's triangle up to n rows"""
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
