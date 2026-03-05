import os
import statistics
from random import randint
from world_gen import gen
import time
from mob_ai import Mob, Mob_AI
from shutil import get_terminal_size
col, row = get_terminal_size()
mob_d_list: list[dict[str, str | tuple[int, int] | int]] = []
mob_list: list[tuple[Mob, tuple[int, int]]] = []
world = gen("debug", (int(row-2), int(col)), 0.05, "easy")
world.generate(mob_list)
for mob_iter in mob_list:
    mob_d_list.append(
        {"type": mob_iter[0].mob_type, "pos": mob_iter[1], "energy": randint(500, 1000), "age": 0, "state": "alive", "state_counter": 0})
mob_ai = Mob_AI(world)

#! modules name should be ecosim if its released


def clear():
    print("\033[H", end="")


def stats(group: list[dict[str, str | tuple[int, int] | int]]) -> str:
    if not group:
        return "extinct"
    avg_e:float = sum(m["energy"] for m in group) / len(group)
    med_age:float = statistics.median(m["age"] for m in group)
    return f"{f'n : {len(group)} average energy : {avg_e:.1f} median age : {med_age:.0f}'.center(45)}"

# // ! remove mobs if energy < 0
# todo fix the water rendering issue use the check area func to make dynamic water bodies that can be surrounded by land and have mobs interact 
# TODO with them, like drinking from them to regain energy or drowning if they stay in them for too long
# todo implement the states (heat, hunger, disease, etc) and have them influence mob behavior and interactions, like reproduction, aggression, movement patterns, etc
# todo: make a better render function that only updates the changed cells instead of redrawing the whole world every time,
#// todo maybe add some color to the mobs and terrain to make it more visually appealing
# todo implement a more complex AI for the mobs that allows them to have different behaviors based on their type and surroundings
# todo add a way for the player to interact with the world and influence the mob population,
# todo maybe by introducing a new mob type that can be controlled by the player or by allowing the player to place traps or food to attract or repel certain mobs.
# // todo add a way to track the population of each mob type and display it to the player, maybe through a simple UI or by printing it to the console every few seconds.
# // todo implement age and an energy system for the mobs, where they need to eat to survive and can die of old age or starvation
# todo add diff states for mobs throughout their age, like baby, adult, and elder, with different behaviors and abilities for each stage
# todo add another prey and an apex predator


c = 0
while True:
    if c%100 == 0:
        os.system("cls" if os.name == "nt" else "clear") #! to remove artifacts from the render, should be replaced with a better render function that only updates the changed cells instead of redrawing the whole world every time
    c += 1
    clear()
    mob_ai.brownian_motion(mob_d_list, c)
    mob_ai.dead_mobs(mob_d_list)
    weak = [m for m in mob_d_list if m["type"] == "Weak"]
    strong = [m for m in mob_d_list if m["type"] == "Strong"]
    w: str = stats(weak)
    w_flag: bool = False
    s: str = stats(strong)
    s_flag: bool = False
    if w == "extinct" and s == "extinct":
        print("All mobs have gone extinct. Simulation ended.")
        break
    elif w == "extinct" and not w_flag:
        w_flag = True
        print("Weak mobs have gone extinct.")
        time.sleep(2)
    elif s == "extinct" and not s_flag:
        s_flag = True
        print("Strong mobs have gone extinct.")
        time.sleep(2)
    else:
        print(f"{c} days | ᵟ : {w}  | Ω : {s}")
    world.render()
    time.sleep(1/6000)
