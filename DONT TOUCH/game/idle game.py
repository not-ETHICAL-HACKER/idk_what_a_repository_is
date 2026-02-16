from World_Gen import Generate_World
from typing import Any
diff = "hard"
mob_list: list[tuple[Any, tuple[int, int]]] = []
world = Generate_World(seed=42)
world.gen_terrain(biome="Forest", difficulty=diff, debug_location=True)
world.gen_mobs(diff, mob_list)
world.display_chunk((0, 0, 0))