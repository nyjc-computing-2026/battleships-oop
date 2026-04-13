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

def get_player_input(size: int) -> tuple[int, int]:
    """Get the player's input for row and column.
    The function should validate the input to ensure it is within the 
    bounds of the grid.

    Arguments:
        None

    Returns:
        A tuple containing the row and column indices as integers.
    """
    pass


def create_player(name: str, size: int) -> dict:
    """Create a player with the given name and an empty grid.

    Arguments:
        name: str -- the name of the player
        size: int -- the size of the grid

    Returns:
        A dictionary representing the player, containing their name and grid.
        Format:
        {
            'name': str,
            'ship_board': list[list[str]],
            'attack_board': list[list[str]],
            'ships': dict[str, int],  # A dictionary to keep track of the player's ships and their lengths
            'turns_taken': int,  # A counter to track the number of turns taken by the player
        }
    """
    pass


def update_attack(
        attacker: dict,
        row: int,
        col: int,
        symbol: str
) -> None:
    """Update the attacker's attack board based on the result of an attack.

    Arguments:
        attacker: dict -- the player whose attack board is to be updated
        row: int -- the row index of the attack
        col: int -- the column index of the attack
        symbol: str -- the symbol to represent the attack result on the board

    Returns:
        None
    """
    pass


def update_defense(
        defender: dict,
        row: int,
        col: int,
        symbol: str
) -> None:
    """Update the defender's ship board based on the result of an attack.

    Arguments:
        defender: dict -- the player whose ship board is to be updated
        row: int -- the row index of the attack
        col: int -- the column index of the attack
        symbol: str -- the symbol to represent the attack result on the board

    Returns:
        None
    """
    pass


def has_player_lost(player: dict, max_turns: int) -> bool:
    """Check if the player has lost the game.
    A player loses when:
    - all of their ships have been sunk.
    - they have exceeded the maximum number of turns.

    Arguments:
        player: dict -- the player to check
        max_turns: int -- the maximum number of turns allowed for the player

    Returns:
        True if the player has lost, False otherwise.
    """
    pass
