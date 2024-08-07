#!/usr/bin/python3

"""
This module contains a function for playing the prime game.

The prime game is a game where two players take turns
removing numbers from a list.
The numbers that can be removed are prime numbers
and their multiples.
The player who cannot make a move loses the game.
"""


def find_primes(num):
    "find prime numbers up to num"
    if (type(num) is not int or num < 0):
        return None

    primes = []
    for candidate in range(2, num + 1):
        prime = True
        for divisor in range(2, candidate):
            if (candidate % divisor == 0):
                prime = False
                break
        if (prime):
            primes.append(candidate)
    return primes


def isWinner(x, nums):
    "find winner of the prime game"
    if (type(nums) is not list or not all([type(n) is int for n in nums]) or
            not all([n > -1 for n in nums])):
        return None

    if (type(x) is not int or x != len(nums)):
        return None

    nums.sort()
    primes = find_primes(nums[-1])
    if (primes is None):
        return None

    Maria_wins = 0
    Ben_wins = 0
    for n in nums:
        prime_count = 0
        for prime in primes:
            if (prime <= n):
                prime_count += 1
            else:
                break
        if prime_count % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1

    if (Maria_wins > Ben_wins):
        return "Maria"
    elif (Ben_wins > Maria_wins):
        return "Ben"
    else:
        return None
