#!/usr/bin/python3
"""Prime number game"""


def primeNumbers(n):
    """Determines the winner of a series of games played"""
    prime_nos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if filtered[prime]:
            prime_nos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return prime_nos


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
