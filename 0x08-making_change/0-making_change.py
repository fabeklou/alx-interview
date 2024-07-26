#!/usr/bin/python3

"""
This module provides a function to calculate the minimum
number of coins needed to make change for a given total.
"""

def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed
    to make change for a given total.

    Args:
        coins (list): A list of coin denominations
            available.
        total (int): The total amount for which change
            needs to be made.

    Returns:
        int: The minimum number of coins needed to make
            change for the given total.

    Example:
        >>> coins = [1, 2, 5]
        >>> total = 11
        >>> makeChange(coins, total)
        3
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[total] == float('inf') else dp[total]
