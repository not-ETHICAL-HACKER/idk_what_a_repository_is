from collections import deque
import numpy as np
from typing import Any
import time
import sys
import os
import random
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


def log(*args: str):
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

class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.is_alive: bool = True
        self.status: str = "Alive"
        self.attack_speed: float = max(random.random(),0.1)  # Attacks per second
        self.level: float = 1
        self.exp:   float = 0
        self.hp:    float = 500
        self.mp:    float = 50
        self.dmg:   float = 25 + round((random.random()*5),2)
        self.dex:   float = 10
        self.luck:  float = 5
        self.inventory: deque[Any] = deque()
        self.exp_multiplier: float = 1.0
        self.exp_gain_rate: str = "Linear"  # n
        self.max_len: int = 0

    def is_dead(self) -> bool:
        k = "Death Token" in self.inventory or not self.is_alive or self.hp<=0
        if not k:
            return False
        else:
            self.is_alive = False
            self.death_screen()
            return True

    def diff_equalizer(self, Difficulty: str) -> None:
        self.difficulty: str = Difficulty
        if hasattr(self, "_difficulty_applied"):
            return
        self._difficulty_applied = True

        if self.difficulty == "Hard":
            self.max_len = 50
            self.hp /= 2
            self.mp /= 2
            self.dmg /= 2
            self.dex /= 2
            self.luck /= np.e
            self.inventory.append("Hard Mode Token")
            self.inventory = deque(self.inventory, maxlen=self.max_len)
            self.exp_multiplier *= 2.0
            self.exp_gain_rate = "Exponential"  # x^n
            #! try to make the difficulty setting more impactful
        elif self.difficulty == "Easy":
            self.max_len = 200
            self.inventory.append("Easy Mode Token")
            self.inventory = deque(self.inventory, maxlen=self.max_len)
        elif self.difficulty == "Normal":
            self.max_len = 100
            self.hp /= 1.5
            self.mp /= 1.5
            self.dmg /= 1.5
            self.dex /= 1.5
            self.luck /= np.e/2
            self.inventory.append("Normal Mode Token")
            self.inventory = deque(self.inventory, maxlen=self.max_len)
            self.exp_multiplier *= 1.5
            self.exp_gain_rate = "Super Linear"  # n*log(n)

    def lvl_up(self) -> int:
        lvl_counter: int = 0
        while self.exp >= self.level * 5:
            self.level += 1
            cost = self.level * 5
            self.exp -= cost
            self.hp += 10
            self.mp += 10
            self.dmg += 10
            self.dex += 10
            lvl_counter += 1
        return lvl_counter

    def status_screen(self) -> str:
        status_info: str = (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"EXP: {self.exp}\n"
            f"HP: {self.hp}\n"
            f"MP: {self.mp}\n"
            f"DMG: {self.dmg}\n"
            f"DEX: {self.dex}\n"
            f"LUCK: {self.luck}\n"
            f"Inventory: {', '.join(map(str, self.inventory)) if self.inventory else 'Empty'}"
        )
        return status_info

    def gain_exp(self, amount: float) -> None:
        if self.exp_gain_rate == "Linear":
            self.exp += amount * self.exp_multiplier
        elif self.exp_gain_rate == "Super Linear":
            self.exp += amount * self.exp_multiplier * (1 + np.log(amount + 1))
        elif self.exp_gain_rate == "Exponential":
            self.exp += amount * self.exp_multiplier * (np.e ** (amount / 10))
        return None

    def add_to_inventory(self, item: str) -> None:
        self.inventory.append(item)
        self.is_dead()
        return None

    def death_screen(self) -> None:
        print("\t\t\tEND SCREEN")
        print("Thank you for playing the game!")
        print(f"Your final stats are:\n{self.status_screen()}")
        log("You died.")
        time.sleep(5)
        sys.exit()

    def heal_up(self):
        raise NotImplementedError("vikfndsk DO sum thin")