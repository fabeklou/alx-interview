#!/usr/bin/python3

"""
This module contains a function to rotate a 2D matrix in-place
by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix in-place by 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): The 2D matrix to be rotated.

    Returns:
        None: The function does not return anything.
            The matrix is rotated in-place.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        rotate_2d_matrix(matrix)
        After rotation, matrix will be:
            [[7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]]
    """

    size = len(matrix)
    m = matrix  # aliasing

    # Transposing
    for row in range(size):
        for col in range(row, size):
            m[row][col], m[col][row] = m[col][row], m[row][col]

    # Reversing
    for row in range(size):
        matrix[row].reverse()
