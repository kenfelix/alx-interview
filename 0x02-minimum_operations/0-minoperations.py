#!/usr/bin/python3
"""Defines a function a method that calculates the fewest number of operations
"""


def minOperations(n):
    """Determines fewest number of operations needed to result in exactly n H characters in the file"""
    num_ops = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            num_ops += min_ops
            n /= min_ops
        min_ops += 1
    return num_ops
