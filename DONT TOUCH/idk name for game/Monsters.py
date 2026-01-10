from Player import Player
import random
from typing import Any

class Monster(Player):
    def __init__(self, difficulty: str, Type: str, Boss: bool = False, Evolve: bool = False) -> None:
        super().__init__(name="Monster")
        self.difficulty: str = difficulty
        self.Evolve = Evolve
        self.mob_type = Type
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
        if Boss:
            self.level *= 2
            self.hp *= 3
            self.dmg *= 2
        if self.Evolve:
            self.hp *= 1.5
            self.dmg *= 1.5

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

    def attack_player(self, player: Player) -> float:
        damage_dealt = self.dmg * (1 + random.uniform(-0.1, 0.1))
        player.hp -= damage_dealt
        return damage_dealt

    def monster_info(self) -> str:
        info: str = (
            f"Monster Level: {self.level}\n"
            f"Monster HP: {self.hp}\n"
            f"Monster DMG: {self.dmg}\n"
        )
        return info

    def check_mob_status(self) -> None:
        raise NotImplementedError("NUh uh")

    def brownian_motion(self, mob_list:list[Any], world:Any):
        half = world.chunk_size - 1
        mon_types = {"Weak": "ᵟ", "Strong": "Ω"}

        for mob in mob_list:
            x, y = mob["pos"]
            ox, oy = x, y

            dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
            x = max(0, min(half, x + dx))
            y = max(0, min(half, y + dy))

            if world.chunk[x][y] == "0":
                world.chunk[ox][oy] = "0"
                world.chunk[x][y] = mon_types[mob["type"]]
                mob["pos"] = (x, y)

