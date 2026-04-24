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
    """Base class for all grid types in the Battleship game."""

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

    def is_valid_coordinate(self, x: int, y: int) -> bool:
        """Check if the given coordinates are valid for the grid.

        Arguments:
            x: int
                the row index to validate
            y: int
                the column index to validate

        Returns:
            True if the coordinates are valid, False otherwise.
        """
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False
        return True


class AttackGrid(Grid):
    """Class representing an attack grid in the Battleship game."""


class ShipGrid(Grid):
    """Class representing a ship grid in the Battleship game."""

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

    def is_valid_coordinate(self, x: int, y: int) -> bool:
        """Check if the given coordinates are valid for the grid.

        Arguments:
            x: int
                the row index to validate
            y: int
                the column index to validate

        Returns:
            True if the coordinates are valid, False otherwise.
        """
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False
        return True

    def initialize_grid(self, ships: list[ship.Ship]) -> None:
        """Initialize the grid by placing ships randomly on the grid.

        Arguments:
            ships: list[Ship]
                a list of ships to place on the grid
        
        Returns:
            None
        """
        for ship in ships:
            x, y = utility.generate_random_coordinate(self.size)
            orientation = utility.generate_random_orientation()
            # Keep trying to place the ship until it is successfully placed
            # on the grid
            while not self.place_ship_on_grid(ship, x, y, orientation):
                x, y = utility.generate_random_coordinate(self.size)
                orientation = utility.generate_random_orientation()


    def place_ship_on_grid(
            self,
            ship: ship.Ship,
            x: int,
            y: int,
            orientation: str
    ) -> bool:
        """Place a ship on the grid at the specified coordinates.

        Arguments:
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
            return self.place_ship_on_grid_horizontally(ship, x, y)
        elif orientation == 'vertical':
            return self.place_ship_on_grid_vertically(ship, x, y)
        else:
            raise ValueError(
                "Invalid orientation. Must be 'horizontal' or 'vertical'."
            )


    def place_ship_on_grid_horizontally(
            self,
            ship: ship.Ship,
            x: int,
            y: int,
    ) -> bool:
        """Place a ship on the grid at the specified coordinates
        horizontally (rightwards).

        Arguments:
            ship: Ship -- the ship to place on the grid
            x: int -- the row index for the starting coordinate
            y: int -- the column index for the starting coordinate
        
        Returns:
            True if the ship was successfully placed, False if placement
            failed due to out-of-bounds or overlap with existing ships.
        """
        for i in range(ship.length):
            if not self.is_valid_coordinate(x, y + i) or self.get(x, y + i) != '~':
                return False
        for i in range(ship.length):
            self.set(x, y + i, ship.symbol)
        return True


    def place_ship_on_grid_vertically(
            self,
            ship: ship.Ship,
            x: int,
            y: int,
    ) -> bool:
        """Place a ship on the grid at the specified coordinates vertically
        (downwards).

        Arguments:
            ship: Ship -- the ship to place on the grid
            x: int -- the row index for the starting coordinate
            y: int -- the column index for the starting coordinate
        
        Returns:
            True if the ship was successfully placed, False if placement
            failed due to out-of-bounds or overlap with existing ships.
        """
        for i in range(ship.length):
            if (
                    not self.is_valid_coordinate(x + i, y)
                    or self.get(x + i, y) != '~'
            ):
                return False
        for i in range(ship.length):
            self.set(x + i, y, ship.symbol)
        return True


if __name__ == "__main__":
    pass
