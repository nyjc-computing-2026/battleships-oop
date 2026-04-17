"""Game data: grid

Grids are represented as nested lists (list of lists), where each
inner list represents a row of the grid.

E.g. a 5x5 grid filled with '~' would look like:
[
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~'],
]
"""

import ship
import utility


def create_grid(n: int, placeholder: str) -> list[list[str]]:
    """Create a n-by-n grid.
    The grid is represented as a list of lists.
    Each inner list represents a row.
    Each row is filled with the placeholder character.

    Arguments:
        n: int
            the size of the grid (n x n)
        placeholder: str
            the character to fill the grid with

    Returns:
        A nested list representing the grid.
    """
    grid = []
    for _ in range(n):
        row = [placeholder] * n
        grid.append(row)
    return grid


def display_grid(grid: list[list[str]]) -> None:
    """Display the grid in a readable format."""
    for row in grid:
        print(" ".join(row))


def get_grid_coordinate_char(grid: list[list[str]], x: int, y: int) -> str:
    """Get the character at the specified grid coordinates.

    Arguments:
        grid: list[list[str]]
        x: int
            the horizontal coordinate
        y: int
            the vertical coordinate
    
    Returns:
        The character at the specified coordinates on the grid.
    """
    return grid[x][y]


def initialize_grid(grid: list[list[str]], ships: list[dict]) -> None:
    """Initialize the grid by placing ships randomly on the grid.

    Arguments:
        grid: list[list[str]]
            the game grid to initialize
        ships: list[dict]
            a list of ships to place on the grid
    
    Returns:
        None
    """
    for ship in ships:
        x, y = utility.generate_random_coordinate(len(grid))
        orientation = utility.generate_random_orientation()
        # Keep trying to place the ship until it is successfully placed
        # on the grid
        while not place_ship_on_grid(grid, ship, x, y, orientation):
            x, y = utility.generate_random_coordinate(len(grid))
            orientation = utility.generate_random_orientation()


def is_valid_coordinate(grid: list[list[str]], x: int, y: int) -> bool:
    """Check if the given coordinates are valid for the grid.

    Arguments:
        grid: list[list[str]]
        x: int
            the row index to validate
        y: int
            the column index to validate

    Returns:
        True if the coordinates are valid, False otherwise.
    """
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid):
        return False
    return True


def place_ship_on_grid(
        grid: list[list[str]],
        ship: dict,
        x: int,
        y: int,
        orientation: str
) -> bool:
    """Place a ship on the grid at the specified coordinates.

    Arguments:
        grid: list[list[str]] -- the game grid
        ship: dict -- the ship to place on the grid
        x: int -- the row index for the starting coordinate
        y: int -- the column index for the starting coordinate
        orientation: str -- the orientation of the ship ('horizontal' or
            'vertical')
    
    Returns:
        True if the ship was successfully placed, False if placement
        failed due to out-of-bounds or overlap with existing ships.
    """
    if orientation == 'horizontal':
        return place_ship_on_grid_horizontally(grid, ship, x, y)
    elif orientation == 'vertical':
        return place_ship_on_grid_vertically(grid, ship, x, y)
    else:
        raise ValueError(
            "Invalid orientation. Must be 'horizontal' or 'vertical'."
        )


def place_ship_on_grid_horizontally(
        grid: list[list[str]],
        ship: ship.Ship,
        x: int,
        y: int,
) -> bool:
    """Place a ship on the grid at the specified coordinates
    horizontally (rightwards).

    Arguments:
        grid: list[list[str]] -- the game grid
        ship: Ship -- the ship to place on the grid
        x: int -- the row index for the starting coordinate
        y: int -- the column index for the starting coordinate
    
    Returns:
        True if the ship was successfully placed, False if placement
        failed due to out-of-bounds or overlap with existing ships.
    """
    for i in range(ship.length):
        if not is_valid_coordinate(grid, x, y + i) or grid[x][y + i] != '~':
            return False
    for i in range(ship.length):
        grid[x][y + i] = ship.symbol
    return True


def place_ship_on_grid_vertically(
        grid: list[list[str]],
        ship: ship.Ship,
        x: int,
        y: int,
) -> bool:
    """Place a ship on the grid at the specified coordinates vertically
    (downwards).

    Arguments:
        grid: list[list[str]] -- the game grid
        ship: Ship -- the ship to place on the grid
        x: int -- the row index for the starting coordinate
        y: int -- the column index for the starting coordinate
    
    Returns:
        True if the ship was successfully placed, False if placement
        failed due to out-of-bounds or overlap with existing ships.
    """
    for i in range(ship.length):
        if (
                not is_valid_coordinate(grid, x + i, y)
                or grid[x + i][y] != '~'
        ):
            return False
    for i in range(ship.length):
        grid[x + i][y] = ship.symbol
    return True


if __name__ == "__main__":
    pass
