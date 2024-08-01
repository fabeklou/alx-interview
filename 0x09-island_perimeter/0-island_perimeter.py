#!/usr/bin/python3

"""
This module calculates the perimeter of an island
represented by a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by a grid.

    Args:
        grid (list[list[int]]): A 2D grid representing the island,
        where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def inbound(row, col):
        """
        Check if the given row and column indices are within the
        bounds of the grid.
        """
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                continue
            for r, c in directions:
                new_row, new_col = row + r, col + c
                if inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                    perimeter += 1
                elif not inbound(new_row, new_col):
                    perimeter += 1

    return perimeter
