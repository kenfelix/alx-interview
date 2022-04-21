#!/usr/bin/python3
"""Defines a function a method that calculates the fewest number of operations
"""


def minOperations(n):
    """Determines fewest number of operations needed to result in exactly n H characters in the file"""
    ops = 0
    H = 1
    cpAll = 0

    while H != n:
        if n % H == 0:
            cpAll = H
            H = H + cpAll
            ops = ops + 2
        else:
            H = H + cpAll
            ops = ops + 1
    return ops
