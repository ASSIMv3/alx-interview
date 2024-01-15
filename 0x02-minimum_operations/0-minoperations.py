#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Function minimum operations, Returns an integer"""
    result = 0
    minOp = 2
    while n > 1:
        while n % minOp == 0:
            result += minOp
            n /= minOp
        minOp += 1
    return result