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

def create_grid(n: int, placeholder: str) -> list[list[str]]:
    """Create a n-by-n grid.
    The grid is represented as a list of lists.
    Each inner list represents a row.
    Each row is filled with the placeholder character.

    Arguments:
        n: int -- the size of the grid (n x n)
        placeholder: str -- the character to fill the grid with

    Returns:
        A nested list representing the grid.
    """
    pass


def display_grid(grid: list[list[str]]) -> None:
    """Display the grid in a readable format."""
    pass


def initialize_grid(grid: list[list[str]], ships: list[str]) -> None:
    """Initialize the grid by placing ships randomly on the grid.

    Arguments:
        grid: list[list[str]] -- the game grid to initialize
        ships: list[str] -- a list of ship symbols to place on the grid
    
    Returns:
        None
    """
    pass


def get_grid_coordinate_char(grid: list[list[str]], x: int, y: int) -> str:
    """Get the character at the specified grid coordinates.

    Arguments:
        grid: list[list[str]] -- the game grid
        x: int -- the row index
        y: int -- the column index
    
    Returns:
        The character at the specified coordinates on the grid.
    """
    pass
