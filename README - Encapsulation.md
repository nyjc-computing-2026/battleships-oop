# Battleships - Object-Oriented Programming: Encapsulation

The original instructions for the task can be found in [`original_instructions.md`](original_instructions.md).

**Object-Oriented Programming** (OOP) is a paradigm that operates on three principles for organising data and operations: **encapsulation**, **polymorphism**, and **inheritance**. These principles make it easier to reason about the code and its logic.

In addition to functions and modularisation, object-oriented programming provides one more tool in your abstraction toolbox.

# Encapsulation

 Encapsulation refers to the bundling of data and methods that act on the data into an object.

 For example, in `ship.py`, each ship contains 4 pieces of information:

 - `name`, the ship's name
 - `symbol`, the letter used to represent the ship on the board
 - `length`, the number of grid squares that the ship takes up on the board
 - `hits`, the number of times the ship has been hit

 Right now we are using a `dict` to bundle them, but using `dict` all the time has distinct downsides:
 - besides ships we also have other things represented as `dict`, such as the player. We might accidentally mix up while trying to pass them to the correct function.
 - `dict` keys are strings, and we might accidentally typo the strings or even pass the wrong string.

 ## Classes and objects

 To define a ship, we use the `class` keyword in Python:

 ```python
 class Ship:
    """Represents a ship in Battleships.

    Each ship records information about the ship type, representation,
    and number of hits.
    """
```

Now we can create a ship with:

```python
ship1 = Ship()
ship1.name = "Battleship"
ship1.symbol = "B"
ship1.length = 4
ship1.hits = 0
ship2 = Ship()
...
```

`ship1` and `ship2` are different instances of `Ship` (i.e. `ship1 is ship2` evaluates to `False`), even if they have the same data.

This isn't very useful though; we would have to repeat 4 lines of code for each ship. These 4 lines are used to **initialise** each ship object, and are required for every ship instance.

## Constructor method

In Python, we would thus put these 4 lines of code in a special method called `__init__()`:

```python
 class Ship:
    """Represents a ship in Battleships.

    Each ship records information about the ship type, representation,
    and number of hits.
    """

    def __init__(self, name: str, symbol: str, length: int):
        self.name = name
        self.symbol = symbol
        self.length = length
        self.hits = 0
```

In the above code, `ship1` has been replaced by a special variable, `self`. `self` refers to the instance that the method is being called from. Now, the code for creating a ship looks like:

```python
ship1 = Ship(name="Battleship", symbol="B", length="4")
```

`__init__()` is called the **constructor method** of `Ship`. The arguments passed to the constructor follow the constructor method interface.

## Working with objects

To make the `hit()` and `is_sunk()` functions work with this `Ship` class, we would modify them as follows:

```python
def hit(ship: Ship) -> None:
    """Register a hit on the ship by incrementing its hit counter.

    Arguments:
        ship: Ship -- the ship to register the hit on

    Returns:
        None
    """
    ship.hits += 1


def is_sunk(ship: Ship) -> bool:
    """Check if the ship is sunk by comparing its hit counter to its length.

    Arguments:
        ship: Ship -- the ship to check

    Returns:
        True if the ship is sunk, False otherwise.
    """
    return ship.hits >= ship.length
```

Instead of accessing keys on a `dict`, we are now accessing **attributes** on an object.

Notice the different terms we use:
- **attribute**: a variable bound to an object
- **method**: a function bound to an object

Notice also that `Ship` and `ship1` refer to different things. `Ship` refers to the blueprint used to create `ship1` and other ship objects. `Ship` is called the **class** and `ship1` the **instance**.

## Exercise: refactoring

Refactor the functions in `player.py` and `grid.py` to use the `Ship` class attributes instead of `dict` keys.

## Instance methods

Since `hit()` and `is_sunk()` only work on `Ship` objects, it is unlikely we will ever use them with any other objects. We might as well bundle them into the `Ship` class as methods:

```python
 class Ship:
    """Represents a ship in Battleships.

    Each ship records information about the ship type, representation,
    and number of hits.
    """

    def __init__(self, name: str, symbol: str, length: int):
        self.name = name
        self.symbol = symbol
        self.length = length
        self.hits = 0

    def hit(self) -> None:
        """Register a hit on the ship.

        Arguments:
            None

        Returns:
            None
        """
        self.hits += 1

    def is_sunk(self) -> bool:
        """Check if the ship is sunk by comparing its hit counter to its length.

        Arguments:
            ship: dict -- the ship to check

        Returns:
            True if the ship is sunk, False otherwise.
        """
        return ship.hits >= ship.length
```

And we call the methods with the method call syntax:

```python
ship1.hit()  # replace ship1 with the actual variable
if ship1.is_sunk():
    print(f"{ship1.name} is sunk!")
```

**Important:** Notice that in the method interface, `self` is always the first parameter. However, when calling the method, we do not need to pass it as an argument: Python will "inject" the instance for us.

### Exercise: refactoring

1. Refactor the player dict in `player.py` as a `Player` class.
2. Refactor the grid dict in `grid.py` as a `Grid` class.
3. Refactor game functions to work with `Player` and `Grid` objects instead of `dict`s.
