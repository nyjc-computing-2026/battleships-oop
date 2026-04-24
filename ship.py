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

    def hit(self) -> None:
        """Register a hit on the ship."""
        self.hits += 1

    def is_sunk(self) -> bool:
        """Check if the ship is sunk by comparing its hit counter to its length.

        Returns:
            bool -- True if the ship is sunk, False otherwise.
        """
        return self.hits >= self.length


if __name__ == "__main__":
    pass
