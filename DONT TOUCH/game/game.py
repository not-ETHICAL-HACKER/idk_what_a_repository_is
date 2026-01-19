import random
from Player import Player
from Monsters import Monster
from Monsters import Mob
from World_Gen import Generate_World
from Combat import Combat
from shutil import get_terminal_size
import time
import csv
import pandas as pd
from typing import Any
import re
# import threading
import os
from datetime import datetime

col, row = get_terminal_size()


def loading_screen():
    words = ["Loading", "Installing", "Deleting", "Optimizing", "Rewriting", "Patching", "Overclocking", "Rebalancing", "Hotfixing", "Summoning", "Sacrificing", "Gaslighting", "Threatening", "Negotiating with", "Spawning", "Syncing", "Binding", "Registering", "Resolving"
             ]
    prefixes = [
        "Pre-", "Post-", "Re-", "Auto-", "Hyper-",
        "Quantum ", "Pseudo-", "Meta-", "Deferred ",
        "Experimental "
    ]
    mods = ["Player", "Monster", "Mob", "Generate_World", "Life", "Reality", "Timeline", "Balance",
            "Entropy", "Luck", "Render Pipeline", "Event Loop", "Tick Rate", "Memory Pool", "State Machine"]
    suffixes = [
        "...", "....", " [OK]", " [FAIL?]", " [RETRYING]",
        " (safe)", " (unstable)", " (do not interrupt)", "[HELP ME]"
    ]
    for _ in range(10, 2, -2):
        status_text = (
            f"{random.choice(prefixes)}"
            f"{random.choice(words)} "
            f"{random.choice(mods)}"
            f"{random.choice(suffixes)}"
        ).center(col)

        max_width = col // _
        for i in range(max_width + 1):
            bar = "#" * i + " " * (max_width - i)
            display = f"{status_text}\n{'|' + bar + '|': ^{col}}"
            print(display, end="\r")

            time.sleep(1/(len(status_text))*2)
            print("\033[A", end="")

        clear()


def Wrapper(func: Any) -> Any:
    def inner(*args: Any, **kwargs: Any) -> Any:
        print("Calling", func.__name__, end=" -> ")
        result = func(*args, **kwargs)
        return result
    return inner


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

with open("DONT TOUCH/game/log/game.log", "w", encoding="utf-8") as f:
    f.write(f"{("Game Log Started".center(col//2, "="))}\n")


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


with open('DONT TOUCH/game/log/mob.csv', "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Timestamp", "ID", "HP", "DMG", "Lvl", "Evolve", "Boss", "is_alive"
    ])


def log_mobs(ID: str, Type: str, HP: int, DMG: int, Lvl: int, Evolve: bool, Boss: bool, is_alive: bool):
    """
    The function `log_mobs` writes mob data to a CSV file including timestamp, ID, type, HP, damage,
    level, evolution status, boss status, and alive status.
    
    :param ID: The ID parameter is a string that represents the unique identifier of the mob
    :type ID: str
    :param Type: The `Type` parameter in the `log_mobs` function represents the type or category of the
    mob being logged. It could be something like "Goblin", "Dragon", "Skeleton", etc., depending on the
    type of creatures in your game
    :type Type: str
    :param HP: HP stands for "Hit Points" and represents the amount of health or life points a mob has
    in a game. It indicates how much damage a mob can sustain before being defeated
    :type HP: int
    :param DMG: DMG stands for damage and it is an integer value representing the amount of damage that
    a mob can inflict on a player or another entity in the game
    :type DMG: int
    :param Lvl: The "Lvl" parameter in the function represents the level of the mob. It is an integer
    value indicating the level of the mob in the game
    :type Lvl: int
    :param Evolve: Evolve is a boolean parameter that indicates whether the mob has the ability to
    evolve or not. If the mob can evolve, the value of this parameter would be True; otherwise, it would
    be False
    :type Evolve: bool
    :param Boss: The `Boss` parameter in the `log_mobs` function is a boolean value that indicates
    whether the mob is a boss or not. If the mob is a boss, the value of this parameter would be `True`,
    otherwise it would be `False`
    :type Boss: bool
    :param is_alive: The `is_alive` parameter in the `log_mobs` function is a boolean value that
    indicates whether the mob is currently alive or not. It is used to track the status of the mob in
    the game
    :type is_alive: bool
    """

    with open("DONT TOUCH/game/log/mob.csv", mode='a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([timestamp, ID, Type, HP,
                        DMG, Lvl, Evolve, Boss, is_alive])


def clear() -> None:
    print("\033[2J\033[H", end="")


os.system('cls' if os.name == 'nt' else 'clear')

loading_screen()

print(" Welcome to the game! ".center(col, "="))
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

m_1 = Monster()

# ? made into chunk_size**2 bcs the world is a square
x, y, z = wrld.spawn_chunk(wrld.chunk_size**2)
dir_moved: list[str] = []  # ? list of directions moved by player
log(f"Player '{p_1.name}' spawned at coordinates (x: {x}, y: {y}, z: {z}) in a {local_biome} biome on {Difficulty} difficulty with seed '{Seed_input}'.")
wrld.gen_terrain(local_biome, Difficulty)
wrld.display_chunk((x, y, z))  # ?displays chunk
wrld.gen_mobs(Difficulty, m_1.mob_pos_list)
mob_list: list[tuple[Mob, tuple[int, int]]] = []
mon_types: dict[str, str] = {"Weak": "ᵟ", "Strong": "Ω"}
char_list: list[str] = []
for i, mob in enumerate(m_1.mob_pos_list):
    b_c = random.random() > 0.8
    e_c = random.random() > 0.5
    mob_list.append((
        Mob(diff=Difficulty,  # Difficulty of main loop
            mob_id=m_1.mob_pos_list[i]["ID"],  # Mob ID
            Type=mon_types[mob["type"]],  # Mob tiers
            Boss=b_c,  # Boss chance
            Evolve=e_c,  # Evolve chance
            Is_Alive=True
            ), m_1.mob_pos_list[i]["pos"]))  # todo implement life counter
    log_mobs(
        m_1.mob_pos_list[i]["ID"],  # Mob ID
        Type=mon_types[mob["type"]],  # Mob tiers
        HP=int(mob_list[i][0].hp),
        DMG=int(mob_list[i][0].dmg),
        Lvl=int(mob_list[i][0].level),
        Boss=b_c,  # Boss chance
        Evolve=e_c,  # Evolve chance
        is_alive=True
    )
while not p_1.is_dead():
    for i in range(m_1.seconds):
        clear()  # ? clears screen

        # ? simulates movement of mobs
        m_1.brownian_motion(m_1.mob_pos_list, wrld)
        for i in range(len(mob_list)):
            # ? changes old mob coords to updated coords
            mob_list[i] = (mob_list[i][0], m_1.mob_pos_list[i]["pos"])
        wrld.display_chunk((x, y, z))
        print("What would you like to do now?")
        print("1.Move\n2.Check Status\n3.Scout Mobs")
        choice = input("> ")
        if choice.lower() == "move" or choice == "1":
            print("[W]".center(col//4))
            print("[A][S][D]".center(col//4))
            a = input("Enter a key from wasd to move: ")
            if not a:
                continue
            dir_moved.append(a[0].upper())
            if a[0].lower() == "a":
                y -= 1
            elif a[0].lower() == "d":
                y += 1
            elif a[0].lower() == "w":
                x -= 1
            elif a[0].lower() == "s":
                x += 1
            else:
                print("Invalid")
            # Create a tuple of current player position
            player_pos = ((x+wrld.chunk_size//2) % wrld.chunk_size,
                          (y+wrld.chunk_size//2) % wrld.chunk_size)

            # Find the mob that is actually at the player's position
            # We loop through our object list to find the match
            for mob, coords in mob_list:
                # Assuming your Mob class has a .pos attribute updated by brownian_motion
                if coords == player_pos:
                    print(
                        f"!!! ENCOUNTERED {mob.mob_id} ({mob.mob_type}) !!!".center(col))
                    print(Combat(p_1, mob, coords, wrld).engage())
        elif choice.lower() in ("status", "check", "check status") or choice == "2":
            print(p_1.status_screen())
        elif choice.lower() in ("scout", "scout mobs") or choice == "3":
            # --- Inside your Choice 3 logic ---
            try:
                # Load and clean headers immediately
                df = pd.read_csv(
                    'DONT TOUCH/game/log/mob.csv', encoding='utf-8')
                df.columns = df.columns.str.strip()

                # We use numeric_only=True to prevent it from trying to average symbols/IDs
                summary = df.groupby('Mob_Type')[
                    ['HP', 'DMG']].mean(numeric_only=True)

                print("\n" + (" SCOUT REPORT ".center(col//2, "=")).center(col, " "))
                if summary.empty:
                    print("No mob data found in the area.")
                else:
                    # round to 1 decimal for cleanliness
                    print(summary.round(1))
                print(("=".center(col//2, "=")).center(col))

            except FileNotFoundError:
                print("Error: No mob log file found. Try spawning mobs first.")
            except Exception as e:
                print(f"Scout failed: {e}")
        with open('DONT TOUCH/game/log/mob.csv', "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Timestamp", "ID", "Type", "HP", "DMG", "Lvl", "Evolve", "Boss", "is_alive"
            ])
        for v, mob in enumerate(m_1.mob_pos_list):
            b_c = random.random() > 0.8
            e_c = random.random() > 0.5
            log_mobs(
                m_1.mob_pos_list[v]["ID"],  # Mob ID
                Type=mon_types[mob["type"]],  # Mob tiers
                HP=int(mob_list[v][0].hp),
                DMG=int(mob_list[v][0].dmg),
                Lvl=int(mob_list[v][0].level),
                Boss=b_c,  # Boss chance
                Evolve=e_c,  # Evolve chance
                is_alive= int(mob_list[v][0].hp) >= 0
            )
        waiting_for_input = input(">")
log(f"Player '{p_1.name}' moved {', '.join(dir_moved)} to coordinates (x: {x}, y: {y}, z: {z}).")
