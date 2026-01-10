import random
from Player import Player
from Monsters import Monster
from World_Gen import Generate_World
from shutil import get_terminal_size
import time
from typing import Any
import re
# import threading
import os
from datetime import datetime

random.seed(1)
row, col = get_terminal_size()
chunk_grid = 11

def Wrapper(func: Any) -> Any:
    def inner(*args: Any, **kwargs: Any) -> Any:
        print("Calling", func.__name__, end=" -> ")
        result = func(*args, **kwargs)
        return result
    return inner


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


def log(*args: str):
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


def clear() -> None:
    print("\033[2J\033[H", end="")

os.system('cls' if os.name == 'nt' else 'clear')
print(" Welcome to the game! ".center(row, "="))
while True:

    Player_id: str = input("Enter your Name : ")

    if not re.match(r"^[A-Za-z0-9_]+$", Player_id):
        print("Invalid input. Please enter a valid name.")
        time.sleep(2)
        clear()
    else:
        break

p_1 = Player(Player_id)

while True:
    Difficulty: str = input(
        "Select Difficulty (Easy/Normal/Hard): ").capitalize()
    if Difficulty not in ["Easy", "Normal", "Hard"]:
        print("Invalid input. Please enter Easy, Normal, or Hard.")
        time.sleep(2)
        clear()
    else:
        break
p_1.diff_equalizer(Difficulty)

Seed_input: str = input("Enter a seed (numbers or words): ")
if Seed_input == "":
    wrld = Generate_World(random.randint(1, 10**6))
else:
    wrld = Generate_World(
        int(Seed_input) if Seed_input.isdigit() else Seed_input)

local_biome = wrld.generate_location()
print(f"You have spawned in a {local_biome} biome.")

x, y, z = wrld.spawn_chunk(chunk_grid**2)
dir_moved: list[str] = []
log(f"Player '{p_1.name}' spawned at coordinates (x: {x}, y: {y}, z: {z}) in a {local_biome} biome on {Difficulty} difficulty with seed '{Seed_input}'.")
wrld.gen_terrain(local_biome, Difficulty)
wrld.gen_mobs(Difficulty)
wrld.display_chunk((x, y, z))
for i in range(10):
    clear()
    wrld.display_chunk((x, y, z))
    print("Directions:\n==>>North,South,East,West")
    a = input("Enter which direction to move: ")
    if not a:
        continue
    dir_moved.append(a[0].upper())
    if a[0].lower() == "e":
        y -= 1
    elif a[0].lower() == "w":
        y += 1
    elif a[0].lower() == "n":
        x -= 1
    elif a[0].lower() == "s":
        x += 1
    else:
        print("Invalid")
        continue
    # for mob in Monster: commented out bcs i need the idea
    #     if mob.pos == (x, y):
    #         dmg = mob.monster.attack_player(p_1)
    #         print(f"A monster attacked you for {dmg:.1f} damage!")

log(f"Player '{p_1.name}' moved {', '.join(dir_moved)} to coordinates (x: {x}, y: {y}, z: {z}).")