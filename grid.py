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


class Grid:
    """Class representing a grid in the Battleship game."""

    def __init__(self, size: int, placeholder: str):
        self.size = size
        self.placeholder = placeholder
        self.data = []
        for _ in range(size):
            row = [placeholder] * size
            self.data.append(row)

    def get(self, x: int, y: int) -> str:
        """Get the character at the specified grid coordinates.

        Arguments:
            x: int
                the horizontal coordinate
            y: int
                the vertical coordinate
        
        Returns:
            The character at the specified coordinates on the grid.
        """
        return self.data[y][x]

    def set(self, x: int, y: int, value: str) -> None:
        """Set the character at the specified grid coordinates.

        Arguments:
            x: int
                the horizontal coordinate
            y: int
                the vertical coordinate
            value: str
                the character to set at the specified coordinates
        
        Returns:
            None
        """
        self.data[y][x] = value

    def display(self) -> None:
        """Display the grid in a readable format."""
        for row in self.data:
            print(" ".join(row))


def get_grid_coordinate_char(grid: Grid, x: int, y: int) -> str:
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
    return grid.data[x][y]


def initialize_grid(grid: Grid, ships: list[ship.Ship]) -> None:
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
        x, y = utility.generate_random_coordinate(grid.size)
        orientation = utility.generate_random_orientation()
        # Keep trying to place the ship until it is successfully placed
        # on the grid
        while not place_ship_on_grid(grid, ship, x, y, orientation):
            x, y = utility.generate_random_coordinate(grid.size)
            orientation = utility.generate_random_orientation()


def is_valid_coordinate(grid: Grid, x: int, y: int) -> bool:
    """Check if the given coordinates are valid for the grid.

    Arguments:
        grid: Grid
        x: int
            the row index to validate
        y: int
            the column index to validate

    Returns:
        True if the coordinates are valid, False otherwise.
    """
    if x < 0 or x >= grid.size or y < 0 or y >= grid.size:
        return False
    return True


def place_ship_on_grid(
        grid: Grid,
        ship: ship.Ship,
        x: int,
        y: int,
        orientation: str
) -> bool:
    """Place a ship on the grid at the specified coordinates.

    Arguments:
        grid: Grid -- the game grid
        ship: Ship -- the ship to place on the grid
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
        grid: Grid,
        ship: ship.Ship,
        x: int,
        y: int,
) -> bool:
    """Place a ship on the grid at the specified coordinates
    horizontally (rightwards).

    Arguments:
        grid: list[list[str]] -- the game grid
        ship: dict -- the ship to place on the grid
        x: int -- the row index for the starting coordinate
        y: int -- the column index for the starting coordinate
    
    Returns:
        True if the ship was successfully placed, False if placement
        failed due to out-of-bounds or overlap with existing ships.
    """
    for i in range(ship.length):
        if not is_valid_coordinate(grid, x, y + i) or grid.data[x][y + i] != '~':
            return False
    for i in range(ship.length):
        grid.data[x][y + i] = ship.symbol
    return True


def place_ship_on_grid_vertically(
        grid: Grid,
        ship: ship.Ship,
        x: int,
        y: int,
) -> bool:
    """Place a ship on the grid at the specified coordinates vertically
    (downwards).

    Arguments:
        grid: list[list[str]] -- the game grid
        ship: dict -- the ship to place on the grid
        x: int -- the row index for the starting coordinate
        y: int -- the column index for the starting coordinate
    
    Returns:
        True if the ship was successfully placed, False if placement
        failed due to out-of-bounds or overlap with existing ships.
    """
    for i in range(ship.length):
        if (
                not is_valid_coordinate(grid, x + i, y)
                or grid.data[x + i][y] != '~'
        ):
            return False
    for i in range(ship.length):
        grid.data[x + i][y] = ship.symbol
    return True


if __name__ == "__main__":
    pass
