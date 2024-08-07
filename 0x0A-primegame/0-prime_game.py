#!/usr/bin/python3

"""
This module contains a function for playing the prime game.

The prime game is a game where two players take turns
removing numbers from a list.
The numbers that can be removed are prime numbers
and their multiples.
The player who cannot make a move loses the game.
"""


def sieve(max_n):
    """
    Sieve of Eratosthenes algorithm to generate a list of prime
    numbers up to a given maximum number.

    Args:
        max_n (int): The maximum number up to which to generate
            the list of prime numbers.

    Returns:
        list: A list of prime numbers up to the given maximum number.
    """
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    prime_list = [p for p in range(2, max_n + 1) if is_prime[p]]
    return prime_list


def isWinner(x, nums):
    """
    Determines the winner of a prime game.

    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of integers representing
            the number of stones in each round.

    Returns:
        str: The name of the winner ('Maria' or 'Ben')
            or None if there is no winner.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve(max_num)

    def play_game(n):
        remaining = list(range(1, n + 1))
        player_turn = 0
        while True:
            move_made = False
            for prime in primes:
                if prime in remaining:
                    move_made = True
                    for multiple in range(prime, n + 1, prime):
                        if multiple in remaining:
                            remaining.remove(multiple)
                    break
            if not move_made:
                return player_turn
            player_turn = 1 - player_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = play_game(n)
            if winner == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
