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
        max_x = self.col - 1
        max_y = self.row - 1
        self.seconds = 1 #! 1 for real movement 60 for faster paced movement (will be kinda strange to watch but good for testing)

    def brownian_motion(self, mob_list: list[Any]) -> None:
        max_y = self.row - 1  # row = number of rows
        max_x = self.col - 1  # col = number of columns
        mon_types = {"Weak": "ᵟ", "Strong": "Ω"}

        for mob in mob_list:
            for _ in range(self.seconds):  # simulate multiple steps
                y, x = mob["pos"]
                ox, oy = x, y  # old position

                dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                x = max(0, min(max_x, x + dx))
                y = max(0, min(max_y, y + dy))

                # Only move if target cell is empty terrain
                if "*" in self.world.chunk[oy][ox]:
                    continue
                if " " in self.world.chunk[y][x] or "░" in self.world.chunk[y][x]:
                    old_terrain = "░"         #?self.world.chunk[oy][ox]
                    self.world.chunk[oy][ox] = old_terrain  # restore old terrain
                    self.world.chunk[y][x] = mon_types[mob["type"]]  # move mob
                    mob["pos"] = (x, y)
                elif  "ᵟ" in self.world.chunk[y][x] :
                    #? Reproduction logic: 20% chance to reproduce into an adjacent cell
                    if random.random() > 0.8 :
                        b = random.randint(0,2)
                        a = random.randint(0,2)
                        self.world.chunk[y-b][x-a] = "ᵟ"
                        mob_list.append({"type": "Weak", "pos": ((y-b)%max_y,(x-a)%max_x)})
                        #! create a mob instance here so tht the generated mob can move
                        #! figured outthe bug with the omega pieces
                        #! i accidentally made them a part ofterrain instead of their own objects
                        #! omega is predator and the other is prey
                elif "Ω" in self.world.chunk[y][x]:  # mob collision
                    # For simplicity, just restore old position (no combat logic)
                    if random.random() < 0.5:  # 50% chance to "win" and move into the cell
                        self.world.chunk[oy][ox] = "*"  # Clear old position
                    mob["pos"] = (ox, oy)
                else:
                    # If target cell is something else (like a wall), also restore old position
                    mob["pos"] = (ox, oy)
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
+                        nx = max(0, min(max_x, x + dx))
+                        ny = max(0, min(max_y, y + dy))
+                        # only place if target cell looks empty
+                        if self.world.chunk[ny][nx] == " " or "░" in self.world.chunk[ny][nx]:
+                            self.world.chunk[ny][nx] = "ᵟ"
+                            mob_list.append({"type": "Weak", "pos": (nx, ny)})
# ...existing code..."""