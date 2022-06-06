#!/usr/bin/python3
"""perimeter Module"""


def island_perimeter(grid) -> int:
    """ returns the perimeter of the island described in grid"""
    new = []
    for i in grid:
        for j in i:
            if j == 1:
                new.append(j)

    perimeter = 2 + 2 * len(new)

    return perimeter
