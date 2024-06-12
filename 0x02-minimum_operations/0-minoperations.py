#!/usr/bin/python3

"""This module contains, a function that calculates the minimum
number of operations required to reach the target value.
"""

from collections import deque


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
    dq = deque([(1, 0, 0)])
    visited = set()

    while dq:
        count, copied, ops = dq.popleft()
        visited.add((count, copied))

        if count == n:
            result = min(result, ops)

        if copied == 0:
            copied = ops = 1

        past = count + copied
        if past <= n and ops < result and (past, copied) not in visited:
            dq.append((count + copied, copied, ops + 1))
        cpy_past = count * 2
        if cpy_past <= n and ops < result and (cpy_past, count) not in visited:
            dq.append((count * 2, count, ops + 2))

    return 0 if result == float('+inf') else result
