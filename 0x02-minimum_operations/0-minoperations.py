#!/usr/bin/python3

"""Calculate the minimum number of operations
required to reach a given number.
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations required
    to reach a given number.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations required.

    """
    if n <= 0:
        return 0

    prime = 2
    operations = 0

    while n > 1:
        while n % prime == 0:
            n //= prime
            operations += prime
        prime += 1

    return operations
