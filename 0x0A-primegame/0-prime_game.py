#!/usr/bin/python3
"""Prime number game"""


def is_winner(x, nums):
    """Determines the winner of a series of games played"""

    def get_primes(n):
        """Generates prime numbers up to a given number"""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                sieve[i * i:n + 1:i] = [False] * len(sieve[i * i:n + 1:i])
        return [i for i in range(n + 1) if sieve[i]]

    primes = [0] + get_primes(max(nums) * 2)

    def can_win(n):
        """Determines if a player can win a game for a given upper limit n"""
        primes_count = sum(1 for p in primes if p <= n)
        return primes_count % 2 != 0

    maria_wins = sum(can_win(n) for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
