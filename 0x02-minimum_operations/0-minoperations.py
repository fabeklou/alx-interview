#!/usr/bin/python3

"""This module contains, a function that calculates the minimum
number of operations required to reach the target value.
"""

import sys


def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations required
    to reach the target value.

    Args:
        n (int): The target value to reach.

    Returns:
        int: The minimum number of operations required
            to reach the target value.
    """
    result = float('+inf')
    initial_count = 1
    sys.setrecursionlimit(100_000)

    def bt(curr_count: int, prev_copy: int, curr_ops: int) -> None:
        """
        Backtracking function to find the minimum number of operations
        required to reach the target count.

        Args:
            curr_count (int): The current count of characters.
            prev_copy (int): The count of characters copied in
                the previous operation.
            curr_ops (int): The current number of operations
                performed.

        Returns:
            None
        """
        nonlocal result
        if curr_count == n:
            result = min(result, curr_ops)
            return

        if prev_copy == 0:
            prev_copy = curr_ops = 1

        if curr_count + prev_copy <= n and curr_ops < result:
            bt(curr_count + prev_copy, prev_copy, curr_ops + 1)

        if curr_count * 2 <= n and curr_ops < result:
            bt(curr_count * 2, curr_count, curr_ops + 2)

    bt(initial_count, 0, 0)
    return 0 if result == float('+inf') else result
