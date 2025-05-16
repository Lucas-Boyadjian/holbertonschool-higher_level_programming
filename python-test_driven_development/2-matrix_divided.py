#!/usr/bin/python3
"""
Module for matrix division

This module provides a function to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div

    Args:
        matrix (list): A list of lists of integers/floats
        div (int/float): The divisor

    Returns:
        list: A new matrix with all elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If each row of the matrix doesn't have the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(error_msg)

    if matrix == []:
        raise TypeError(error_msg)

    if matrix == [[], []]:
        return [[], []]

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)

    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(error_msg)

    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(item / div, 2) for item in row] for row in matrix]
