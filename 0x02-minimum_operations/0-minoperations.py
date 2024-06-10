#!/usr/bin/python3

"""This module contains, a function that calculates the minimum
number of operations required to reach the target value.
"""

from typing import Union


def minOperations(target: int) -> Union[int, float]:
    """
    Calculates the minimum number of operations required
    to reach the target value.

    Args:
        target (int): The target value to reach.

    Returns:
        int: The minimum number of operations required
            to reach the target value.
    """
    result: Union[float, int] = float('+inf')
    initial_count: int = 1

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
        if curr_count == target:
            result = min(result, curr_ops)
            return

        if prev_copy == 0:
            prev_copy = curr_ops = 1

        if curr_count + prev_copy <= target and curr_ops < result:
            bt(curr_count + prev_copy, prev_copy, curr_ops + 1)

        if curr_count * 2 <= target and curr_ops < result:
            bt(curr_count * 2, curr_count, curr_ops + 2)

    bt(initial_count, 0, 0)
    return 0 if result == float('+inf') else result
