"""Game data: ships

Ships are represented with the following data:
- name: str
  The name of the ship displayed to the player.
- symbol: str
  The character used to represent the ship on the grid.
- length: int
  The number of grid spaces the ship occupies.
"""


class Ship:
    """Represents a ship in Battleships.

    Each ship records information about the ship type, representation,
    and number of hits.
    """

    def __init__(self, name: str, symbol: str, length: int) -> None:
        self.name = name
        self.symbol = symbol
        self.length = length
        self.hits = 0

    def hit(self) -> None:
        """Register a hit on the ship.

        Returns:
            None
        """
        self.hits += 1


    def is_sunk(self) -> bool:
        """Check if the ship is sunk by comparing its hit counter to its length.

        Returns:
            True if the ship is sunk, False otherwise.
        """
        return self.hits >= self.length


def create_ship(name: str, symbol: str, length: int) -> Ship:
    """Create a ship with the given name, symbol, and length.

    Arguments:
        name: str -- the name of the ship
        symbol: str -- the character to represent the ship on the grid
        length: int -- the number of grid spaces the ship occupies

    Returns:
        A Ship object representing the ship.
    """
    return Ship(name, symbol, length)


def hit(ship: Ship) -> None:
    """Register a hit on the ship.

    Arguments:
        ship: Ship -- the ship to register the hit on

    Returns:
        None
    """
    ship.hits += 1


def is_sunk(ship: Ship) -> bool:
    """Check if the ship is sunk by comparing its hit counter to its length.

    Arguments:
        ship: Ship -- the ship to check

    Returns:
        True if the ship is sunk, False otherwise.
    """
    return ship.hits >= ship.length


if __name__ == "__main__":
    ship1 = Ship(
        "Battleship",
        "B",
        4
    )
    # ship1.name = "Battleship"
    # ship1.symbol = "B"
    # ship1.length = 4
    # ship1.hits = 0
    ship2 = Ship(
        "Battleship",
        "B",
        4
    )
