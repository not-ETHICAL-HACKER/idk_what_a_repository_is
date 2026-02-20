from typing import Any
import random
class Mob:
    def __init__(self, difficulty: str, mob_type: str, mob_id: str, boss: bool, evolve: bool):
        self.difficulty = difficulty
        self.mob_type = mob_type
        self.mob_id = mob_id
        self.boss = boss
        self.evolve = evolve
class Mob_AI:
    def __init__(self, world: Any ):
        self.world:Any = world
        self.row, self.col = world.size
        self.seconds = 1 #! 1 for real movement 60 for faster paced movement (will be kinda strange to watch but good for testing)

    def brownian_motion(self, mob_list: list[Any]) -> None:
        max_y = self.row - 1  # row = number of rows
        max_x = self.col - 1  # col = number of columns
        mon_types = {"Weak": "ᵟ", "Strong": "Ω"}

        for mob in mob_list:
            for _ in range(self.seconds):  # simulate multiple steps
                x, y = mob["pos"]
                ox, oy = x, y  # old position

                dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                x = max(0, min(max_x, x + dx))
                y = max(0, min(max_y, y + dy))

                # Only move if target cell is empty terrain
                if " " in self.world.chunk[y][x] or "░" in self.world.chunk[y][x]:
                    old_terrain = "░"         #?self.world.chunk[oy][ox]
                    self.world.chunk[oy][ox] = old_terrain  # restore old terrain
                    self.world.chunk[y][x] = mon_types[mob["type"]]  # move mob
                    mob["pos"] = (x, y)
                elif  "ᵟ" in self.world.chunk[y][x] :
                    # For simplicity, just restore old position (no combat logic)
                    mob["pos"] = (ox, oy)
                elif "Ω" in self.world.chunk[y][x]:  # mob collision
                    # For simplicity, just restore old position (no combat logic)
                    if random.random() < 0.5:  # 50% chance to "win" and move into the cell
                        self.world.chunk[oy][ox] = "*"  # Clear old position
                    mob["pos"] = (ox, oy)
                else:
                    # If target cell is something else (like a wall), also restore old position
                    mob["pos"] = (ox, oy)
