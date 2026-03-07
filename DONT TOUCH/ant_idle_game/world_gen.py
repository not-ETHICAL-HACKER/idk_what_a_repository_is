"""This module is responsible for generating the game world based on a seed and specified parameters. It creates a grid of terrain and populates it with mobs according to the defined monster density. The generated world can be rendered to the console for visualization."""
import random
from colorama import Back, Fore, Style, init
from mob_ai import Mob, Mob_AI
init(autoreset=True)

# This Python class `gen` generates a world with specified size, monster density, and difficulty
# level, populating it with weak and strong mobs.
class gen:
    def __init__(self, seed: str, world_size: tuple[int, int], monster_density: float, diff: str):
        """
        The function initializes attributes for a game world based on input parameters.

        :param seed: The `seed` parameter is a string used to initialize the random number generator for
        generating the game world. It is converted into a numerical value by summing the ASCII values of
        its characters. This numerical value is then used to seed the random number generator
        :type seed: str
        :param world_size: The `world_size` parameter is a tuple that represents the dimensions of the
        game world. It specifies the width and height of the world in terms of grid units. For example,
        if `world_size` is `(10, 10)`, it means the game world has a width of 10
        :type world_size: tuple[int, int]
        :param monster_density: The `monster_density` parameter represents the density of monsters in
        the game world. It is a float value that determines how many monsters are present in a given
        area of the game world. A higher `monster_density` value means there are more monsters in the
        world, while a lower value means there are
        :type monster_density: float
        :param diff: The `diff` parameter in the `__init__` method seems to represent the difficulty
        level of the game. It is a string that likely indicates the chosen difficulty setting for the
        game. This parameter could be used to adjust various aspects of the game such as monster
        strength, resource availability, or any
        :type diff: str
        """
        self.seed = sum(ord(c) for c in seed)
        random.seed(self.seed)
        self.diff = diff
        self.size = world_size
        self.monster_density = monster_density
        self.terrain: dict[str, str] = {"0": " ",  # ?"░",
                                        "1": "≈", # water
                                        "W": "ᵟ",  # Weak Mob
                                        "S": "Ω",     # Strong Mob
                                        }
        self.chunk: list[list[str]] = []

    def generate(self, mon_list: list[Mob] = []) -> None:
        """
        This function generates mobs with varying strengths on a grid based on a specified monster
        density.

        :param mon_list: The `mon_list` parameter in the `generate` method is a list of `Mob` objects.
        Each `Mob` object represents a mobile entity in the game world with specific attributes and
        behaviors.
        :type mon_list: list[Mob]
        """
        
        for y in range(self.size[0]):
            row = ""
            for x in range(self.size[1]):
                if random.random() < self.monster_density:
                    # decide mob strength first, then write terrain and mob object to match
                    is_weak = random.random() < 0.8
                    terrain_key = 'W' if is_weak else 'S'
                    row += self.terrain[terrain_key]
                    mob_type = "Weak" if is_weak else "Strong"
                    mon_list.append(Mob(self.diff, mob_type, f"mob_{len(mon_list)}", random.randint(500, 1000), (x, y), 0))
                else:
                    row += self.terrain["0"]  # Empty or water terrain
            self.chunk.append(list(row))

    def render(self) -> None:
        """
        The `render` function uses a color map to print styled characters from a chunk.
        """
        COLOR_MAP: dict[str, str] = {
            "ᵟ": Fore.GREEN + Style.BRIGHT + "ᵟ",
            "Ω": Fore.RED + Style.BRIGHT + "Ω",
            "Ψ": Fore.YELLOW + Style.BRIGHT + "Ψ",
            "λ": Fore.MAGENTA + Style.BRIGHT + "λ",
            "Δ": Fore.CYAN + Style.BRIGHT + "Δ",
            "*": Style.DIM + Fore.WHITE + "*",
            "≈": Fore.CYAN + Style.BRIGHT + "≈",
            "░": Fore.GREEN + Style.BRIGHT + "░",
        }
        for row in self.chunk:
            print("".join(Back.BLACK+COLOR_MAP.get(cell, cell) +
                  Style.RESET_ALL for cell in row))

    def grow_up(self, mon_list: list[Mob]) -> None:
        """
        The `grow_up` function iterates through a list of mobs and calls their `grow` method to
        simulate growth or aging.

        :param mon_list: The `mon_list` parameter in the `grow_up` method is a list of `Mob` objects.
        Each `Mob` object represents a mobile entity in the game world with specific attributes and
        behaviors. The `grow_up` method likely simulates the passage of time for these mobs, allowing
        them to age or develop based on their individual growth mechanics.
        :type mon_list: list[Mob]
        """
        for mob in mon_list:
            mob.grow()
if __name__ == "__main__":
    print("Run idle_game.py to see the world generation in action! dumahh")
