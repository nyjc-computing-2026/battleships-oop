# Battleships - Abstraction and Modularization

The original instructions for the task can be found in [`original_instructions.md`](original_instructions.md)

# Abstraction: Schemas and Interfaces

The first thing you may have realised is that for a team to work together, you'll need to agree on:

- data formats: how ships, players, hits and misses will be represented in the game data
- interfaces: what functions should do, what type(s) they should take in, what they should return

You've had some training in this in the assignments, but now you need to apply it as a group.

### Individual task

Determine how you will represent:
- game boards (empty space, ships, hits and misses)
- players (boards, ships, other player data)
- game: turns taken by each player, maximum number of turns, et


# Abstraction: Chunking functions

With that done, it's tempting to jump right in and begin coding. Without a plan, it's easy to get lost in the weeds and forget what you were initially trying to do.

For a game, we usually start with the game loop:
- what are the individual tasks that need to be done for each part of the game?
- how do we "package" this requirement into a function?

A technique that can help at this stage is "_hallucination_": _pretend_ the function you need exists. What would it be called? What would it take in, and what would it do and/or return? Instead of writing the main loop with the details of everything you were trying to do, Write your code as though those functions exist, and use them to *describe* what you are trying to do instead of doing it.

This naturally chunks the project into individual tasks that you can work on as a group.

### Individual task

#### Write the game loop.  

**Do not:**
- mutate data directly (no string concatenation or list mutation)
- access data directly from a list or string (no string/list slicing, indexing etc)

This practice forces you to step away from the concrete details, and look at the purpose/intention: what effect are you trying to achieve?

#### Write function docstrings and annotations for the hallucinated functions

Next, look at the functions you hallucinated. Write the docstrings and annotations.

This practice forces you to think through the data schemas you came up with earlier, and edit them so that they serve the project. It also forces you to think about function scope: is a particular function doing too much?

# Abstraction: Modularization

Analyze the interface of the functions you wrote earlier.

1. Do any of them rely on a particular data structure? If they take in board data, or player data, those functions will rely on the implementation details.
2. Are any of them helper functions? E.g. functions for generating random coordinates, formatting text.

### Individual task

Determine how the functions can be bundled into modules in a way that makes the code more readable. This reduces the number of function definitions in `main.py`, and makes it easier to collaborate: you can have individual team members work on a module without affecting the main program.

# Putting it all together: game testing

How would you test that each of these modules/functions is doing the correct thing?

Initially you might do some manual testing, running the game and entering inputs manually to visually inspect of the result is correct. But this gets tiring quickly. Think about how you could automate this part: instead of relying on manual input, is there a way to write the actions you take as code instead, so you can run it as a test?

As you go, you might find that some functions still involve a lot of implementation. you can and should "hallucinate" more functions as necessary to further chunk the code into parts.
