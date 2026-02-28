"""This module is responsible for generating the game world based on a seed and specified parameters. It creates a grid of terrain and populates it with mobs according to the defined monster density. The generated world can be rendered to the console for visualization."""
import random
#! from colorama import Fore, Style, init
from mob_ai import Mob
#! init(autoreset=True)


# This Python class `gen` generates a world with specified size, monster density, and difficulty
# level, populating it with weak and strong mobs.
class gen:
    def __init__(self, seed:str, world_size: tuple[int, int], monster_density: float,diff:str):
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
        """self.terrain:dict[str,str] = {  "0":Style.BRIGHT+Fore.GREEN + " " ,#? "░",
                                        "W": Style.BRIGHT+Fore.MAGENTA + "ᵟ",  # Weak Mob
                                        "DW": Style.BRIGHT+Fore.LIGHTBLACK_EX + "ᵟ",  # Dead Weak Mob
                                        "S": Style.BRIGHT+Fore.RED + "Ω",     # Strong Mob
                                        "DS": Style.DIM+Fore.LIGHTBLACK_EX + "Ω",     # Dead Strong Mob
                                        "ᵟ": Style.BRIGHT+Fore.MAGENTA + "ᵟ",  # Weak Mob
                                        "Ω": Style.BRIGHT+Fore.RED + "Ω",     # Strong Mob
                                    }"""
        self.terrain:dict[str,str] = {  "0": " ", #?"░",
                                        "W": "ᵟ",  # Weak Mob
                                        "S": "Ω",     # Strong Mob
                                        }
        self.chunk: list[list[str]] = []
        

    def generate(self,mon_list:list[tuple[Mob,tuple[int, int]]] = []) -> None:
        """
        This function generates mobs with varying strengths on a grid based on a specified monster
        density.
        
        :param mon_list: The `mon_list` parameter in the `generate` method is a list of tuples. Each
        tuple contains a `Mob` object and a tuple representing the coordinates `(x, y)` of the mob in
        the grid. The `Mob` object is created based on certain conditions such as mob strength (
        :type mon_list: list[tuple[Mob,tuple[int, int]]]
        """
        for y in range(self.size[0]):
            row = ""
            for x in range(self.size[1]):#? thers smth wrong with the way mobs are generated,
                                        #? i thoght i made only preys but i made the predators without their ability to move
                if random.random() < self.monster_density:
                    # decide mob strength first, then write terrain and mob object to match
                    is_weak = random.random() < 0.7
                    terrain_key = 'W' if is_weak else 'S'
                    row += self.terrain[terrain_key]
                    mob_type = "Weak" if is_weak else "Strong"
                    mon_list.append((Mob(self.diff, mob_type, f"mob_{len(mon_list)}", False, False),(x, y)))
                else:
                    row += self.terrain["0"]  # Empty terrain
            self.chunk.append(list(row))
    
    def render(self) -> None:
        """
        The `render` function iterates through each row in the `chunk` attribute and prints the
        concatenated characters in each row.
        """
        for row in self.chunk:
            print("".join(row))

