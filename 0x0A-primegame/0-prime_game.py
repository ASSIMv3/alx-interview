#!/usr/bin/python3
"""Prime number game"""


def is_prime(n):
    """Determines the winner of a series of games played"""
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_winner(x, nums):
    """Determines the winner of a series of games played"""
    players = {'Maria': 0, 'Ben': 0}
    for round in range(x):
        n = nums[round]

        winner = 1
        i = 2
        while i <= n:
            while (i <= n + 1) and (not is_prime(i)):
                i += 1
            if i > n:
                break
            winner += 1
            i += 1

        if winner % 2 == 0:
            players['Maria'] += 1
        else:
            players['Ben'] += 1

    if players['Ben'] < players['Maria']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return None
