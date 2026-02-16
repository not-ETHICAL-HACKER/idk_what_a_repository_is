from world_gen import gen
from time import sleep
from mob_ai import Mob, Mob_AI
from shutil import get_terminal_size
col,row = get_terminal_size()
mob_d_list: list[dict[str, str | tuple[int, int]]] = []
mob_list: list[tuple[Mob, tuple[int, int]]] = []
world = gen("debug", (row//2-1, col//2-1), 0.05, "easy")
world.generate(mob_list)
for mob_iter in mob_list:
    mob_d_list.append({"type": mob_iter[0].mob_type, "pos": mob_iter[1]})
mob_ai = Mob_AI(world)


def clear():
    print("\033[H", end="")

c=0
while True:
    c+=1
    clear()
    print(c)
    mob_ai.brownian_motion(mob_d_list)
    world.render()
    sleep(1)