from Player import Player
import random
from typing import Any
from datetime import datetime
import csv
import os


def log_mob_position(mob_type: str, x: int, y: int):
    file_exists = os.path.isfile('DONT TOUCH\\log\\mob_logs.csv')

    with open('DONT TOUCH\\log\\mob_logs.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the header only if the file is new
        if not file_exists:
            writer.writerow(['Timestamp', 'Mob_Type', 'X', 'Y'])

        # Write the mob data
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([timestamp, mob_type, x, y])


class Monster(Player):
    def __init__(self, difficulty: str, Type: str, Evolve: bool = False):
        super().__init__(name="Monster")
        self.difficulty: str = difficulty
        self.Evolve = Evolve
        self.mob_type = Type
        self.seconds = 6  # a mob moves every second and im tryin to emulate dnd mechanics
        self.mob_pos_list: list[dict[str, tuple[int, int] | str]] = []

    def evolve(self, Mob_lvl: int, Mob_Tier: str) -> None:
        if not self.Evolve:
            return
        if Mob_Tier == "Weak":
            self.level = (Mob_lvl*1.2)//1
            self.hp = (self.hp*1.3)//1
            self.dmg = (self.dmg*1.3)//1
        elif Mob_Tier == "Strong":
            self.level = (Mob_lvl*1.5)//1
            self.hp = (self.hp*1.5)//1
            self.dmg = (self.dmg*1.5)//1
        elif Mob_Tier == "Boss":
            self.level = (Mob_lvl*2)//1
            self.hp = (self.hp*2)//1
            self.dmg = (self.dmg*2)//1

    def loot_drop(self, player: Player) -> list[str]:
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

    def flee_chance(self, player: Player) -> bool:
        flee_probability = (self.level / player.level) * 0.5
        return random.random() <= flee_probability

    def monster_info(self) -> str:
        info: str = (
            f"Monster Level: {self.level}\n"
            f"Monster HP: {self.hp}\n"
            f"Monster DMG: {self.dmg}\n"
        )
        return info

    def check_mob_status(self) -> None:
        raise NotImplementedError("NUh uh")

    def brownian_motion(self, mob_list: list[Any], world: Any):
        half = world.chunk_size - 1
        mon_types = {"Weak": "ᵟ", "Strong": "Ω"}
        for _ in range(self.seconds):
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
                    log_mob_position(mob["type"], mob["pos"][0], mob["pos"][1])


class Mob:
    def __init__(self, diff: str, mob_id: str, Type: str = "ᵟ", Boss: bool = False, Evolve: bool = False) -> None:
        self.difficulty: str = diff
        self.Evolve = Evolve
        self.mob_type = Type
        self.mob_id = mob_id
        self.Boss = Boss
        self.seconds = 6  # a mob moves every second and im tryin to emulate dnd mechanics
        self.mob_pos_list: list[dict[str | int, tuple[int, int] | str]] = []
        if self.difficulty == "Easy":
            self.level = random.randint(1, 5)+(5 if "ᵟ" not in Type else 0)
            self.hp = random.randint(20, 50)+(10 if "ᵟ" not in Type else 0)
            self.dmg = random.randint(5, 15)+(5 if "ᵟ" not in Type else 0)
        elif self.difficulty == "Normal":
            self.level = random.randint(5, 15)+(10 if "ᵟ" not in Type else 0)
            self.hp = random.randint(50, 100)+(25 if "ᵟ" not in Type else 0)
            self.dmg = random.randint(15, 30)+(10 if "ᵟ" not in Type else 0)
        elif self.difficulty == "Hard":
            self.level = random.randint(15, 30)+(15 if "ᵟ" not in Type else 0)
            self.hp = random.randint(100, 200)+(50 if "ᵟ" not in Type else 0)
            self.dmg = random.randint(30, 50)+(15 if "ᵟ" not in Type else 0)
        if self.Boss:
            self.level *= 2
            self.hp *= 3
            self.dmg *= 2
        if self.Evolve:
            self.hp *= 1.5
            self.dmg *= 1.5

    def __repr__(self) -> str:
        return f"[{self.mob_id}: {self.mob_type}, HP: {int(self.hp)},DMG: {int(self.dmg)}, Lvl: {self.level}, {self.Evolve=}, {self.Boss=}]"

    def attack_player(self, player: Player) -> float:
        damage_dealt = self.dmg * (1 + random.uniform(-0.1, 0.1))
        player.hp -= damage_dealt
        return damage_dealt
