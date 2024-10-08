#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
    grid (List[List[int]]): A list of list of integers where:
        - 0 represents water
        - 1 represents land

    Returns:
    int: The perimeter of the island

    The grid is completely surrounded by water, and there is only one island
    (or nothing). The island doesn't have "lakes" (water inside that isn't
    connected to the water surrounding the island).
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check cell above
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check cell below
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check cell to the left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check cell to the right
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
