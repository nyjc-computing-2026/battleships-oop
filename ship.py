"""Game data: ships

Ships are represented with the following data:
- name: str
  The name of the ship displayed to the player.
- symbol: str
  The character used to represent the ship on the grid.
- length: int
  The number of grid spaces the ship occupies.
"""


def create_ship(name: str, symbol: str, length: int) -> dict:
    """Create a ship with the given name, symbol, and length.

    Arguments:
        name: str -- the name of the ship
        symbol: str -- the character to represent the ship on the grid
        length: int -- the number of grid spaces the ship occupies

    Returns:
        A dictionary representing the ship, containing its name, symbol, and length.
        Format:
        {
            'name': str,
            'symbol': str,
            'length': int,
            'hits': int,  # A counter to track the number of hits the ship has taken
        }
    """
    return {
        'name': name,
        'symbol': symbol,
        'length': length,
        'hits': 0,
    }


def hit(ship: dict) -> None:
    """Register a hit on the ship.

    Arguments:
        ship: dict -- the ship to register the hit on

    Returns:
        None
    """
    ship['hits'] += 1


def is_sunk(ship: dict) -> bool:
    """Check if the ship is sunk by comparing its hit counter to its length.

    Arguments:
        ship: dict -- the ship to check

    Returns:
        True if the ship is sunk, False otherwise.
    """
    return ship['hits'] >= ship['length']


if __name__ == "__main__":
    pass