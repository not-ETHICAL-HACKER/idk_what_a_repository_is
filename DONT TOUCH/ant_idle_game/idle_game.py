import os
import statistics
from world_gen import gen
import time
from mob_ai import Mob, Mob_AI
from shutil import get_terminal_size
col, row = get_terminal_size()
mob_list: list[Mob] = []
world = gen("debug", (int(row-2)//2, int(col)//2), 0.05, "easy")
world.generate(mob_list)
mob_ai = Mob_AI(world)

#! modules name should be ecosim if its released


def clear():
    print("\033[H", end="")


def stats(group: list[Mob]) -> str:
    if not group:
        return "extinct"
    avg_e:float = sum(m.energy for m in group) / len(group)
    med_age:float = statistics.median(m.age for m in group)
    return f"{f'n : {len(group)} average energy : {avg_e:.1f} median age : {med_age:.0f}'.center(45)}"

# // ! remove mobs if energy < 0
# todo fix the water rendering issue use the check area func to make dynamic water bodies that can be surrounded by land and have mobs interact 
# todo with them, like drinking from them to regain energy or drowning if they stay in them for too long
# todo implement the states (heat, hunger, disease, etc) and have them influence mob behavior and interactions, like reproduction, aggression, movement patterns, etc
#// todo change the list of dicts to a list of Mob objects for better code organization and readability, and update the Mob_AI class accordingly
# todo: make a better render function that only updates the changed cells instead of redrawing the whole world every time,
#// todo maybe add some color to the mobs and terrain to make it more visually appealing
# todo implement a more complex AI for the mobs that allows them to have different behaviors based on their type and surroundings
# todo add a way for the player to interact with the world and influence the mob population,
# todo maybe by introducing a new mob type that can be controlled by the player or by allowing the player to place traps or food to attract or repel certain mobs.
# // todo add a way to track the population of each mob type and display it to the player, maybe through a simple UI or by printing it to the console every few seconds.
# // todo implement age and an energy system for the mobs, where they need to eat to survive and can die of old age or starvation
# todo add diff states for mobs throughout their age, like baby, adult, and elder, with different behaviors and abilities for each stage
# todo add another prey and an apex predator
# todo implement more mob fights


c = 0

s_flag: bool = False
w_flag: bool = False
print("\033[?25l", end="") #! tohide cursor
while True:
    if c%250 == 0:
        os.system("cls" if os.name == "nt" else "clear") #! to remove artifacts from the render, should be replaced with a better render function that only updates the changed cells instead of redrawing the whole world every time
    c += 1
    clear()
    mob_ai.brownian_motion(mob_list)
    mob_ai.dead_mobs(mob_list)
    weak = [m for m in mob_list if m.mob_type == "Weak"]
    strong = [m for m in mob_list if m.mob_type == "Strong"]
    w: str = stats(weak)
    s: str = stats(strong)
    if w == "extinct" and s == "extinct":
        print("All mobs have gone extinct. Simulation ended.")
        break
    elif w == "extinct" and not w_flag:
        os.system("cls" if os.name == "nt" else "clear") #! to remove artifacts from the render, should be replaced with a better render function that only updates the changed cells instead of redrawing the whole world every time
        w_flag = True
        print("Weak mobs have gone extinct.")
        time.sleep(2)
    elif s == "extinct" and not s_flag:
        os.system("cls" if os.name == "nt" else "clear") #! to remove artifacts from the render, should be replaced with a better render function that only updates the changed cells instead of redrawing the whole world every time
        s_flag = True
        print("Strong mobs have gone extinct.")
        time.sleep(2)
    else:
        print(f"{c} days | ᵟ : {w}  | Ω : {s}")
    world.grow_up(mob_list)
    world.render()
    time.sleep(1/600)
