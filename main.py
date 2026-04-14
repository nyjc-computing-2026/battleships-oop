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
        attack_board=grid.Grid(size=grid_size, placeholder="~"),
        ships={
            "B": ship.create_ship(name="Battleship", symbol="B", length=4),
            "C": ship.create_ship(name="Cruiser", symbol="C", length=3),
            "D": ship.create_ship(name="Destroyer", symbol="D", length=2)
        }
    )
    human = player.Human(
        name="Player",
        ship_board=grid.ShipGrid(size=grid_size, placeholder="~"),
        attack_board=grid.Grid(size=grid_size, placeholder="~"),
        ships={
            "B": ship.create_ship(name="Battleship", symbol="B", length=4),
            "C": ship.create_ship(name="Cruiser", symbol="C", length=3),
            "D": ship.create_ship(name="Destroyer", symbol="D", length=2)
        }
    )

    # Game setup: populate ship boards and initialize attack boards
    computer.ship_board.initialize(
        ships=list(computer.ships.values()),
    )
    human.ship_board.initialize(
        ships=list(human.ships.values()),
    )

    # Game loop
    attacker = human
    defender = computer
    while (
            not human.has_player_lost(max_turns)
            and not computer.has_player_lost(max_turns)
    ):
        # Attacker's turn
        print(f"{attacker.name}'s turn:")
        # Show attacker's board before input
        attacker.attack_board.display()
        row, col = attacker.get_input()
        # Process attacker's attack on defender's grid
        hit_char = defender.ship_board.get(row, col)
        if hit_char in defender.ships:
            message = f"Hit! {attacker.name} hit {defender.name}'s {defender.ships[hit_char].name}!"
            attacker.update_attack(row, col, hit_char)
            defender.update_defense(row, col, hit_char)
        else:
            message = f"{attacker.name} missed!"
            attacker.update_attack(row, col, "O")
            defender.update_defense(row, col, "O")
        print(message)
        attacker.take_turn()

        # Swap attacker and defender for the next turn
        attacker, defender = defender, attacker


if __name__ == "__main__":
    main()
