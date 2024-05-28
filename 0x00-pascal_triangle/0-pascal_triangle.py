#!/usr/bin/python3

"""This module contains the  of the function pascal_triangle"""


def pascal_triangle(n):
    """pascal_traiangle create and returns a list of lists
    of integers representing the Pascal's triangle

    Arguments:
        n (int): the height of the triangle

    Returns:
        (List[List]): an empty list if n <= 0, a 2D list otherwise
    """
    if n <= 0:
        return []

    triangle = [[1] * size for size in range(1, n + 1)]
    for idx1 in range(2, n):
        for idx2 in range(1, len(triangle[idx1 - 1])):
            triangle[idx1][idx2] = triangle[idx1 - 1][idx2 - 1]\
                + triangle[idx1 - 1][idx2]

    return triangle
