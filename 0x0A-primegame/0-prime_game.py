#!/usr/bin/python3


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game for multiple rounds.

    :param x: number of rounds
    :param nums: array of n for each round
    :return: name of the player that won the most rounds, or None if it's a tie
    """

    def sieve_of_eratosthenes(n):
        """Generate primes up to n using the Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    def play_game(n):
        """Simulate a single game and return the winner."""
        primes = sieve_of_eratosthenes(n)
        moves = sum(1 for i in range(2, n + 1) if primes[i])
        return "Maria" if moves % 2 == 1 else "Ben"

    if not nums or x != len(nums):
        return None

    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
