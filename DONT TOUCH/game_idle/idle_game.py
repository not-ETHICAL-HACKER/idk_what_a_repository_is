from world_gen import gen
from shutil import get_terminal_size
row,col = get_terminal_size()
world = gen("debug", (row-1, col-1), 0.05)
world.generate()