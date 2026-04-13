"""Utility functions for Battleships

This module provides utility functions for the Battleships game, such as
generating random coordinates and creating the game grid.
"""

import random


def is_valid_coordinate(n: int, row: int, col: int) -> bool:
    """Check if the given row and column indices are valid for the grid.

    Arguments:
        n: int -- the size of the grid (n x n)
        row: int -- the row index to validate
        col: int -- the column index to validate

    Returns:
        True if the coordinates are valid, False otherwise.
    """
    pass


def generate_random_coordinate(n: int) -> tuple[int, int]:
    """Generate a random coordinate (row, column) within the bounds of
    the grid.

    Arguments:
        n: int -- the size of the grid (n x n)

    Returns:
        A tuple containing the row and column indices as integers.
    """
    pass
