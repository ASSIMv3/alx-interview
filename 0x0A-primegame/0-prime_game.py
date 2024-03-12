#!/usr/bin/python3
"""Prime number game"""


def primeNumbers(n):
    """Determines the winner of a series of games played"""
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return primes


def isWinner(x, nums):
    """Determines the winner of a series of games played"""
    if x is None or nums is None or x == 0 or not nums:
        return None

    maria = ben = 0
    for i in range(x):
        prime_nos = prime_numbers(nums[i])
        if len(prime_nos) % 2 == 0:
            ben += 1
        else:
            maria += 1
    
    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
