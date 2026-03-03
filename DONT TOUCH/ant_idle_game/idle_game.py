import statistics
from random import randint
from world_gen import gen
from time import sleep
from mob_ai import Mob, Mob_AI
from shutil import get_terminal_size
col, row = get_terminal_size()
mob_d_list: list[dict[str, str | tuple[int, int] | int]] = []
mob_list: list[tuple[Mob, tuple[int, int]]] = []
world = gen("debug", (int(row//1-1), int(col/1-1)), 0.05, "easy")
world.generate(mob_list)
for mob_iter in mob_list:
    mob_d_list.append(
        {"type": mob_iter[0].mob_type, "pos": mob_iter[1], "energy": randint(50, 100), "age": 0})
mob_ai = Mob_AI(world)

#! modules name should be ecosim if its released


def clear():

    print("\033[2J\033[H", end="")

def stats(group):
    if not group:
        return "extinct"
    avg_e = sum(m["energy"] for m in group) / len(group)
    med_age = statistics.median(m["age"] for m in group)
    return f"n={len(group)} e={avg_e:.1f} age={med_age:.0f}"

#! remove mobs if energy < 0
# todo: make a better render function that only updates the changed cells instead of redrawing the whole world every time,
# todo maybe add some color to the mobs and terrain to make it more visually appealing
# todo implement a more complex AI for the mobs that allows them to have different behaviors based on their type and surroundings
# todo add a way for the player to interact with the world and influence the mob population,
# todo maybe by introducing a new mob type that can be controlled by the player or by allowing the player to place traps or food to attract or repel certain mobs.
# todo add a way to track the population of each mob type and display it to the player, maybe through a simple UI or by printing it to the console every few seconds.
# // todo implement age and an energy system for the mobs, where they need to eat to survive and can die of old age or starvation
# todo add diff states for mobs throughout their age, like baby, adult, and elder, with different behaviors and abilities for each stage
# todo add another prey and an apex predator


c = 0
while True:
    c += 1
    clear()
    mob_ai.brownian_motion(mob_d_list, c)
    mob_ai.dead_mobs(mob_d_list)
    weak = [m for m in mob_d_list if m["type"] == "Weak"]
    strong = [m for m in mob_d_list if m["type"] == "Strong"]
    print(f"{c} days | ᵟ {stats(weak)}  | Ω {stats(strong)}")
    world.render()
    sleep(1/120)
