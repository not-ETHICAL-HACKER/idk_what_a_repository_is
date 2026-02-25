import random
#! from colorama import Fore, Style, init
from mob_ai import Mob
#! init(autoreset=True)


class gen:
    def __init__(self, seed:str, world_size: tuple[int, int], monster_density: float,diff:str):
        self.seed = sum(ord(c) for c in seed)
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
                                        "W": "Ω",  # Weak Mob
                                        }
        self.chunk: list[list[str]] = []
        

    def generate(self,mon_list:list[tuple[Mob,tuple[int, int]]] = []) -> None:
        for y in range(self.size[0]):
            row = ""
            for x in range(self.size[1]):#? thers smth wrong with the way mobs are generated,
                                        #? i thoght i made only preys but i made the predators without their ability to move
                if random.random() < self.monster_density:
                    row += f"{self.terrain['W']:2s}"  #! Predator # i also dont know why the predator spawns outside the chunk but the prey spawns inside the chunk
                    mon_list.append((Mob(self.diff, "Weak", f"mob_{len(mon_list)}", False, False),(x, y))) # Prey
                else:
                    row += self.terrain["0"]  # Empty terrain
            self.chunk.append(list(row))
            print(row)
    
    def render(self) -> None:
        for row in self.chunk:
            print("".join(row))
