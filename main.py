"""Battleship Game"""

import grid
import player
import utility

# Game data (global)
# This section defines the global data structures used in the game, such
# as the ships and their properties.

BATTLESHIP = {
    "name": "Battleship",
    "symbol": "B",
    "length": 4,
}
CRUISER = {
    "name": "Cruiser",
    "symbol": "C",
    "length": 3,
}
DESTROYER = {
    "name": "Destroyer",
    "symbol": "D",
    "length": 2,
}
SHIP = {
    "B": BATTLESHIP,
    "C": CRUISER,
    "D": DESTROYER,
}

MAX_TURNS = 30


# Main game loop

def main() -> None:
    """Main function to run the Battleship game."""
    grid_size = 10
    max_turns = 30
    computer = player.create_player("Computer", grid_size)
    human = player.create_player("Player", grid_size)

    # Game setup: populate ship boards and initialize attack boards
    grid.initialize_grid(computer["ship_board"], ["B", "C", "D"])
    grid.initialize_grid(human["ship_board"], ["B", "C", "D"])
    human["turns_taken"] = 0
    computer["turns_taken"] = 0

    # Game loop
    while (
            not player.has_player_lost(human, max_turns)
            and not player.has_player_lost(computer, max_turns)
    ):
        # Player's turn
        print(f"{human['name']}'s turn:")
        grid.display_grid(human['attack_board'])
        row, col = player.get_player_input(grid_size)
        # Process human's attack on computer's grid
        hit_char = grid.get_grid_coordinate_char(computer['ship_board'], row, col)
        if hit_char in SHIP:
            print(f"Hit! You hit the computer's {SHIP[hit_char]['name']}!")
            player.update_attack(human, row, col, hit_char)
            player.update_defense(computer, row, col, "X")
        else:
            print("Miss!")
            player.update_attack(human, row, col, "O")
            player.update_defense(computer, row, col, "O")  # Mark miss on
        human["turns_taken"] += 1

        # Computer's turn
        print(f"{computer['name']}'s turn:")
        grid.display_grid(computer['attack_board'])
        row, col = utility.generate_random_coordinate(len(computer['ship_board']))
        # Process computer's attack on human's grid
        hit_char = grid.get_grid_coordinate_char(human['ship_board'], row, col)
        if hit_char in SHIP:
            print(f"Computer hit your {SHIP[hit_char]['name']}!")
            player.update_attack(computer, row, col, hit_char)
            player.update_defense(human, row, col, "X")
        else:
            print("Computer missed!")
            player.update_attack(computer, row, col, "O")
            player.update_defense(human, row, col, "O")
        computer["turns_taken"] += 1


if __name__ == "__main__":
    main()
