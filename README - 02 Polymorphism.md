# Battleships - Object-Oriented Programming: Encapsulation

The original instructions for the task can be found in [`original_instructions.md`](original_instructions.md).

**Object-Oriented Programming** (OOP) is a paradigm that operates on three principles for organising data and operations: **encapsulation**, **polymorphism**, and **inheritance**. These principles make it easier to reason about the code and its logic.

In addition to functions and modularisation, object-oriented programming provides one more tool in your abstraction toolbox.


# Polymorphism

In the previous lesson, you learned to **bundle data and methods acting on the data** into an object using a class, and **prevent inadvertent modification to data** by using public getter/setter methods to protect access to private data.

In the process, we created `Ship`, `Grid`, `Player` classes and their accompanying methods, and refactored the game code to use these classes and their instances.

But if we inspect more closely, we actually have two kinds of Grids: attack boards, and ship boards. And we have two kinds of Players: the human player and the computer player. Yet we only have one kind of Ship.

Although the game mentions three types of `Ship`s with different data (`name`, `symbol`, and `length`), they all behave identically: when they are `hit()`, their hit count increases by one, and when the hit count matches or exceeds the `length`, they are sunk. So all three ship types can be represented with one class.

On the other hand, the attack grid and the ship grid are not the same: the attack grid and ship grid have different purposes.

Attack grid:
- tracks player guesses, marking misses and any ships hit

Ship grid:
- shows player's ship layout
- marks enemy hits and misses

While both grids have `get()`, `set()`, and `display()` methods, only the ship grid needs `initialize()` and `place_ship()` methods.

Likewise, the human and computer player classes behave differently:

Human player:
- inputs the coordinate to attack using `input()`

Computer player:
- generates the coordinates to attack using an algorithm

How are we able to specify these differences in code, while still making the classes compatible with game code?

## Sharing a common interface

We first need to specify the **common interface** shared by the classes. For the `HumanPlayer` and `ComputerPlayer` classes, the following methods are shared in common:

- `__init__()`
- `has_lost()`
- `is_input_valid()`
- `update_attack()`
- `update_defense()`

For the `AttackGrid` and `ShipGrid` classes, the following methods are shared in common:

- `__init__()`
- `display()`
- `get()`
- `set()`
- `is_valid_coordinate()`


## Exercise 1

1. Duplicate the `Grid` class into `AttackGrid` and `ShipGrid` classes.

2. Update the `Player.update_attack()` and `Player.update_defense()` method annotations to require the specific grid classes.

3. Duplicate the `Player` class into `HumanPlayer` and `ComputerPlayer` classes.

4. Refactor the game to create instances of the appropriate class where necessary. Ensure the game still runs.


## Creating methods of the same name with different behaviour

The game loop currently duplicates the code for each player:

```python
while (
        not player.has_player_lost(human, max_turns)
        and not player.has_player_lost(computer, max_turns)
):
    # Player's turn
    print(f"{human.name}'s turn:")
    # Show player's board before input
    human.attack_board.display()
    row, col = player.get_player_input(grid_size)
    # Process human's attack on computer's grid
    hit_char = computer.ship_board.get(row, col)
    if hit_char in computer.ships:
        message = f"Hit! {human.name} hit {computer.name}'s {computer.ships[hit_char].name}!"
        human.update_attack(row, col, hit_char)
        computer.update_defense(row, col, hit_char)
    else:
        message = f"{human.name} missed!"
        human.update_attack(row, col, "O")
        computer.update_defense(row, col, "O")
    print(message)
    human.take_turn()

    # Computer's turn
    print(f"{computer.name}'s turn:")
    row, col = utility.generate_random_coordinate(len(computer.ship_board))
    # Process computer's attack on human's grid
    hit_char = human.ship_board.get(row, col)
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
    computer.take_turn()
```

The code for each is near-identical. The only difference here is what we mentioned: the player is prompted for input, while the computer generates its own input.

We could collapse both cases into one set of code with the following change:

```python
# Human goes first
attacker = human
defender = computer
while (
        not attacker.has_lost(max_turns)
        and not defender.has_lost(computer, max_turns)
):
    print(f"{attacker.name}'s turn:")
    # Show player's board before human input
    if isinstance(attacker, player.HumanPlayer):
        attacker.attack_board.display()
    row, col = attacker.get_input(grid_size)
    # Process attack
    hit_char = defender.ship_board.get(row, col)
    if hit_char in computer.ships:
        message = f"Hit! {attacker.name} hit {defender.name}'s {defender.ships[hit_char].name}!"
        attacker.update_attack(row, col, hit_char)
        defender.update_defense(row, col, hit_char)
    else:
        message = f"{attacker.name} missed!"
        attacker.update_attack(row, col, "O")
        defender.update_defense(row, col, "O")
    # Show player's board after computer input
    if isinstance(attacker, player.HumanPlayer):
        attacker.ship_board.display()
    print(message)
    attacker.take_turn()
    # Swap attacker and defender
    attacker, defender = defender, attacker
```

The critical change is:

```python
row, col = attacker.get_input(grid_size)
```

Since the `attacker` swaps between `HumanPlayer` and `ComputerPlayer` on each successive turn, both classes must implement a `get_input()` method that takes in an `int` and returns a 2-integer `tuple`.


## Exercise 2

Implement the following methods:

- `HumanPlayer.get_input(size: int) -> tuple[int, int]`
- `ComputerPlayer.get_input(size: int) -> tuple[int, int]`


Both `HumanPlayer` and `ComputerPlayer` implement a `get_input()` method with the same name but with different behaviour. We say that the `HumanPlayer` and `ComputerPlayer` classes are **polymorphic**.

Question: Are the `AttackGrid` and `ShipGrid` classes polymorphic? Why or why not?
