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

We use different terms for data bundled in an object:
- **attribute**: a variable bound to an object
- **method**: a function bound to an object

Notice also that `Ship` and `ship1` refer to different things. `Ship` refers to the blueprint used to create `ship1` and other ship objects. `Ship` is called the **class** of the `ship1` **instance**.


## The constructor method

In Python, we would thus put these 4 lines of code in a special **method** called `__init__()`:

```python
 class Ship:
    """Represents a ship in Battleships.

    Each ship records information about the ship type, representation,
    and number of hits.
    """

    # A function defined in a class is a method
    def __init__(self, name: str, symbol: str, length: int):
        self.name = name
        self.symbol = symbol
        self.length = length
        self.hits = 0
```

In the above code, `ship1` has been replaced by a special variable, `self`. `self` refers to the instance that the method is being called from. Now, the code for creating a ship looks like:

```python
# Create a ship using named (keyword) arguments
# PEP8: Note that keyword arguments do not need space around `=` operator
ship1 = Ship(name="Battleship", symbol="B", length="4")
```

**Important:** Notice that in the method interface, `self` is always the first parameter. However, when calling the method, we do not need to pass it as an argument: Python will "inject" the instance for us.

`__init__()` is called the **constructor method** of `Ship`. The arguments passed to the constructor follow the constructor method interface.

### Addendum

We can also use:

```python
# Create a ship using positional arguments
ship1 = Ship("Battleship", "B", "4")
```

This is faster to write at the moment, but risks lower readability in future: a reader will have to check the `Ship.__init__()` interface to understand what the arguments refer to.


## Exercise 1

Refactor the following functions in `grid.py` to use the `Ship` class attributes instead of `dict` keys:

- `grid.place_ship_on_grid_horizontally()`
- `grid.place_ship_on_grid_vertically()`
- `ship.hit()`
- `ship.is_sunk()`


## Instance methods

Since `ship.hit()` and `ship.is_sunk()` only work on `Ship` objects, it is unlikely we will ever use them with any other objects. We might as well bundle them into the `Ship` class as methods:

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

### Exercise 2

Refactor the following functions to use `Ship` methods instead of `ship` module functions:

- `player.has_player_lost()`
- `player.update_defense()`


### Exercise 3

1. Create a `Player` class in `player.py`.
2. Refactor the following functions in `player.py` to use `Player` instances instead of `dict`s:
   - `player.create_player()`
   - `player.update_attack()`
   - `player.update_defense()`
   - `player.has_player_lost()`


## Preventing inadvertent modification through private data

So far in Battleships, we have been representing grids as a nested list of string symbols (`list[list[str]]`). Grids are directly accessed and updated in `grid.py` and `player.py`. This opens up grid data to **inadvertent modification**: any code anywhere in the program might write the wrong data to the grid, resulting in inconsistent data.

This need not be malicious; programmers can make mistakes and typos too. Is there a way we can control changes to grid data so that *only approved, validated edits can happen*?

### Public and private data

We do so by making data **private**, and require the use of **public** methods to access or modify data. Methods used to access data (without modifying it) are called **getter** methods, while methods used to update data are usually called **setter** methods.

In other programming languages, such as Java, private data cannot be accessed from outside the class's methods. However, in Python, there is no way to make an object's attribute *truly private*: all object attributes are accessible. Instead, we use a programming convention: private data in Python is marked with an underscore (`_`) prefix.

So we might design the `Grid` class like this:

```python
class Grid:
    """Represents a 2D square grid in Battleships.

    Each grid stores data as a single-character string, accessed using
    (x, y) coordinates, with x representing the horizontal coordinate
    and y representing the vertical coordinate.
    """

    def __init__(self, size: int):
        self._data = []
        for _ in range(n):
            row = [placeholder] * n
            self._data.append(row)

    def get(self, x: int, y: int) -> str:
        """Getter method for grid data.

        Arguments:
            x: int
                The horizontal coordinate
            y: int
                The vertical coordinate

        Returns:
            The character (str) at coordinate (x, y)
        """
        return self._data[y][x]

    def set(self, x: int, y: int, symbol: str) -> None:
        """Setter method for grid data.

        Arguments:
            x: int
                The horizontal coordinate
            y: int
                The vertical coordinate
            symbol:
                The symbol to store at coordinate (x, y)

        Returns:
            None
        """
        if len(symbol) != 1:
            raise ValueError(
                f"{repr(symbol)}: symbol must be single character only"
            )
        self._data[y][x] = symbol
```

The `_data` attribute has an underscore prefix, indicating to other programmers that this is private data and should not be accessed directly. Instead, the `get()` and `set()` methods should be used to retrieve data at coordinates or store data at coordinates.

Notice that the use of setter methods enables validation to be enforced. This is how the use of methods to update data can **prevent inadvertent modification**.


### Exercise 4

1. Refactor the following functions in `grid.py` to use `Grid` instances and `get()`/`set()` methods instead of `dict`s:
   - `grid.create_grid()`
   - `grid.display_grid()`
   - `grid.get_grid_coordinate_char()`
   - `grid.initialize_grid()`
   - `grid.is_valid_coordinate()`
   - `grid.place_ship_on_grid_horizontally()`
   - `grid.place_ship_on_grid_vertically()`
2. Implement the following functions as methods in `grid.py`:
   - `grid.display_grid()`
   - `grid.is_valid_coordinate()`
3. Refactor the remaining code to use the methods implemented in `Grid` class.

4. Implement `Player.take_turn()` setter method to update the `turns_taken` attribute.
5. Refactor the main game loop to observe encapsulation principle by using the setter method.
