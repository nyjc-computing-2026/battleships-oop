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
    attacker = human
    defender = computer
    while (
            not human.has_player_lost(max_turns)
            and not computer.has_player_lost(max_turns)
    ):
        # Attacker's turn
        print(f"{attacker.name}'s turn:")
        # Show human's board before input
        if isinstance(attacker, player.Human):
            attacker.attack_board.display()
        x, y = attacker.get_input()
        # Process attacker's attack on defender's grid
        hit_char = defender.ship_board.get(x, y)
        if hit_char in defender.ships:
            message = f"Hit! {attacker.name} hit {defender.name}'s {defender.ships[hit_char].name}!"
            attacker.update_attack(x, y, hit_char)
            defender.update_defense(x, y, hit_char)
        else:
            message = f"{attacker.name} missed!"
            attacker.update_attack(x, y, "O")
            defender.update_defense(x, y, "O")
        # Show human's ship board after input
        if isinstance(attacker, player.Human):
            attacker.ship_board.display()
        print(message)
        attacker.take_turn()

        # Attacker and defender switch roles for the next turn
        attacker, defender = defender, attacker


if __name__ == "__main__":
    main()
