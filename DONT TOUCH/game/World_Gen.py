from typing import Any
from colorama import init, Fore, Back, Style
import random
init(autoreset=True)

mon_types: dict[str, str] = {"Weak": "ᵟ", "Strong": "Ω"}

class Generate_World:
    def __init__(self, seed: int | str):
        self.player_pos: tuple[int, int, int] = (0, 0, 0)
        self.chunk_size = 11
        self.chunk = [[" "]*self.chunk_size for _ in range(self.chunk_size)]
        if isinstance(seed, str):
            seed = sum(ord(c) for c in seed)
        random.seed(seed)

    def generate_location(self) -> str:
        locations = ["Forest", "Desert",
                     "Mountain", "River", "Cave", "Village"]
        return random.choice(locations)

    def spawn_chunk(self, size: int) -> tuple[int, int, int]:
        x = y = z = 0
        #!path=[]
        dir = list("NSEWUD")
        while True:
            for _ in range(size):
                random.shuffle(dir)
                a = [dir[0]]
                #!path+=a
                if a == ['N']:
                    y += 1
                elif a == ['S']:
                    y -= 1
                elif a == ['E']:
                    x += 1
                elif a == ['W']:
                    x -= 1
                elif a == ['U']:
                    z += 1
                elif a == ['D']:
                    z -= 1
            sun = (x**2+y**2+z**2)**0.5
            if x+self.chunk_size//2 < 0 or y+self.chunk_size//2 < 0:
                continue
            print(f"(x : {x}, y : {y}, z : {z})\n")
            #!print(path[:100])
            print(f"Distance from origin: {sun}")
            self.player_pos = x, y, z
            return x, y, z

    def display_chunk(self, coords: tuple[int, int, int]) -> list[str]:
        size = len(self.chunk)
        cx, cy, _ = coords
        self.player_icons: list[str] = ["|", "⨋", "⨌", "⨍", "⨎"]
        self.player_icon: str = self.player_icons[2] 
        self.terrain: dict[str, str] = {
            "0": Style.BRIGHT+Fore.GREEN + "░",  # Grass
            "1": Style.BRIGHT+Fore.GREEN + "▲",  # Tree
            "2": Style.BRIGHT+Fore.BLUE + "≈",  # Water
            "3": Style.BRIGHT+Fore.YELLOW + "#",  # Sand
            "4": Style.BRIGHT+Fore.GREEN + "|",  # Cactus
            "5": Style.BRIGHT+Fore.BLUE + "≈",  # Water
            "6": Style.BRIGHT+Fore.LIGHTGREEN_EX + "*",  # Rock
            "7": Style.BRIGHT+Fore.BLUE + "❄",  # Snow
            "8": Style.BRIGHT+Fore.LIGHTBLACK_EX + "⏵",  # Cliff
            "9": Style.BRIGHT+Fore.BLUE + "≈",  # Water
            "10": Style.BRIGHT+Fore.GREEN + "░",  # Grass
            "11": Style.BRIGHT+Fore.GREEN + "▞",  # Mud
            "12": Style.BRIGHT+Fore.LIGHTGREEN_EX + "*",  # Rock
            "13": Style.BRIGHT+Fore.LIGHTMAGENTA_EX + "▼",  # Stalagmite
            "14": Style.BRIGHT+Fore.LIGHTMAGENTA_EX + "^", # Stalagtite
            "15": Style.BRIGHT + Fore.RED + "⌂",  # House
            "16": "16",
            "17": "17",
            "18": "18",
            "W": Style.BRIGHT+Fore.MAGENTA + "ᵟ",  # Weak Mob
            "S": Style.BRIGHT+Fore.RED + "Ω",     # Strong Mob
            "ᵟ": Style.BRIGHT+Fore.MAGENTA + "ᵟ",  # Weak Mob
            "Ω": Style.BRIGHT+Fore.RED + "Ω",     # Strong Mob
        }
        l: list[str] = []
        for i, row in enumerate(self.chunk):
            line: list[str] = []
            for j, cell in enumerate(row):
                if (i, j) == ((cx+size//2) % self.chunk_size, (cy+size//2) % self.chunk_size):
                    icon_text = f"{self.player_icon:^1s}"
                    line.append(Fore.RED + Style.BRIGHT +
                                icon_text + Style.RESET_ALL)  # Player position
                    self.player_pos = i, j, _
                else:
                    line.append(Fore.WHITE+Style.BRIGHT+Back.BLACK +
                                self.terrain[str(cell)].center(2))
            l.append("".join(line))
            print(" ".join(line))
        return l

    def gen_terrain(self, biome: str, difficulty: str) -> None:
        self.biome = biome
        self.difficulty = difficulty
        for i in range(self.chunk_size):
            for j in range(self.chunk_size):
                if self.biome == "Forest":
                    self.chunk[i][j] = random.choices(
                        # 0 : grass, 1: tree, 2: water
                        ["0", "1", "2"], weights=[70, 20, 10])[0]
                elif self.biome == "Desert":
                    self.chunk[i][j] = random.choices(
                        # 3: sand, 4: cactus, 5: water
                        ["3", "4", "5"], weights=[80, 15, 5])[0]
                elif self.biome == "Mountain":
                    self.chunk[i][j] = random.choices(
                        # 6: rock, 7: snow, 8: cliff
                        ["6", "7", "8"], weights=[60, 30, 10])[0]
                elif self.biome == "River":
                    self.chunk[i][j] = random.choices(
                        # 9: water, 10: grass, 11: mud
                        ["9", "10", "11"], weights=[50, 40, 10])[0]
                elif self.biome == "Cave":
                    self.chunk[i][j] = random.choices(
                        # 12: rock, 13: stalactite, 14: stalagmite
                        ["12", "13", "14"], weights=[70, 15, 15])[0]
                elif self.biome == "Village":
                    self.chunk[i][j] = random.choices(
                        # 15: house, 16: road, 17: farm
                        ["15", "16", "17"], weights=[50, 30, 20])[0]

                #! add more biomes
                #! adjust weights based on difficulty
        #! implement terrain generation based on biome and difficulty
        return None

    def gen_structures(self) -> None:
        #! implement structure generation
        return None
    
    def gen_resources(self) -> None:
        #! implement resource generation
        return None

    def gen_mobs(self, diff: str, mob_list: list[dict[str, Any]]) -> None:
        

        for i in range(self.chunk_size):
            for j in range(self.chunk_size):
                roll = random.random()

                if diff == "Easy":
                    if roll < 0.15:
                        mob_list.append({"type": "Weak", "pos": (i, j)})
                        self.chunk[i][j] = "W"
                    elif roll > 0.95:
                        mob_list.append({"type": "Strong", "pos": (i, j)})
                        self.chunk[i][j] = "S"
                elif diff == "Normal":
                    if roll < 0.2:
                        mob_list.append({"type": "Weak", "pos": (i, j)})
                        self.chunk[i][j] = "W"
                    elif roll < 0.3:
                        mob_list.append({"type": "Strong", "pos": (i, j)})
                        self.chunk[i][j] = "S"
                elif diff == "Hard":
                    if roll < 0.3:
                        mob_list.append({"type": "Strong", "pos": (i, j)})
                        self.chunk[i][j] = "S"
                    elif roll < 0.8:
                        mob_list.append({"type": "Weak", "pos": (i, j)})
                        self.chunk[i][j] = "W"
                else:
                    if roll > 0.2:
                        mob_list.append({"type": "Strong", "pos": (i, j)})
                        self.chunk[i][j] = "S"
        for i,char in enumerate(mob_list):
            char["ID"] = (
        mon_types[char["type"]] +
        chr(65 + (i % 26)) +
        str(i)
    )