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
        self.max_x = self.col - 1
        self.max_y = self.row - 1
        self.seconds = 1 #! 1 for real movement 60 for faster paced movement (will be kinda strange to watch but good for testing)

    def brownian_motion(self, mob_list: list[Any],count:int) -> None:
        mon_types = {"Weak": "ᵟ", "Strong": "Ω"}

        new_mobs: list[dict[str, Any]] = []

        for mob in list(mob_list):
            for _ in range(self.seconds):  # simulate multiple steps
                # stored positions are (x, y)
                x, y = mob["pos"]
                ox, oy = x, y  # old position

                dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                nx = max(0, min(self.max_x, x + dx))
                ny = max(0, min(self.max_y, y + dy))

                #? check if new pos is a corpse
                if "*" in self.world.chunk[ny][nx]:
                    continue

                target_cell = self.world.chunk[ny][nx]
                if " " in target_cell or "░" in target_cell:
                    old_terrain = "░"
                    self.world.chunk[oy][ox] = old_terrain  # restore old terrain
                    self.world.chunk[ny][nx] = mon_types[mob["type"]]  # move mob
                    mob["pos"] = (nx, ny)
                elif "ᵟ" in target_cell:
                    # Reproduction logic: 5% chance to reproduce into an adjacent cell
                    if random.random() > 0.95 and not self.check_area(nx, ny,char="ᵟ",num=3):
                        dx = random.randint(-1, 1)
                        dy = random.randint(-1, 1)
                        rx = max(0, min(self.max_x, nx + dx))
                        ry = max(0, min(self.max_y, ny + dy))
                        # only place if target cell looks empty
                        if (" " == self.world.chunk[ry][rx]) or ("░" in self.world.chunk[ry][rx]):
                            self.world.chunk[ry][rx] = "ᵟ"
                            new_mobs.append({"type": "Weak", "pos": (rx, ry)})
                elif "Ω" in target_cell:  # mob collision
                    # For simplicity, just restore old position (no combat logic)
                    if random.random() < 0.25:  # 25% chance to "win" and move into the cell
                        self.world.chunk[oy][ox] = "*"  # Clear old position
                    if self.check_area(nx, ny,char="*"):
                        self.world.chunk[ny][nx] = "Ω" #! mmob wins and creates child
                    mob["pos"] = (ox, oy)
                else:
                    # If target cell is something else (like a wall), also restore old position
                    mob["pos"] = (ox, oy)

        # Add newborns after processing to avoid mutating while iterating
        if new_mobs:
            mob_list.extend(new_mobs)
    def check_area(self, x: int, y: int,char:str,num:int=0,area:tuple[int, int] = (3, 3)) -> bool:
        count = 0
        for dy in range(-area[1]//2, area[1]//2 + 1):
            for dx in range(-area[0]//2, area[0]//2 + 1):
                nx = max(0, min(self.max_x, x + dx))
                ny = max(0, min(self.max_y, y + dy))
                if char in self.world.chunk[ny][nx]:
                    count += 1

        return count > num
"""# ...existing code...
                elif "ᵟ" in self.world.chunk[y][x] :
                    # For simplicity, just restore old position (no combat logic)
                    if random.random() > 0.8 :
-                        b = random.randint(0,2)
-                        a = random.randint(0,2)
-                        self.world.chunk[y-b][x-a] = "ᵟ"
-                        mob_list.append({"type": "Weak", "pos": (y-b,x-a)})
+                        # spawn a new weak mob nearby; clamp to bounds and keep (x,y) order
+                        dx = random.randint(-2, 2)
+                        dy = random.randint(-2, 2)
+                        nx = max(0, min(self.max_x, x + dx))
+                        ny = max(0, min(self.max_y, y + dy))
+                        # only place if target cell looks empty
+                        if self.world.chunk[ny][nx] == " " or "░" in self.world.chunk[ny][nx]:
+                            self.world.chunk[ny][nx] = "ᵟ"
+                            mob_list.append({"type": "Weak", "pos": (nx, ny)})
# ...existing code..."""