"""This module defines the `Mob` and `Mob_AI` classes, which represent mobs in a game and their behavior within a grid-based world. The `Mob` class encapsulates attributes such as difficulty, type, ID, boss status, and evolution capability. The `Mob_AI` class simulates mob behavior, including movement, interactions, and reproduction based on specific rules. Mobs can move randomly, reproduce under certain conditions, and interact with other mobs, with the world state being updated accordingly."""
from typing import Any
import random
# This Python class represents a mob in a game with attributes such as difficulty, type, ID, boss
# status, and evolution capability.


class Mob:
    """The `Mob` class represents a mob in a game, characterized by its difficulty level, type, unique identifier, boss status, and evolution capability. Each mob instance can be initialized with specific attributes that define its behavior and role within the game world."""

    def __init__(self, difficulty: str, mob_type: str, mob_id: str, boss: bool, evolve: bool):
        """
        This Python function initializes attributes related to a game mob with specified
        characteristics.

        :param difficulty: The `difficulty` parameter in the `__init__` method is a string that
        represents the difficulty level of a game. It could be values like "easy", "medium", or "hard"
        depending on the game's settings
        :type difficulty: str
        :param mob_type: The `mob_type` parameter in the `__init__` method represents the type of mobile
        entity or creature. It could be a category or classification that helps differentiate different
        types of mobs within the game or application. Examples of `mob_type` could include "zombie",
        "skeleton", "
        :type mob_type: str
        :param mob_id: The `mob_id` parameter in the `__init__` method is used to store the unique
        identifier of a mobile entity (mob) in a game. This identifier helps differentiate one mob from
        another and can be used for various purposes such as tracking, referencing, or identifying
        specific mobs within the game
        :type mob_id: str
        :param boss: The `boss` parameter in the `__init__` method is a boolean value that indicates
        whether the mob is a boss or not. If `boss` is `True`, it means the mob is a boss; if `boss` is
        `False`, it means the mob is not a boss
        :type boss: bool
        :param evolve: The `evolve` parameter in the `__init__` method is a boolean flag that indicates
        whether the mob has the ability to evolve or not. If `evolve` is `True`, it means the mob can
        evolve, and if it's `False`, the mob does not have the
        :type evolve: bool
        """
        self.difficulty = difficulty
        self.mob_type = mob_type
        self.mob_id = mob_id
        self.boss = boss
        self.evolve = evolve
# The `Mob_AI` class in Python simulates mob behavior in a world grid, including movement,
# interactions, and reproduction based on specific rules.


class Mob_AI:
    """The `Mob_AI` class simulates mob behavior in a grid-based world, allowing for movement,
interactions, and reproduction based on defined rules. Mobs can move randomly, reproduce under certain conditions, and interact with other mobs, with the world state being updated accordingly."""

    def __init__(self, world: Any):
        """
        The function initializes attributes related to the size and movement speed of a world object.

        :param world: The `world` parameter in the `__init__` method is expected to be an object of type
        `Any`. This object represents the world in which some kind of simulation or game is taking
        place. The code snippet initializes various attributes of the class instance based on the
        properties of the world object provided
        :type world: Any
        """
        self.world: Any = world
        self.row, self.col = world.size
        self.max_x = self.col - 1
        self.max_y = self.row - 1
        # ! 1 for real movement 60 for faster paced movement (will be kinda strange to watch but good for testing)
        self.seconds = 1

    def brownian_motion(self, mob_list: list[Any], count: int) -> None:
        """
        The `brownian_motion` function simulates movement and interactions of mobs in a world grid,
        including reproduction and collision logic.
        
        :param mob_list: The `mob_list` parameter in the `brownian_motion` function is a list of
        dictionaries representing mobs in the simulation. Each dictionary contains information about a
        mob, such as its type ("Weak" or "Strong") and its current position on the map
        :type mob_list: list[Any]
        :param count: The `count` parameter is an integer that represents the number of iterations or
        steps to simulate in the Brownian motion function. Each iteration involves moving the mobs in
        the `mob_list` according to the rules defined in the function. The function simulates the
        movement and interactions of different types of mobs (
        :type count: int
        """
        mon_types = {"Weak": "ᵟ", "Strong": "Ω"}

        new_mobs: list[dict[str, Any]] = []

        for mob in list(mob_list):
            mob.setdefault("energy", 50)
            mob.setdefault("age", 0)
            for _ in range(self.seconds):  # simulate multiple steps
                # stored positions are (x, y)
                x, y = mob["pos"]
                ox, oy = x, y  # old position

                dx, dy = random.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
                nx = max(0, min(self.max_x, x + dx))
                ny = max(0, min(self.max_y, y + dy))

                mob["age"] += 1
                mob["energy"] -= 1+int(random.random()*5)  # lose energy on movement
                
                # ? check if new pos is a corpse
                if "*" in self.world.chunk[ny][nx]:
                    mob["energy"] += 2  # gain energy from corpse
                    continue

                target_cell = self.world.chunk[ny][nx]
                if " " in target_cell or "░" in target_cell:
                    old_terrain = "░"
                    # restore old terrain
                    self.world.chunk[oy][ox] = old_terrain
                    # move mob
                    self.world.chunk[ny][nx] = mon_types[mob["type"]]
                    mob["pos"] = (nx, ny)
                elif "ᵟ" in target_cell:
                    # Reproduction logic: 5% chance to reproduce into an adjacent cell
                    if random.random() > 0.95 and not self.check_area(nx, ny, char="ᵟ", num=3):
                        dx = random.randint(-1, 1)
                        dy = random.randint(-1, 1)
                        rx = max(0, min(self.max_x, nx + dx))
                        ry = max(0, min(self.max_y, ny + dy))
                        # only place if target cell looks empty
                        if (" " == self.world.chunk[ry][rx]) or ("░" in self.world.chunk[ry][rx]):
                            self.world.chunk[ry][rx] = "ᵟ"
                            new_mobs.append({"type": "Weak", "pos": (rx, ry), "energy": mob["energy"]+random.randint(-10,10), "age": 0})
                            mob["energy"] = mob.get("energy", 50) - 50  # reduce energy on reproduction
                elif "Ω" in target_cell:  # mob collision
                    # For simplicity, just restore old position (no combat logic)
                    if random.random() < 0.25:  # 25% chance to "win" and move into the cell
                        self.world.chunk[oy][ox] = "*"  # Clear old position
                    # If there's a corpse nearby, the winner may create an offspring.
                    if self.check_area(nx, ny, char="*"):
                        # try to place a child in a nearby empty cell
                        if random.random() > 0.95 and not self.check_area(nx, ny, char="Ω", num=5):#! remove mobs if energy < 0
                            ddx = random.randint(-1, 1)
                            ddy = random.randint(-1, 1)
                            rx = max(0, min(self.max_x, nx + ddx))
                            ry = max(0, min(self.max_y, ny + ddy))
                            # only place if target cell looks empty
                            if (self.world.chunk[ry][rx] == " ") or ("░" in self.world.chunk[ry][rx]):
                                self.world.chunk[ry][rx] = "Ω"
                                new_mobs.append(
                                    {"type": "Strong", "pos": (rx, ry)})
                        else:
                            # ensure the winning mob remains visible on map
                            self.world.chunk[ny][nx] = "Ω"
                    mob["pos"] = (ox, oy)
                else:
                    # If target cell is something else (like a wall), also restore old position
                    mob["pos"] = (ox, oy)

        # Add newborns after processing to avoid mutating while iterating
        if new_mobs:
            mob_list.extend(new_mobs)

    def check_area(self, x: int, y: int, char: str, num: int = 0, area: tuple[int, int] = (3, 3), enemy: str = "Ω") -> bool:
        """
        The function `check_area` checks the number of occurrences of a character within a specified
        area around a given position in a game world grid, excluding occurrences of a specified enemy
        character.
        
        :param x: The `x` parameter represents the x-coordinate of the center point in the area you want
        to check
        :type x: int
        :param y: The 'y' parameter in the function represents the vertical position within the game
        world grid where you want to check for a specific character and its surroundings
        :type y: int
        :param char: The `char` parameter in the `check_area` method is a string representing a
        character that you are checking for in the specified area. The method iterates over a square
        area centered around the coordinates `(x, y)` and counts the occurrences of the `char` character
        within that area
        :type char: str
        :param num: The `num` parameter in the `check_area` method is an optional integer parameter that
        specifies the minimum number of occurrences of the `char` within the specified area for the
        method to return `True`. If the count of occurrences of `char` within the area is greater than
        `num`, the, defaults to 0
        :type num: int (optional)
        :param area: The `area` parameter in the `check_area` method represents the size of the area
        around a given position `(x, y)` that will be checked for certain conditions. It is a tuple of
        two integers `(width, height)` representing the dimensions of the rectangular area to be
        examined. The default
        :type area: tuple[int, int]
        :param enemy: The `enemy` parameter in the `check_area` method is a string that represents the
        character of an enemy entity in the game world. The method iterates over a specified area around
        a given position `(x, y)` and counts the occurrences of a specified character `char` while
        ensuring that the, defaults to Ω
        :type enemy: str (optional)
        :return: a boolean value indicating whether the count of occurrences of the character `char` in
        the specified area around the coordinates `(x, y)` is greater than the specified number `num`.
        """
        count = 0
        for dy in range(-area[1]//2, area[1]//2 + 1):
            for dx in range(-area[0]//2, area[0]//2 + 1):
                nx = max(0, min(self.max_x, x + dx))
                ny = max(0, min(self.max_y, y + dy))
                if char in self.world.chunk[ny][nx] and enemy not in self.world.chunk[ny][nx]:
                    count += 1

        return count > num
    def dead_mobs(self,arr):
        """
        The `dead_mobs` function marks mobs with zero energy as corpses in the game world and removes them
        from the list of active mobs.
        
        :param arr: The `arr` parameter is a list of dictionaries representing mobs in a game. Each
        dictionary in the list contains information about a mob, such as its energy level (`"energy"`) and
        position (`"pos"`). The `dead_mobs` method iterates over this list, checks if a
        """
        for mob in arr.copy():  # Use a copy to avoid modifying list during iteration
            if mob["energy"] <= 0:
                x, y = mob["pos"]
                self.world.chunk[y][x] = "*"  # Mark as corpse
                arr.remove(mob)  # Remove from active mobs


if __name__ == "__main__":
    print("Run idle_game.py to see the mob AI in action! dumahh")