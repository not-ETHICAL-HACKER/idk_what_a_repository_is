from world_gen import gen
from time import sleep
from mob_ai import Mob, Mob_AI
from shutil import get_terminal_size
col, row = get_terminal_size()
mob_d_list: list[dict[str, str | tuple[int, int]]] = []
mob_list: list[tuple[Mob, tuple[int, int]]] = []
world = gen("debug", (int(row//1.125-1), int(col/1.125-1)), 0.005, "easy")
world.generate(mob_list)
for mob_iter in mob_list:
    mob_d_list.append({"type": mob_iter[0].mob_type, "pos": mob_iter[1]})
mob_ai = Mob_AI(world)

#! modules name should be ecosim if its released
def clear():
    print("\033[2J\033[H", end="")


c = 0
while c != 1000:
    c += 1
    clear()
    print(c)
    mob_ai.brownian_motion(mob_d_list, c)
    world.render()
    sleep(1/30)
