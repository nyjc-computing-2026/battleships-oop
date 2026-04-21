"""Game data: player

Each player has two boards, and also tracks the status of their ships
and the number of turns taken.
"""

import grid
import ship


class Player:
    """Represents a player in Battleships.

    Each player records information about:
    - player's name
    - the player's ship board (containing ship positions)
    - the player's attack board (containing attack guesses and results)
    - the player's ship status (number hits) 
    """
    def __init__(
            self,
            name: str,
            ship_board: grid.Grid,
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

    def update_attack(
            self,
            x: int,
            y: int,
            symbol: str
    ) -> None:
        """Update the attacker's attack board based on the result of an
        attack.

        Arguments:
            attacker: Player
                the player whose attack board is to be updated
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

    def update_defense(
            self,
            x: int,
            y: int,
            symbol: str
    ) -> None:
        """Update the defender's ship board based on the result of an attack.

        Arguments:
            defender: Player
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


def create_player(
        name: str,
        ship_board: grid.Grid,  # grid
        attack_board: grid.Grid,  # grid
        ships: dict[str, ship.Ship],  # symbol: ship
) -> Player:
    """Create a player with the given name and an empty grid.

    Arguments:
        name: str
            the name of the player
        ship_board: grid.Grid
            the player's ship board
        attack_board: grid.Grid
            the player's attack board
        ships: dict[str, Ship]
            a dictionary mapping ship symbols to their details

    Returns:
        A dictionary representing the player, containing their name and
        grid.
        Format:
        {
            'name': str,
            'ship_board': list[list[str]],
            'attack_board': list[list[str]],
            'ships': {
                "B": ...
                "C": ...
                "D": ...
            },
            'turns_taken': int,
        }
    """
    player = Player(name, ship_board, attack_board, ships)
    return player
    p1 = Player(name, ship_board, attack_board, ships)
    return p1


def get_player_input(size: int) -> tuple[int, int]:
    """Get the player's input for row and column.
    The function should validate the input to ensure it is within the 
    bounds of the grid.

    Arguments:
        size: int
            the size of the grid (n x n)

    Returns:
        A tuple containing the x and y coordinates as integers.
    """
    userinput = input("Enter x and y coordinates (e.g. '3 4'): ")
    while not is_input_valid(userinput, size):
        print(
            "Invalid input. Please enter x and y coordinates as two "
            "integers separated by a space."
        )
        userinput = input("Enter x and y coordinates (e.g. '3 4'): ")
    row_str, col_str = userinput.split()
    return int(row_str), int(col_str)



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


if __name__ == "__main__":
    pass
