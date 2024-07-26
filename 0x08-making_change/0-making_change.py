#!/usr/bin/python3

"""
This module provides a function to calculate the minimum number
of coins needed to make change for a given total.
"""

from collections import deque


def makeChange(coins, total):
    """
    Calculates the minimum number of coins
    needed to make change for a given total.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The total amount to make change for.

    Returns:
        int: The minimum number of coins needed to make change
             for the total. Returns -1 if it is not possible
             to make change for the total using the given coins.
    """
    dq = deque([(0, 0)])
    visited = set()

    while dq:
        curr, changes = dq.popleft()

        if curr == total:
            return changes

        for coin in coins:
            if curr + coin not in visited and curr + coin <= total:
                dq.append((curr + coin, changes + 1))
                visited.add(curr + coin)

    return -1
