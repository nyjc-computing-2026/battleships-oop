"""Battleship Game"""

import grid
import player
import ship
import utility

# Game data (global)
# This section defines the global data used in the game

MAX_TURNS = 30
PLACEHOLDER = "~"


# Main game loop

def main() -> None:
    """Main function to run the Battleship game."""
    grid_size = 10
    max_turns = 30
    computer = player.Computer(
        name="Computer",
        ship_board=grid.ShipGrid(size=grid_size, placeholder="~"),
        attack_board=grid.AttackGrid(size=grid_size, placeholder="~"),
        ships={
            "B": ship.Ship(name="Battleship", symbol="B", length=4),
            "C": ship.Ship(name="Cruiser", symbol="C", length=3),
            "D": ship.Ship(name="Destroyer", symbol="D", length=2)
        }
    )
    human = player.Human(
        name="Player",
        ship_board=grid.ShipGrid(size=grid_size, placeholder="~"),
        attack_board=grid.AttackGrid(size=grid_size, placeholder="~"),
        ships={
            "B": ship.Ship(name="Battleship", symbol="B", length=4),
            "C": ship.Ship(name="Cruiser", symbol="C", length=3),
            "D": ship.Ship(name="Destroyer", symbol="D", length=2)
        }
    )

    # Game setup: populate ship boards and initialize attack boards
    computer.ship_board.initialize_grid(
        ships=list(computer.ships.values()),
    )
    human.ship_board.initialize_grid(
        ships=list(human.ships.values()),
    )

    # Game loop
    while (
            not human.has_lost(max_turns)
            and not computer.has_lost(max_turns)
    ):
        # Player's turn
        print(f"{human.name}'s turn:")
        # Show player's board before input
        human.attack_board.display()
        x, y = human.get_input()
        # Process human's attack on computer's grid
        hit_char = computer.ship_board.get(x, y)
        if hit_char in computer.ships:
            message = f"Hit! {human.name} hit {computer.name}'s {computer.ships[hit_char].name}!"
            human.update_attack(x, y, hit_char)
            human.update_defense(x, y, hit_char)
        else:
            message = f"{human.name} missed!"
            human.update_attack(x, y, "O")
            human.update_defense(x, y, "O")
        print(message)
        human.turns_taken += 1

        # Computer's turn
        print(f"{computer.name}'s turn:")
        x, y = utility.generate_random_coordinate(len(computer.ship_board.data))
        # Process computer's attack on human's grid
        hit_char = computer.ship_board.get(x, y)
        if hit_char in human.ships:
            message = f"Hit! {computer.name} hit {human.name}'s {human.ships[hit_char].name}!"
            computer.update_attack(x, y, hit_char)
            computer.update_defense(x, y, hit_char)
        else:
            message = f"{computer.name} missed!"
            computer.update_attack(x, y, "O")
            computer.update_defense(x, y, "O")
        # Show player's ship board after input
        computer.ship_board.display()
        print(message)
        computer.turns_taken += 1


if __name__ == "__main__":
    main()
