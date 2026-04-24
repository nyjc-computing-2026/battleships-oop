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
    """Class representing a ship in the Battleship game."""
    def __init__(self, name: str, symbol: str, length: int):
        self.name = name
        self.symbol = symbol
        self.length = length
        self.hits = 0  # A counter to track the number of hits the ship has taken


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
    pass
