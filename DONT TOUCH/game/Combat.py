from typing import Any
import time
import os
import random
from Player import Player
from Monsters import Mob
from datetime import datetime
LOG_COUNTER_FILE = "DONT TOUCH/game/log/log_counter.txt"
# Read counter once at startup
if os.path.exists(LOG_COUNTER_FILE):
    try:
        with open(LOG_COUNTER_FILE, "r") as f:
            log_counter = int(f.read())
    except ValueError:
        log_counter = 0
else:
    log_counter = 0


def log(*args: Any):
    global log_counter
    log_counter += 1

    msg = " ".join(map(str, args))
    stamp = datetime.now().strftime("%d/%m/%Y,%H:%M:%S")
    line = f"[{stamp}] [Log {log_counter}] {msg}"
    with open("DONT TOUCH/game/log/game.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")

    # Save counter to file every time (safe and persistent)
    with open(LOG_COUNTER_FILE, "w") as f:
        f.write(str(log_counter))


# The `Combat` class simulates a combat scenario between a player and a monster, including attacks,
# skills, and last stand mechanics.
class Combat:
    """
    Docstring for Combat

    Attributes:
    - player (Player): The player involved in the combat.
    - monster (Mob): The monster involved in the combat.
    - coords (tuple[int, int]): The coordinates of the combat location.
    - world (Any): The game world where the combat takes place.
    Methods:
    - engage() -> str: Simulates the combat until one party is defeated.
    - player_flee_chance() -> bool: Calculates the chance of the player fleeing.
    - monster_flee_chance() -> bool: Calculates the chance of the monster fleeing.
    - skill(skill_name: str) -> str: Executes a skill used by the player.
    - last_stand_player() -> str: Executes the player's last stand ability.
    - last_stand_monster() -> str: Executes the monster's last stand ability.
    """
    def __init__(self, player: Player, monster: Mob, coords: tuple[int, int], world: Any) -> None:
        self.player = player
        self.world = world
        self.coords = coords
        self.monster = monster
        self.last_stand_monster_count = 0
        self.last_stand_player_count = 0

    def engage(self) -> str:
        log("Combat started between", self.player.name,
            "and", self.monster.mob_type)
        while self.player.hp > 0 and self.monster.hp > 0:
            # Simulate time between attacks
            time.sleep(1-self.player.attack_speed)
            if random.random() >= 0.5:

                self.monster.hp -= self.player.dmg
                print(
                    f"{self.player.name} attacks {self.monster.mob_id} for {self.player.dmg} damage!")
                log(self.player.name, "attacked", self.monster.mob_id,
                    "for", self.player.dmg, "damage.")

            else:

                self.player.hp -= self.monster.dmg
                print(
                    f"{self.monster.mob_id} attacks {self.player.name} for {self.monster.dmg} damage!")
                log(self.monster.mob_id, "attacked", self.player.name,
                    "for", self.monster.dmg, "damage.")

            if (self.player.hp <= 5 or self.monster.hp <= 10) and random.random() < 0.5:

                if self.player.hp <= 5:

                    print(self.player.name, "is attempting Last Stand!")
                    self.last_stand_player()

                if self.monster.hp <= 10:
                    self.last_stand_monster()

            if self.monster.hp <= 0:
                a, b = self.coords
                self.world.chunk[a][b] = "DW" if self.monster.mob_type == "Weak" else "DS"
                log(self.monster.mob_type, "defeated by", self.player.name)
                return f"{self.player.name} has defeated the {self.monster.mob_type}!"

            if self.player.hp <= 0:
                log(self.player.name, "was defeated by",
                    self.monster.mob_type+self.monster.mob_id)
                return f"{self.player.name} has been defeated by the {self.monster.mob_type+self.monster.mob_id}!"

            elif self.monster.hp <= 0:
                log(self.monster.mob_type+self.monster.mob_id,
                    "was defeated by", self.player.name)

                return f"{self.monster.mob_type+self.monster.mob_id} has been defeated by the {self.player.name}!"

            self.monster.check_mob_status()

        return "Combat ended."

    def player_flee_chance(self) -> bool:

        flee_probability = (self.monster.level / self.player.level) * 0.5
        return random.random() <= flee_probability

    def monster_flee_chance(self) -> bool:

        flee_probability = (self.monster.level/self.player.level) * 0.5
        return random.random() <= flee_probability

    def skill(self, skill_name: str) -> str:

        log(self.player.name, "used skill",
            skill_name, "on", self.monster.mob_type)

        if skill_name == "Power Strike":

            damage = self.player.dmg*1.5
            self.monster.hp -= damage
            log(self.player.name, "dealt", damage, "damage to",
                self.monster.mob_type, "using Power Strike")
            return f"{self.player.name} used Power Strike and dealt {damage} damage!"

        elif skill_name == "Heal":

            heal_amount = self.player.level*5
            self.player.hp += heal_amount
            log(self.player.name, "healed for", heal_amount, "HP using Heal")
            return f"{self.player.name} used Heal and restored {heal_amount} HP!"

        else:

            log(self.player.name, "tried to use unknown skill", skill_name)
            return f"Unknown skill: {skill_name}"

    def last_stand_player(self) -> str:

        log(self.player.name, "is attempting Last Stand!")

        if self.player.hp <= (5):

            self.player.hp += self.player.level*10
            log(self.player.name, "successfully used Last Stand and restored HP!")
            print(self.player.name, "used Last Stand and restored HP!")

            if random.random() > min(0.8 + (0.01 * (2 ** (self.last_stand_player_count - 1))),0.95):

                self.player.hp = max(self.player.hp - 10, 1)
                self.last_stand_player_count += 1
                log(self.player.name, f"Last Stand exploded and dealt - {10*self.last_stand_player_count} damage to",
                    self.monster.mob_type)
                print(self.player.name, f"Last Stand exploded and dealt - {10*self.last_stand_player_count} damage to",
                      self.monster.mob_type)
                a = self.last_stand_monster_count
            return f"{self.player.name} used Last Stand and restored HP!"

        else:

            print(self.player.name, "failed to use Last Stand; HP too high.")
            log(self.player.name, "failed to use Last Stand; HP too high.")
            return f"Last Stand can only be used when HP is low!"

    def last_stand_monster(self) -> str:

        log(self.monster.mob_type, "is attempting Last Stand!")
        print(self.monster.mob_type, "is attempting Last Stand!")

        if self.monster.hp <= (10):

            self.monster.hp += self.monster.level*10
            log(self.monster.mob_type,
                "successfully used Last Stand and restored HP!")
            print(self.monster.mob_type,
                  "used Last Stand and restored HP!")

            if random.random() > min(0.8 + (0.01 * (2 ** (self.last_stand_monster_count - 1))),0.95):

                self.monster.hp = max(self.monster.hp - 10, 1)
                self.last_stand_monster_count += 1
                log(self.monster.mob_type,
                    f"Last Stand exploded and dealt - {10*self.last_stand_monster_count} damage to", self.player.name)
                print(self.monster.mob_type,
                      f"Last Stand exploded and dealt - {10*self.last_stand_monster_count} damage to", self.player.name)

            return f"{self.monster.mob_type} used Last Stand and restored HP!"

        else:

            log(self.monster.mob_type, "failed to use Last Stand; HP too high.")

            return f"Last Stand can only be used when HP is low!"
