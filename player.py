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


def create_player(
        name: str,
        ship_board: list[list[str]],  # grid
        attack_board: list[list[str]],  # grid
        ships: dict[str, dict],  # symbol: ship
) -> dict:
    """Create a player with the given name and an empty grid.

    Arguments:
        name: str
            the name of the player
        ship_board: list[list[str]]
            the player's ship board
        attack_board: list[list[str]]
            the player's attack board
        ships: dict[str, dict]
            a dictionary mapping ship symbols to their details

    Returns:
        A dictionary representing the player, containing their name and
        grid.
        Format:
        {
            'name': str,
            'ship_board': list[list[str]],
            'attack_board': list[list[str]],
            'ships': dict[str, dict],
            'turns_taken': int,
        }
    """
    return {
        'name': name,
        'ship_board': ship_board,
        'attack_board': attack_board,
        'ships': ships,
        'turns_taken': 0,
    }


def get_player_input(size: int) -> tuple[int, int]:
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
    while not is_input_valid(userinput, size):
        print(
            "Invalid input. Please enter row and column as two "
            "integers separated by a space."
        )
        userinput = input("Enter row and column (e.g. '3 4'): ")
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


def update_attack(
        attacker: dict,  # player
        x: int,
        y: int,
        symbol: str
) -> None:
    """Update the attacker's attack board based on the result of an
    attack.

    Arguments:
        attacker: dict
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
    attacker['attack_board'][x][y] = symbol


def update_defense(
        defender: dict,  # player
        x: int,
        y: int,
        symbol: str
) -> None:
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
        defender['ship_board'][x][y] = "O"  # Miss
    else:
        defender['ship_board'][x][y] = "X"  # Hit
        if (
                symbol in defender["ships"]
                and not ship.is_sunk(defender["ships"][symbol])
        ):
            ship.hit(defender["ships"][symbol])


def has_player_lost(player: dict, max_turns: int) -> bool:
    """Check if the player has lost the game.
    A player loses when:
    - all of their ships have been sunk.
    - they have exceeded the maximum number of turns.

    Arguments:
        player: dict
            the player to check
        max_turns: int
            the maximum number of turns allowed for the player

    Returns:
        True if the player has lost, False otherwise.
    """
    if player['turns_taken'] >= max_turns:
        return True
    for player_ship in player['ships'].values():
        if not ship.is_sunk(player_ship):
            return False
    return True


if __name__ == "__main__":
    pass
