from numpy import half
from world_gen import gen
from typing import Any
import random
class Mobs:
    def __init__(self, world: gen ):
        self.world:gen = world
        self.row, self.col = world.size
        self.seconds =  6

    def brownian_motion(self, mob_list: list[Any]) -> None:
        half_r = self.row//2 - 1
        half_c = self.col//2 - 1
        mon_types = {"Weak": "ᵟ", "Strong": "Ω"}
        for _ in range(self.seconds): #! emulating dnd mechanics
            for mob in mob_list:
                x, y = mob["pos"]
                ox, oy = x, y

                dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                x = max(0, min(half_c, x + dx))
                y = max(0, min(half_r, y + dy))

                if world.chunk[x][y] in ["0", "3", "6", "10", "11", "2", "5", "12", "16"]:
                    old_terrain = world.chunk[x][y]
                    world.chunk[ox][oy] = old_terrain
                    world.chunk[x][y] = mon_types[mob["type"]]
                    mob["pos"] = (x, y)