"""Battleship Game"""

import grid
import player
import ship
import utility

# Game data (global)
# This section defines the global data used in the game

MAX_TURNS = 30


# Main game loop

def main() -> None:
    """Main function to run the Battleship game."""
    grid_size = 10
    max_turns = 30
    computer = player.create_player(
        name="Computer",
        ship_board=grid.create_grid(n=grid_size, placeholder="~"),
        attack_board=grid.create_grid(n=grid_size, placeholder="~"),
        ships={
            "B": ship.create_ship(name="Battleship", symbol="B", length=4),
            "C": ship.create_ship(name="Cruiser", symbol="C", length=3),
            "D": ship.create_ship(name="Destroyer", symbol="D", length=2)
        }
    )
    human = player.create_player(
        name="Player",
        ship_board=grid.create_grid(n=grid_size, placeholder="~"),
        attack_board=grid.create_grid(n=grid_size, placeholder="~"),
        ships={
            "B": ship.create_ship(name="Battleship", symbol="B", length=4),
            "C": ship.create_ship(name="Cruiser", symbol="C", length=3),
            "D": ship.create_ship(name="Destroyer", symbol="D", length=2)
        }
    )

    # Game setup: populate ship boards and initialize attack boards
    grid.initialize_grid(
        grid=computer.ship_board,
        ships=list(computer.ships.values()),
    )
    grid.initialize_grid(
        grid=human.ship_board,
        ships=list(human.ships.values()),
    )
    human.turns_taken = 0
    computer.turns_taken = 0

    # Game loop
    while (
            not human.has_player_lost(max_turns)
            and not computer.has_player_lost(max_turns)
    ):
        # Player's turn
        print(f"{human.name}'s turn:")
        # Show player's board before input
        human.attack_board.display()
        row, col = player.get_player_input(grid_size)
        # Process human's attack on computer's grid
        hit_char = grid.get_grid_coordinate_char(computer.ship_board, row, col)
        if hit_char in computer.ships:
            message = f"Hit! {human.name} hit {computer.name}'s {computer.ships[hit_char].name}!"
            human.update_attack(row, col, hit_char)
            computer.update_defense(row, col, hit_char)
        else:
            message = f"{human.name} missed!"
            human.update_attack(row, col, "O")
            computer.update_defense(row, col, "O")
        print(message)
        human.turns_taken += 1

        # Computer's turn
        print(f"{computer.name}'s turn:")
        row, col = utility.generate_random_coordinate(computer.ship_board.size)
        # Process computer's attack on human's grid
        hit_char = grid.get_grid_coordinate_char(human.ship_board, row, col)
        if hit_char in human.ships:
            message = f"Hit! {computer.name} hit {human.name}'s {human.ships[hit_char].name}!"
            computer.update_attack(row, col, hit_char)
            human.update_defense(row, col, hit_char)
        else:
            message = f"{computer.name} missed!"
            computer.update_attack(row, col, "O")
            human.update_defense(row, col, "O")
        # Show player's ship board after input
        human.ship_board.display()
        print(message)
        computer.turns_taken += 1


if __name__ == "__main__":
    main()
