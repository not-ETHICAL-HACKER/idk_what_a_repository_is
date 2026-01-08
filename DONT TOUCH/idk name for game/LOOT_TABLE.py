import random
class LOOT_TABLE:
    def __init__(self, Mob_lvl: int, Mob_Tier: str):
        self.Mob_lvl = Mob_lvl
        self.Mob_Tier = Mob_Tier
        self.gold_dropped = random.randint(1, 10)*Mob_lvl
        self.exp_dropped = Mob_lvl*random.randint(1, 5)

    def generate_loot(self) -> list[str]:
        self.loot: list[str] = []
        if self.Mob_Tier == "Weak":
            if random.random() < 0.3:
                self.loot.append("Health Potion")
            if random.random() < 0.1:
                self.loot.append("Common Item")
        elif self.Mob_Tier == "Strong":
            if random.random() < 0.5:
                self.loot.append("Health Potion")
            if random.random() < 0.3:
                self.loot.append("Mana Potion")
            if random.random() < 0.2:
                self.loot.append("Uncommon Item")
        elif self.Mob_Tier == "Boss":
            if random.random() < 0.8:
                self.loot.append("Health Potion")
            if random.random() < 0.7:
                self.loot.append("Mana Potion")
            if random.random() < 0.5:
                self.loot.append("Rare Item")
            if random.random() < 0.2:
                self.loot.append("Epic Item")
            if random.random() < 0.1:
                self.loot.append("Legendary Item")
            if random.random()*100 < self.Mob_lvl:
                self.loot.append("Mythic Item")
        if random.random() < 0.01:
            self.loot.append("Death Token")

        return self.loot

