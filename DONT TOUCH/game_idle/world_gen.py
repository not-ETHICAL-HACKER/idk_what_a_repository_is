import random
from colorama import Fore, Style, init
init(autoreset=True)


class gen:
    def __init__(self, seed:str, world_size: tuple[int, int], monster_density: float):
        self.seed = sum(ord(c) for c in seed)
        self.size = world_size
        self.monster_density = monster_density

    def generate(self):
        grass = Style.BRIGHT+Fore.GREEN + "░"  # Grass
        for y in range(self.world_size[1]):
            row = ""
            for x in range(self.world_size[0]):
                random.seed(self.seed + x * self.world_size[1] + y)
                if random.random() < self.monster_density:
                    row += f"{Style.BRIGHT+Fore.RED + "#":1^}"  # Monster
                else:
                    row += grass
            print(row)


if __name__ == "__main__":
    world_seed = input("Enter world seed (integer or string): ")
    size = (20, 10)  # Width x Height
    mob_density = 0.1  # 10% chance of a monster in each cell
    world = gen(world_seed, size, mob_density)
    world.generate()