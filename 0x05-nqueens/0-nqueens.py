#!/usr/bin/python3

"""
This module contains a backtracking algorithm to solve the N-Queens problem.

The N-Queens problem is the following:
Given an integer N, find all possible placements of N queens
on an NxN chessboard so that no queen attacks another.

Each placement is represented as a list of lists, where each inner list
contains the row and column of a queen.
"""

import sys


def bt(row, queens, visit_col, visit_diag_add, visit_diag_sub, solutions):
    """
    Backtracking algorithm to find all possible valid placements of N queens
    on an NxN chessboard.

    Args:
        row (int): current row we are trying to place a queen on.
        queens (list): list of already placed queens. Each queen is represented
            as a list of two integers, the row and column of the queen.
        visit_col (set): set of columns that we already visited.
        visit_diag_add (set): set of diagonals that we already visited,
            where the diagonal is represented as the sum of the row and column
            indices.
        visit_diag_sub (set): set of diagonals that we already visited,
            where the diagonal is represented as the difference of the row and
            column indices.
        solutions (list): list of found solutions. Each solution is a list of
            lists, where each inner list contains the row and
            column of a queen.

    Returns:
        None
    """
    if len(queens) == number_of_queens:
        solutions.append(queens[:])
        return

    if row == number_of_queens:
        return

    for col in range(number_of_queens):
        if col in visit_col:
            continue
        if row + col in visit_diag_add or row - col in visit_diag_sub:
            continue

        queens.append([row, col])
        visit_col.add(col)
        visit_diag_add.add(row + col)
        visit_diag_sub.add(row - col)

        bt(row + 1, queens,
           visit_col, visit_diag_add, visit_diag_sub, solutions)
        if queens:
            queens.pop()
            visit_col.remove(col)
            visit_diag_add.remove(row + col)
            visit_diag_sub.remove(row - col)


def nqueens():
    """
    Finds all possible valid placements of N queens on an NxN chessboard.

    This function implements a backtracking algorithm to find all possible
    valid placements of N queens on an NxN chessboard. The algorithm starts
    by placing the first queen in the first row and then iteratively places
    the remaining queens in subsequent rows. At each step, it checks if the
    current queen can be placed on the current row and column without
    attacking any previously placed queens. If a valid placement is found,
    the function recursively continues to the next row. If no valid placement
    is found, the algorithm backtracks to the previous row and tries
    alternate column for the same row.

    The function returns a list of all possible valid placements of N queens.
    Each solution is represented as a list of lists, where each inner list
    contains the row and column of a queen.

    Args:
        None

    Returns:
        solutions (list): list of all possible valid placements of N queens.
            Each solution is represented as a list of lists, where each inner
            list contains the row and column of a queen.

    Example:
        >>> nqueens()
        [[0, 1], [1, 3], [2, 0], [3, 2]]

    Note:
        This function assumes that the input N is at least 4.
    """
    solutions = []
    visit_col, visit_diag_add, visit_diag_sub = set(), set(), set()
    bt(0, [], visit_col, visit_diag_add, visit_diag_sub, solutions)

    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    number_of_queens = 0

    try:
        number_of_queens = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if number_of_queens < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens()
    for solution in solutions:
        print(solution)
