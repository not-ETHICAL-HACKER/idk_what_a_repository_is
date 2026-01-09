import game
from Player import Player
import random


class Monster(Player):
    def __init__(self, difficulty: str, Boss: bool = False, Evolve: bool = False) -> None:
        super().__init__(name="Monster")
        self.difficulty: str = difficulty
        self.Evolve = Evolve
        self.mob_pos_list: list[dict[str | int, tuple[int, int] | str]] = []
        if self.difficulty == "Easy":
            self.level = random.randint(1, 5)
            self.hp = random.randint(20, 50)
            self.dmg = random.randint(5, 15)
        elif self.difficulty == "Normal":
            self.level = random.randint(5, 15)
            self.hp = random.randint(50, 100)
            self.dmg = random.randint(15, 30)
        elif self.difficulty == "Hard":
            self.level = random.randint(15, 30)
            self.hp = random.randint(100, 200)
            self.dmg = random.randint(30, 50)
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
    def check_mob_status(self)->None:
        raise NotImplementedError("NUh uh")
    def brownian_motion(self, mob_list: list[dict[str, tuple[int, int] | str]]) -> None:
        dir = list("NSEWUD")
        half = game.wrld.chunk_size // 2
        for m in range(len(mob_list)):
            x, y = mob_list[m].get("pos", (0, 0))
            for _ in range(5):
                a = random.choice(dir)
                if a == 'N':
                    y += 1
                elif a == 'S':
                    y -= 1
                elif a == 'E':
                    x += 1
                elif a == 'W':
                    x -= 1
                x = max(-half, min(half - 1, x))
                y = max(-half, min(half - 1, y))
            mob_list[m]["pos"] = x, y
        return

    def check_mob_pos(self) -> None:
        for i, c in enumerate(game.wrld.display_chunk(game.wrld.player_pos)):
            for j, char in enumerate(c):
                if "ᵟ" in char:
                    # Append a dictionary or tuple representing this specific mob
                    self.mob_pos_list.append({"type": "Weak", "pos": (i, j)})

                elif "Ω" in char:
                    self.mob_pos_list.append({"type": "Strong", "pos": (i, j)})
