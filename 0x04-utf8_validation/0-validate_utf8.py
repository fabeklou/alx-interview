#!/usr/bin/python3

"""
This module provides a function to validate whether
a given list of integers represents a valid UTF-8 encoding.

The function `validUTF8` takes a list of 8bits integers as input
and checks if it represents a valid UTF-8 encoding.
It returns True if the encoding is valid, and False otherwise.

Example usage:
data = [197, 130, 1]
# Represents the UTF-8 encoding of the character 'Ç'
result = validUTF8(data)
print(result)
# Output: True

Note: This function assumes that the input list contains
only valid integers in the range of 0 to 255.
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determines if a given list of integers represents
    a valid UTF-8 encoding.

    Args:
        data (list): A list of integers
            representing UTF-8 encoded characters.

    Returns:
        bool: True if the data represents a valid UTF-8 encoding,
            False otherwise.
    """

    def is_valid(index, count):
        """
        Helper function to check if a sequence of bytes
        starting at the given index is valid.

        Args:
            index (int): The starting index of the sequence.
            count (int): The number of bytes in the sequence.

        Returns:
            bool: True if the sequence is valid, False otherwise.
        """
        for _ in range(count):
            if index >= len(data):
                return False
            bits = data[index]
            if bits >> 6 != 2:
                return False
            index += 1
        return True

    cursor = 0
    while cursor < len(data):
        bits = data[cursor] >> 3

        if bits == 30:
            if not is_valid(cursor + 1, 3):
                return False
            cursor += 4
        elif bits >> 1 == 14:
            if not is_valid(cursor + 1, 2):
                return False
            cursor += 3
        elif bits >> 2 == 6:
            if not is_valid(cursor + 1, 1):
                return False
            cursor += 2
        elif bits >> 4 == 0:
            cursor += 1
        else:
            return False

    return True
