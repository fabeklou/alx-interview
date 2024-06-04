#!/usr/bin/python3

"""This module contains the canUnlockAll function"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened
    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    """
    keys = set(boxes[0])
    boxes[0] = None  # first boxe visited and his keys were collected

    while keys:
        for key in tuple(keys):
            if boxes[key] is not None:
                keys = keys | set(boxes[key])
                boxes[key] = None
            keys.remove(key)

    for boxe in boxes:
        if boxe is not None:
            return False

    return True
