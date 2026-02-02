from Player import Player
import random
from typing import Any


# The `Monster` class in Python represents a monster entity with attributes for movement and loot
# drops, including a method for simulating Brownian motion movement behavior.
class Monster(Player):
    """This was originally intended to be the base class for all mobs, but was later replaced by the Mob class.\nNow it serves as a helper class for general monster behavior like movement and loot dropping."""
    def __init__(self):
        super().__init__(name="Monster")
        self.seconds = 6  # a mob moves every second and im tryin to emulate dnd mechanics
        self.mob_pos_list: list[dict[str, tuple[int, int] | str]] = []

    def loot_drop(self, player: Player) -> list[str]:
        # todo: change this func to implement the lootable class of loot_table.py
        loot: list[str] = []
        gold_dropped = random.randint(1, 10) * self.level
        loot.append(f"{gold_dropped} Gold Coins")
        if random.random() < 0.3:
            loot.append("Health Potion")
        if random.random() < 0.2:
            loot.append("Mana Potion")
        if random.random() < 0.1:
            loot.append("Rare Item")
        for item in loot:
            player.add_to_inventory(item)
        return loot

    def brownian_motion(self, mob_list: list[Any], world: Any ) -> None:
        half = world.chunk_size - 1
        mon_types = {"Weak": "ᵟ", "Strong": "Ω"}
        for _ in range(self.seconds): #! emulating dnd mechanics
            for mob in mob_list:
                x, y = mob["pos"]
                ox, oy = x, y

                dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                x = max(0, min(half, x + dx))
                y = max(0, min(half, y + dy))

                if world.chunk[x][y] in ["0", "3", "6", "10", "11", "2", "5", "12", "16"]:
                    old_terrain = world.chunk[x][y]
                    world.chunk[ox][oy] = old_terrain
                    world.chunk[x][y] = mon_types[mob["type"]]
                    mob["pos"] = (x, y)

# The `Mob` class represents a game monster with attributes such as difficulty level, health points,
# damage, type, boss status, and methods for attacking players and checking status.
class Mob:
    """
    Mob entity with difficulty, type, boss status, and evolution mechanics.
    
    Attributes:

    - difficulty (str): The difficulty level of the mob (Easy, Normal, Hard).
    - mob_type (str): The type of the mob (e.g., Weak, Strong
    - mob_id (str): A unique identifier for the mob.
    - Boss (bool): Indicates if the mob is a boss.
    - Evolve (bool): Indicates if the mob can evolve.
    - is_alive (bool): Indicates if the mob is alive.

    Methods:
    - attack_player(player: Player) -> float: Simulates an attack on a player and returns damage dealt.
    - monster_info() -> str: Returns a string with detailed information about the mob.
    - check_mob_status() -> None: Checks if the mob is alive based on its health points.
    
    To Implement:

    - make the mob drop loot using the LOOT_TABLE class
    - add more mob behaviors and interactions
    - implement mob evolution mechanics
    - make the mobs actually die and respawn
    """
    def __init__(self, diff: str, mob_id: str, Type: str, Boss: bool, Evolve: bool, Is_Alive: bool = True) -> None:
        self.difficulty: str = diff
        self.Evolve = Evolve
        self.mob_type = Type
        self.mob_id = mob_id
        self.Boss = Boss
        self.is_alive = Is_Alive
        self.attack_speed = max(random.random(), 0.1)
        self.seconds = 6  # a mob moves every second and im tryin to emulate dnd mechanics
        self.pos: tuple[int, int] = (0, 0)
        self.mob_pos_list: list[dict[str | int, tuple[int, int] | str]] = []
        if self.difficulty == "Easy":
            self.level = random.randint(1, 5)+(1 if "ᵟ" not in Type else 0)
            self.hp = random.randint(20, 50)+(10 if "ᵟ" not in Type else 0)
            self.dmg = random.randint(1, 5)+(5 if "ᵟ" not in Type else 0)
        elif self.difficulty == "Normal":
            self.level = random.randint(5, 15)+(5 if "ᵟ" not in Type else 0)
            self.hp = random.randint(50, 100)+(25 if "ᵟ" not in Type else 0)
            self.dmg = random.randint(5, 15)+(7 if "ᵟ" not in Type else 0)
        elif self.difficulty == "Hard":
            self.level = random.randint(15, 30)+(10 if "ᵟ" not in Type else 0)
            self.hp = random.randint(100, 150)+(50 if "ᵟ" not in Type else 0)
            self.dmg = random.randint(15, 30)+(10 if "ᵟ" not in Type else 0)
        if self.Boss:
            self.level *= 2
            self.hp *= 3
            self.dmg *= 2
        if self.Evolve:
            self.hp *= 1.5
            self.dmg *= 1.5

    def __repr__(self) -> str:
        return f"[{self.mob_id}: {self.mob_type}, HP: {int(self.hp)},DMG: {int(self.dmg)}, Lvl: {self.level}, {self.Evolve=}, {self.Boss=}, {self.is_alive=}]"

    def attack_player(self, player: Player) -> float:
        damage_dealt = self.dmg * (1 + random.uniform(-0.1, 0.1))
        player.hp -= damage_dealt
        return damage_dealt

    def monster_info(self) -> str:
        info: str = (
            f"Monster Level: {self.level}\n"
            f"Monster HP: {self.hp}\n"
            f"Monster DMG: {self.dmg}\n"
            f"Monster ATK SPD: {self.attack_speed}\n"
            f"Monster Type: {self.mob_type}\n"
            f"Monster Boss: {self.Boss}\n"
            f"Monster Evolve: {self.Evolve}\n"
        )
        return info

    def check_mob_status(self) -> None:
        if self.hp <= 0:
            self.is_alive = False