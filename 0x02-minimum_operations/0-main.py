#!/usr/bin/python3

"""
Main file for testing
"""


minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 17
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 31
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 0
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 400
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 997
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 993
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 4000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9999
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 98000  # segfault using dp
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 0
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = -100000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


# can only work with prime factor approach

n = 100_000_000  # segfault using dp
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100_000_000_000  # segfault using dp
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100_000_000_001  # segfault using dp
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100_000_000_000_000  # segfault using dp
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100_000_000_000_001  # segfault using dp
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100_000_000_000_000_000  # segfault using dp
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100_000_000_000_000_000_000  # segfault using dp
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


# expected outputs:
"""
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
Min # of operations to reach 17 char: 17
Min # of operations to reach 31 char: 31
Min # of operations to reach 0 char: 0
Min # of operations to reach 1 char: 0
Min # of operations to reach 100 char: 14
Min # of operations to reach 400 char: 18
Min # of operations to reach 1000 char: 21
Min # of operations to reach 997 char: 997
Min # of operations to reach 993 char: 334
Min # of operations to reach 2000 char: 23
Min # of operations to reach 4000 char: 25
Min # of operations to reach 9999 char: 118
Min # of operations to reach 98000 char: 37
Min # of operations to reach 0 char: 0
Min # of operations to reach -100000 char: 0
Min # of operations to reach 100000000 char: 56
Min # of operations to reach 100000000000 char: 77
Min # of operations to reach 100000000001 char: 12917
Min # of operations to reach 100000000000000 char: 98
Min # of operations to reach 100000000000001 char: 121499860
Min # of operations to reach 100000000000000000 char: 119
Min # of operations to reach 100000000000000000000 char: 140
"""