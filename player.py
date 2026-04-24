"""Game data: player

A player is represented as a dictionary containing their name, ship
board, attack board, and other relevant information.

E.g. a player dictionary might look like:
{
    'name': 'Player 1',
    # A grid representing the player's ships
    'ship_board': [...],
    # A grid representing the player's attacks on the opponent
    'attack_board': [...],
    # A dictionary to keep track of the player's ships and their lengths
    'ships': {'B': 1, 'C': 1, 'D': 1},
    # A counter to track the number of turns taken by the player
    'turns_taken': 0,
}
"""

import grid
import ship


class Human:
    """Class representing a human player in the Battleship game."""
    def __init__(
            self,
            name: str,
            ship_board: grid.ShipGrid,
            attack_board: grid.AttackGrid,
            ships: dict[str, ship.Ship],
    ):
        self.name = name
        self.ship_board = ship_board
        self.attack_board = attack_board
        self.ships = ships
        self.turns_taken = 0

    def take_turn(self) -> None:
        """Take a single turn.

        Returns:
            None
        """
        self.turns_taken += 1

    def update_attack(self, x: int, y: int, symbol: str) -> None:
        """Update the attacker's attack board based on the result of an
        attack.

        Arguments:
            x: int
                the horizontal coordinate of the attack
            y: int
                the vertical coordinate of the attack
            symbol: str
                the symbol to represent the attack result on the board

        Returns:
            None
        """
        self.attack_board.set(x, y, symbol)


    def update_defense(self, x: int, y: int, symbol: str) -> None:
        """Update the defender's ship board based on the result of an attack.

        Arguments:
            self: Player
                the player whose ship board is to be updated
            x: int
                the horizontal coordinate of the attack
            y: int
                the vertical coordinate of the attack
            symbol: str
                the symbol to represent the attack result on the board

        Returns:
            None
        """
        if symbol == "~":
            self.ship_board.set(x, y, "O")  # Miss
        else:
            self.ship_board.set(x, y, "X")  # Hit
            if (
                    symbol in self.ships
                    and not self.ships[symbol].is_sunk()
            ):
                self.ships[symbol].hit()

    def has_lost(self, max_turns: int) -> bool:
        """Check if the player has lost the game.
        A player loses when:
        - all of their ships have been sunk.
        - they have exceeded the maximum number of turns.

        Arguments:
            max_turns: int
                the maximum number of turns allowed for the player

        Returns:
            True if the player has lost, False otherwise.
        """
        if self.turns_taken >= max_turns:
            return True
        for player_ship in self.ships.values():
            if not player_ship.is_sunk():
                return False
        return True

    def get_input(self) -> tuple[int, int]:
        """Get the player's input for row and column.
        The function should validate the input to ensure it is within the 
        bounds of the grid.

        Arguments:
            size: int
                the size of the grid (n x n)

        Returns:
            A tuple containing the row and column indices as integers.
        """
        userinput = input("Enter row and column (e.g. '3 4'): ")
        while not self.is_input_valid(userinput):
            print(
                "Invalid input. Please enter row and column as two "
                "integers separated by a space."
            )
            userinput = input("Enter row and column (e.g. '3 4'): ")
        row_str, col_str = userinput.split()
        return int(row_str), int(col_str)

    def is_input_valid(self, input_str: str) -> bool:
        """Validate the player's input for row and column.

        Arguments:
            input_str: str
                the raw input string from the player
            size: int
                the size of the grid (n x n)

        Returns:
            True if the input is valid, False otherwise.
        """
        if not input_str.count(" ") == 1:
            return False
        row_str, col_str = input_str.split()
        if not (row_str.isdigit() and col_str.isdigit()):
            return False
        row, col = int(row_str), int(col_str)
        if (
                row < 0 or row >= self.ship_board.size
                or col < 0 or col >= self.ship_board.size
        ):
            return False
        return True


class Computer:
    """Class representing a computer player in the Battleship game."""

    def __init__(
            self,
            name: str,
            ship_board: grid.ShipGrid,
            attack_board: grid.AttackGrid,
            ships: dict[str, ship.Ship],
    ):
        self.name = name
        self.ship_board = ship_board
        self.attack_board = attack_board
        self.ships = ships
        self.turns_taken = 0

    def update_attack(self, x: int, y: int, symbol: str) -> None:
        """Update the attacker's attack board based on the result of an
        attack.

        Arguments:
            x: int
                the horizontal coordinate of the attack
            y: int
                the vertical coordinate of the attack
            symbol: str
                the symbol to represent the attack result on the board

        Returns:
            None
        """
        self.attack_board.set(x, y, symbol)

    def update_defense(self, x: int, y: int, symbol: str) -> None:
        """Update the defender's ship board based on the result of an attack.

        Arguments:
            self: Player
                the player whose ship board is to be updated
            x: int
                the horizontal coordinate of the attack
            y: int
                the vertical coordinate of the attack
            symbol: str
                the symbol to represent the attack result on the board

        Returns:
            None
        """
        if symbol == "~":
            self.ship_board.set(x, y, "O")  # Miss
        else:
            self.ship_board.set(x, y, "X")  # Hit
            if (
                    symbol in self.ships
                    and not self.ships[symbol].is_sunk()
            ):
                self.ships[symbol].hit()

    def has_lost(self, max_turns: int) -> bool:
        """Check if the player has lost the game.
        A player loses when:
        - all of their ships have been sunk.
        - they have exceeded the maximum number of turns.

        Arguments:
            max_turns: int
                the maximum number of turns allowed for the player

        Returns:
            True if the player has lost, False otherwise.
        """
        if self.turns_taken >= max_turns:
            return True
        for player_ship in self.ships.values():
            if not player_ship.is_sunk():
                return False
        return True


if __name__ == "__main__":
    pass
