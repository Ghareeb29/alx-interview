#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.

This module contains a function that calculates the perimeter of an island
represented by 1's in a grid of 0's and 1's.
"""


def island_perimeter(grid):
    """
    Calculate and return the perimeter of the island in the grid.

    The grid represents water by 0 and land by 1. The grid cells are
    connected horizontally/vertically (not diagonally). The grid is
    rectangular, with its width and height not exceeding 100. The grid
    is completely surrounded by water, and there is one island (or nothing).
    The island doesn't have "lakes" (water inside that isn't connected to
    the water surrounding the island).

    Args:
        grid (List[List[int]]): A list of list of integers representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1:  # If it's a land cell
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:  # Check cell above
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Check cell to the left
                    perimeter -= 2

    return perimeter
