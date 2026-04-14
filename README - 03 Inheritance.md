# Battleships - Object-Oriented Programming: Inheritance

The original instructions for the task can be found in [`original_instructions.md`](original_instructions.md).

**Object-Oriented Programming** (OOP) is a paradigm that operates on three principles for organising data and operations: **encapsulation**, **polymorphism**, and **inheritance**. These principles make it easier to reason about the code and its logic.

In addition to functions and modularisation, object-oriented programming provides one more tool in your abstraction toolbox.


# Inheritance

In the previous lesson, you learned to create polymorphic classes, which are classes that implement one or more methods with **the same name but different behaviour**. Polymorphic classes promote code generalisation, allowing code to be written without having to check for specific instances.

But in the process, we duplicated a lot of code across the `HumanPlayer` and `ComputerPlayer` classes, and across the `AttackGrid` and `ShipGrid` classes. This is not only tedious, it can also be dangerous: when we have code duplicated across multiple classes, it's easy to update code or fix a bug in one place while forgetting to update all the duplicate copies exactly. For this reason, programmers try to follow the DRY principle: "**D**on't **R**epeat **Y**ourself".

We can use inheritance to **promote code reuse**. Inheritance allows a **child class** (also called **subclass**) to access public methods from a **parent clas** (also called **superclass**).

In Python, we indicate inheritance as follows:

```python
class AttackGrid(Grid):
    
```

This means that the subclass `AttackGrid` inherits from the superclass `Grid`. Any public methods defined in `Grid` may be called from `AttackGrid` as well.

We can use this feature to move all duplicate code from `AttackGrid` and `ShipGrid` into `Grid`:

```python
class Grid:
    """Represents a 2D square grid in Battleships.

    Each grid stores data as a single-character string, accessed using
    (x, y) coordinates, with x representing the horizontal coordinate
    and y representing the vertical coordinate.
    """

    def __init__(self, size: int, placeholder: str):
        self.size = size
        self._data = []
        for _ in range(n):
            row = [placeholder] * n
            self._data.append(row)

    def display(self) -> None:
        """Display the grid in a readable format."""
        for row in self._data:
            print(" ".join(row))

    def is_valid_coordinate(x: int, y: int) -> bool:
        """Check if the given coordinates are valid for the grid.

        Arguments:
            grid: list[list[str]]
            x: int
                the row index to validate
            y: int
                the column index to validate

        Returns:
            True if the coordinates are valid, False otherwise.
        """
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid):
            return False
        return True

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

Methods defined on the child classes are not accessible from other child classes:

```python
class AttackGrid(Grid):
    """Represents the 2D grid used for a player to mark attacks."""


class ShipGrid(Grid):
    """Represents the 2D grid used for a player to mark ship locations."""

    def initialize(self, ships: list[Ship]) -> None:
        """Initialize the grid by placing ships randomly on the grid.

        Arguments:
            ships: list[Ship]
                a list of ships to place on the grid
        
        Returns:
            None
        """
        for ship in ships:
            x, y = utility.generate_random_coordinate(self.size)
            orientation = utility.generate_random_orientation()
            # Keep trying to place the ship until it is successfully placed
            # on the grid
            while not self.place_ship(ship, x, y, orientation):
                x, y = utility.generate_random_coordinate(self.size)
                orientation = utility.generate_random_orientation()

    def place_ship_on_grid(
            self,
            ship: Ship,
            x: int,
            y: int,
            orientation: str
    ) -> bool:
        """Place a ship on the grid at the specified coordinates.

        Arguments:
            ship: dict -- the ship to place on the grid
            x: int -- the row index for the starting coordinate
            y: int -- the column index for the starting coordinate
            orientation: str -- the orientation of the ship ('horizontal' or
                'vertical')
        
        Returns:
            True if the ship was successfully placed, False if placement
            failed due to out-of-bounds or overlap with existing ships.
        """
        if orientation == 'horizontal':
            return self._place_ship_horizontally(ship, x, y)
        elif orientation == 'vertical':
            return self._place_ship_vertically(ship, x, y)
        else:
            raise ValueError(
                "Invalid orientation. Must be 'horizontal' or 'vertical'."
            )

    def _place_ship_horizontally(
            self,
            ship: Ship,
            x: int,
            y: int,
    ) -> bool:
        """Place a ship on the grid at the specified coordinates
        horizontally (rightwards).

        Arguments:
            ship: dict -- the ship to place on the grid
            x: int -- the row index for the starting coordinate
            y: int -- the column index for the starting coordinate
        
        Returns:
            True if the ship was successfully placed, False if placement
            failed due to out-of-bounds or overlap with existing ships.
        """
        for i in range(ship['length']):
            if not is_valid_coordinate(grid, x, y + i) or grid[x][y + i] != '~':
                return False
        for i in range(ship['length']):
            grid[x][y + i] = ship['symbol']
        return True

    def _place_ship_vertically(
            self,
            ship: Ship,
            x: int,
            y: int,
    ) -> bool:
        """Place a ship on the grid at the specified coordinates
        vertically (downwards).

        Arguments:
            ship: dict -- the ship to place on the grid
            x: int -- the row index for the starting coordinate
            y: int -- the column index for the starting coordinate
        
        Returns:
            True if the ship was successfully placed, False if placement
            failed due to out-of-bounds or overlap with existing ships.
        """
        # Validate ship coordinates are empty first
        for i in range(ship.length):
            if (
                    not self.is_valid_coordinate(x + i, y)
                    or self.get(x + i, y) != '~'
            ):
                return False
        # Place ship
        for i in range(ship.length):
            self.set(x + i, y) = ship.symbol
        return True
```

Here, the methods defined on `ShipGrid` are not accessible from `AttackGrid`.
