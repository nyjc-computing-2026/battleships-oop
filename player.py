"""Game data: player

Each player has two boards, and also tracks the status of their ships
and the number of turns taken.
"""

import grid
import ship
import utility


class Human:
    """Represents the human player in Battleships.

    Each player records information about:
    - name
    - ship board, containing the ship layout
    - attack board, containing the player's guesses and results
    - ships, containing ship status
    """
    def __init__(
            self,
            name: str,
            ship_board: grid.ShipGrid,
            attack_board: grid.Grid,
            ships: dict[str, ship.Ship],
    ) -> None:
        self.name = name
        self.ship_board = ship_board
        self.attack_board = attack_board
        self.ships = ships
        self.turns_taken = 0

    def has_player_lost(self, max_turns: int) -> bool:
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

    def take_turn(self) -> None:
        """Increment the player's turn count by one."""
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
            defender: dict
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

    def get_input(self) -> tuple[int, int]:
        """Get the player's input for row and column.
        The function should validate the input to ensure it is within the 
        bounds of the grid.

        Returns:
            A tuple containing the row and column indices as integers.
        """
        userinput = input("Enter row and column (e.g. '3 4'): ")
        while not is_input_valid(userinput, self.attack_board.size):
            print(
                "Invalid input. Please enter row and column as two "
                "integers separated by a space."
            )
            userinput = input("Enter row and column (e.g. '3 4'): ")
        row_str, col_str = userinput.split()
        return int(row_str), int(col_str)


class Computer:
    """Represents the computer player in Battleships.

    Each player records information about:
    - name
    - ship board, containing the ship layout
    - attack board, containing the player's guesses and results
    - ships, containing ship status
    """

    def __init__(
            self,
            name: str,
            ship_board: grid.ShipGrid,
            attack_board: grid.Grid,
            ships: dict[str, ship.Ship],
    ) -> None:
        self.name = name
        self.ship_board = ship_board
        self.attack_board = attack_board
        self.ships = ships
        self.turns_taken = 0

    def has_player_lost(self, max_turns: int) -> bool:
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

    def take_turn(self) -> None:
        """Increment the player's turn count by one."""
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
            defender: dict
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

    def get_input(self) -> tuple[int, int]:
        """Get the player's input for row and column.
        The function should validate the input to ensure it is within the 
        bounds of the grid.

        Returns:
            A tuple containing the row and column indices as integers.
        """
        return utility.generate_random_coordinate(self.ship_board.size)

def is_input_valid(input_str: str, size: int) -> bool:
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
    if row < 0 or row >= size or col < 0 or col >= size:
        return False
    return True
