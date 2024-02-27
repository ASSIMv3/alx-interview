#!/usr/bin/python3
"""0-making_change Module"""


def makeChange(coins, total):
    """Return fewest number of coins needed to meet total"""
    temp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0
    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin
    return temp_value if total == 0 else -1