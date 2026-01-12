from typing import Any
from Player import Player
from Monsters import Mob
import os
from datetime import datetime
LOG_COUNTER_FILE = "DONT TOUCH/log/log_counter.txt"

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
    with open("DONT TOUCH/log/game.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")

    # Save counter to file every time (safe and persistent)
    with open(LOG_COUNTER_FILE, "w") as f:
        f.write(str(log_counter))

class Combat:
    def __init__(self,player:Player,monster:Mob) -> None:
        self.player=player
        self.monster=monster
    def engage(self) -> str:
        log("Combat started between", self.player.name, "and", self.monster.mob_type)
        while self.player.hp > 0 and self.monster.hp > 0:
            self.monster.hp -= self.player.dmg
            log(self.player.name, "attacked", self.monster.mob_type, "for", self.player.dmg, "damage.")
            if self.monster.hp <= 0:
                log(self.monster.mob_type, "defeated by", self.player.name)
                return f"{self.player.name} has defeated the {self.monster.mob_type}!"
            self.player.hp -= self.monster.dmg
            log(self.monster.mob_type, "attacked", self.player.name, "for", self.monster.dmg, "damage.")
            if self.player.hp <= 0:
                log(self.player.name, "was defeated by", self.monster.mob_type)
                return f"{self.player.name} has been defeated by the {self.monster.mob_type}!"
        return "Combat ended."