"""This module defines the `Mob` and `Mob_AI` classes, which represent mobs in a game and their behavior within a grid-based world. The `Mob` class encapsulates attributes such as difficulty, type, ID, boss status, and evolution capability. The `Mob_AI` class simulates mob behavior, including movement, interactions, and reproduction based on specific rules. Mobs can move randomly, reproduce under certain conditions, and interact with other mobs, with the world state being updated accordingly."""
import math
from typing import Any
import random
from combat import Combat
# This Python class represents a mob in a game with attributes such as difficulty, type, ID, boss
# status, and evolution capability.
fight = Combat()

# todo craeate seperate calss for predators and prey that inherit from mob, with different behaviors and attributes, like predators being able to hunt prey and prey having different reproduction rates or energy requirements


class Mob:
    """The `Mob` class represents a mob in a game, characterized by its difficulty level, type, unique identifier, boss status, and evolution capability. Each mob instance can be initialized with specific attributes that define its behavior and role within the game world."""

    def __init__(self, difficulty: str, mob_type: str, mob_id: str, energy: int | float, coords: tuple[int, int], age: int, evolve: bool = False):
        self.difficulty = difficulty
        self.mob_type = mob_type
        self.old_type = mob_type
        self.mob_id = mob_id
        self.energy = energy
        self.age = age
        self.coords = coords
        self.evolve = evolve
        self.state = "Healthy"  # Example state, can be expanded to include more complex behaviors
        # Example stage, can be used to represent different stages of life or evolution
        self.stage = "Baby"

    def grow(self):
        """
        The `grow` function assigns a  based on the age of an entity, with specific symbols used for
        representation on a map.
        """
        if self.age > 1500:
            # ! Ψ for its representation on the map, should be changed to something else if we add more mob types to avoid confusion
            self.mob_type = "Ancient"
        elif self.age > 500:
            # ! λ for its representation on the map, should be changed to something else if we add more mob types to avoid confusion
            self.mob_type = "Elder"
        elif self.age > 250 and self.mob_type != "Strong":
            # ! Δ for its representation on the map, should be changed to something else if we add more mob types to avoid confusion
            self.mob_type = "Adult"


class Predator(Mob):
    """The `Predator` class represents a mob that is a predator in the game, inheriting from the `Mob` class. It can have additional attributes and behaviors specific to predators, such as hunting capabilities and energy requirements for survival."""

    def __init__(self, difficulty: str, mob_type: str, mob_id: str, energy: int | float, coords: tuple[int, int], age: int, evolve: bool = False):
        super().__init__(difficulty, mob_type, mob_id, energy, coords, age, evolve)
        # todo Additional attributes specific to predators can be added here


class Prey(Mob):
    """The `Prey` class represents a mob that is a prey in the game, inheriting from the `Mob` class. It can have additional attributes and behaviors specific to prey, such as reproduction rates and energy requirements for survival."""

    def __init__(self, difficulty: str, mob_type: str, mob_id: str, energy: int | float, coords: tuple[int, int], age: int, evolve: bool = False):
        super().__init__(difficulty, mob_type, mob_id, energy, coords, age, evolve)
        # todo Additional attributes specific to prey can be added here
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
        self.corpse_list = []  # list of (coords, decay_time) for corpses in the world
        self.corpse_decay_time = 500  # time it takes for a corpse to decay and be removed from the world
        
    def brownian_motion(self, mob_list: list[Mob]) -> None:
        """
        The `brownian_motion` function simulates movement and interactions of mobs in a world grid,
        including reproduction and collision logic.

        :param mob_list: The `mob_list` parameter in the `brownian_motion` function is a list of
        dictionaries representing mobs in the simulation. Each dictionary contains information about a
        mob, such as its type ("Weak" or "Strong") and its current position on the map
        :type mob_list: list[Mob]
        :param count: The `count` parameter is an integer that represents the number of iterations or
        steps to simulate in the Brownian motion function. Each iteration involves moving the mobs in
        the `mob_list` according to the rules defined in the function. The function simulates the
        movement and interactions of different types of mobs (
        :type count: int
        """
            
        nuke = Mob("easy","Nuke", 8008135, 10e9, (self.max_x//2, self.max_y//2),0)
        mon_types = {"Weak": "ᵟ", "Adult": "Δ",
                     "Elder": "λ", "Ancient": "Ψ", "Strong": "Ω"}
        #! the oreder of apex predatoors are
        # ? weak prey (ᵟ) -> strong prey (Δ) -> weak predator (Ω) -> strong predator (λ) -> apex predator (Ψ)

        new_mobs: list[Mob] = []

        for mob in list(mob_list):
            for _ in range(self.seconds):  # simulate multiple steps
                # stored positions are (x, y)
                x, y = mob.coords
                ox, oy = x, y  # old position

                dx, dy = random.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
                nx = max(0, min(self.max_x, x + dx))
                ny = max(0, min(self.max_y, y + dy))

                mob.age += 1
                mob.grow()
                # lose energy on movement
                # randomize energy loss a bit to create more variation in mob lifespans
                #! the energy loss formula is based on a combination of a base movement cost (1), a random factor (0-2), and a logarithmic function of the mob's age and energy to create a more dynamic and realistic energy depletion over time.
                stress = 100 if random.random() > 0.99 else 0 
                safe_energy = max(1, mob.energy)
                mob.energy -= stress +((random.random()**2)*2 + math.log10(mob.age+1.1) +math.log(safe_energy+1.1)**0.75)
                # ? check if new pos is a corpse
                if "*" in self.world.chunk[ny][nx]:
                    sign = 1 if random.random() > 0.5 else -1
                    mob.energy += 150 +(random.random()*50*sign) # gain energy from corpse
                    self.world.chunk[ny][nx] = " "  # consume corpse
                    self.corpse_list = [c for c in self.corpse_list if c[0] != (nx, ny)]  # remove corpse from list
                    continue
                if self.check_area(nx, ny, char="*", area=(3, 3), num=5):
                    # lose energy from nearby corpses (disease, bad smell, etc)
                    mob.energy -= 150
                    continue
                target_cell = self.world.chunk[ny][nx]
                if " " in target_cell or "░" in target_cell:
                    old_terrain = "░"
                    # restore old terrain
                    self.world.chunk[oy][ox] = old_terrain
                    # move mob
                    self.world.chunk[ny][nx] = mon_types[mob.mob_type]
                    mob.coords = (nx, ny)
                elif "ᵟ" in target_cell and mob.mob_type not in ["Strong", "Adult", "Elder", "Ancient"]:
                    # Reproduction logic: 5% chance to reproduce into an adjacent cell
                    if mob.energy > 500 and not self.check_area(nx, ny, char="ᵟ", num=3):
                        rdx = random.randint(-1, 1)
                        rdy = random.randint(-1, 1)
                        rx = max(0, min(self.max_x, nx + rdx))
                        ry = max(0, min(self.max_y, ny + rdy))
                        # only place if target cell looks empty
                        if (" " == self.world.chunk[ry][rx]) or ("░" in self.world.chunk[ry][rx]):
                            self.world.chunk[ry][rx] = "ᵟ"
                            new_mobs.append(Mob(
                                self.world.diff, "Weak", f"mob_{len(mob_list)+len(new_mobs)}", mob.energy*random.gauss(1, 0.1), (rx, ry), 0))
                            # reduce energy on reproduction
                            mob.energy -= 350
                elif "ᵟ" in target_cell and mob.mob_type in ["Strong", "Elder", "Ancient"]:
                    target = next(
                        (m for m in mob_list if m.coords == (nx, ny)), None)
                    if target:
                        fight.fight(
                            mob, target)
                    if mob.mob_type in ["Strong", "Elder", "Ancient"] and random.random() > 0.95:
                        fight.aoe_damage(mob, [m for m in mob_list if abs(
                            m.coords[0] - nx) <= 1 and abs(m.coords[1] - ny) <= 1 and m.mob_id != mob.mob_id])
                elif "Δ" in target_cell and mob.mob_type not in ["Strong", "Elder", "Ancient"]:
                    # Reproduction logic: 10% chance to reproduce into an adjacent cell
                    if mob.energy > 750 and not self.check_area(nx, ny, char="Δ", num=3):
                        rdx = random.randint(-1, 1)
                        rdy = random.randint(-1, 1)
                        rx = max(0, min(self.max_x, nx + rdx))
                        ry = max(0, min(self.max_y, ny + rdy))
                        # only place if target cell looks empty
                        if (" " == self.world.chunk[ry][rx]) or ("░" in self.world.chunk[ry][rx]):
                            self.world.chunk[ry][rx] = "Δ"
                            new_mobs.append(Mob(
                                self.world.diff, mob.old_type, f"mob_{len(mob_list)+len(new_mobs)}", mob.energy*random.gauss(1, 0.1), (rx, ry), 0))
                            # reduce energy on reproduction
                            mob.energy -= 500
                elif "Δ" in target_cell and mob.mob_type in ["Strong", "Elder", "Ancient"]:
                    target = next(
                        (m for m in mob_list if m.coords == (nx, ny)), None)
                    if target:
                        fight.fight(
                            mob, target)
                    if mob.mob_type in ["Strong", "Elder", "Ancient"] and random.random() > 0.95:
                        fight.aoe_damage(mob, [m for m in mob_list if abs(
                            m.coords[0] - nx) <= 1 and abs(m.coords[1] - ny) <= 1 and m.mob_id != mob.mob_id])
                elif "λ" in target_cell and mob.mob_type not in ["Strong", "Adult", "Ancient"]:
                    # Reproduction logic: 5% chance to reproduce into an adjacent cell
                    if mob.energy > 1000 and not self.check_area(nx, ny, char="λ", num=3):
                        rdx = random.randint(-1, 1)
                        rdy = random.randint(-1, 1)
                        rx = max(0, min(self.max_x, nx + rdx))
                        ry = max(0, min(self.max_y, ny + rdy))
                        # only place if target cell looks empty
                        if (" " == self.world.chunk[ry][rx]) or ("░" in self.world.chunk[ry][rx]):
                            self.world.chunk[ry][rx] = "λ"
                            new_mobs.append(Mob(
                                self.world.diff, mob.old_type, f"mob_{len(mob_list)+len(new_mobs)}", mob.energy*random.gauss(1, 0.1), (rx, ry), 0))
                            # reduce energy on reproduction
                            mob.energy -= 750
                elif "λ" in target_cell and mob.mob_type in ["Strong", "Adult", "Ancient"]:
                    target = next(
                        (m for m in mob_list if m.coords == (nx, ny)), None)
                    if target:
                        fight.fight(
                            mob, target)
                    if mob.mob_type in ["Strong", "Adult", "Ancient"] and random.random() > 0.95:
                        fight.aoe_damage(mob, [m for m in mob_list if abs(
                            m.coords[0] - nx) <= 1 and abs(m.coords[1] - ny) <= 1 and m.mob_id != mob.mob_id])
                elif "Ψ" in target_cell and mob.mob_type == "Ancient":
                    # Reproduction logic: 2.5% chance to reproduce into an adjacent cell
                    if mob.energy > 1250 and not self.check_area(nx, ny, char="Ψ", num=3):
                        rdx = random.randint(-1, 1)
                        rdy = random.randint(-1, 1)
                        rx = max(0, min(self.max_x, nx + rdx))
                        ry = max(0, min(self.max_y, ny + rdy))
                        # only place if target cell looks empty
                        if (" " == self.world.chunk[ry][rx]) or ("░" in self.world.chunk[ry][rx]):
                            self.world.chunk[ry][rx] = "Ψ"
                            new_mobs.append(Mob(
                                self.world.diff, mob.old_type, f"mob_{len(mob_list)+len(new_mobs)}", mob.energy*random.gauss(1, 0.1), (rx, ry), 0))
                            # reduce energy on reproduction
                            mob.energy -= 1000
                elif "Ψ" in target_cell and mob.mob_type != "Ancient":
                    target = next(
                        (m for m in mob_list if m.coords == (nx, ny)), None)
                    if target:
                        fight.fight(
                            mob, target)
                    if mob.mob_type in ["Strong", "Elder", "Ancient"] and random.random() > 0.95:
                        fight.aoe_damage(mob, [m for m in mob_list if abs(
                            m.coords[0] - nx) <= 1 and abs(m.coords[1] - ny) <= 1 and m.mob_id != mob.mob_id])
                elif "Ω" in target_cell and mob.mob_type == "Strong":
                    if mob.energy > 750 and not self.check_area(nx, ny, char="Ω", num=3):
                        rdx = random.randint(-1, 1)
                        rdy = random.randint(-1, 1)
                        rx = max(0, min(self.max_x, nx + rdx))
                        ry = max(0, min(self.max_y, ny + rdy))
                        # only place if target cell looks empty
                        if (self.world.chunk[ry][rx] == " ") or ("░" in self.world.chunk[ry][rx]):
                            self.world.chunk[ry][rx] = "Ω"
                            new_mobs.append(Mob(
                                self.world.diff, "Strong", f"mob_{len(mob_list)+len(new_mobs)}", mob.energy*random.gauss(1, 0.1), (rx, ry), 0))
                            mob.energy -= 500  # reduce energy on reproduction
                elif "Ω" in target_cell and mob.mob_type != "Strong":
                    target = next(
                        (m for m in mob_list if m.coords == (nx, ny)), None)
                    if target:
                        fight.fight(
                            mob, target)
                    if mob.mob_type in ["Adult", "Elder", "Ancient"] and random.random() > 0.95:
                        fight.aoe_damage(mob, [m for m in mob_list if abs(
                            m.coords[0] - nx) <= 1 and abs(m.coords[1] - ny) <= 1 and m.mob_id != mob.mob_id])
                else:
                    # If target cell is something else (like a wall), also restore old position
                    mob.coords = (ox, oy)
        self.corpse_decay()
        
        if random.random() > 0.99:
            center = self.max_x//2, self.max_y//2
            fight.aoe_damage(nuke, mob_list)
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

    def dead_mobs(self, arr: list[Mob]) -> None:
        """
        The `dead_mobs` function marks mobs with zero energy as corpses in the game world and removes them
        from the list of active mobs.

        :param arr: The `arr` parameter is a list of dictionaries representing mobs in a game. Each
        dictionary in the list contains information about a mob, such as its energy level (`"energy"`) and
        position (`"pos"`). The `dead_mobs` method iterates over this list, checks if a
        """
        for mob in arr[:]:  # Use a copy to avoid modifying list during iteration
            if mob.energy <= 0:
                x, y = mob.coords
                self.world.chunk[y][x] = "*"  # Mark as corpse
                self.corpse_list.append([(x, y), 0])  # Add corpse to decay list
                arr.remove(mob)  # Remove from active mobs

    def corpse_decay(self) -> None:
        """
        The `corpse_decay` function simulates the decay of corpses in a game world by removing them
        """
        for corpse in self.corpse_list[:]:
            x,y = corpse[0]
            corpse[1] += 1
            if corpse[1] > self.corpse_decay_time:
                self.world.chunk[y][x] = " "
                self.corpse_list.remove(corpse)
                


if __name__ == "__main__":
    print("Run idle_game.py to see the mob AI in action! dumahh")
