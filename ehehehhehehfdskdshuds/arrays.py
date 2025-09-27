l=[
    [1,2,3,4,5],
    [5,4,3,2,1],
    [1,4,9,16,25]
]
inj=" "
import random
import time
import colorama,pyautogui
from termcolor import colored
l=random.choice(l[1])
print(pyautogui.size())
colorama.init(autoreset=True)
print(Fore.RED + "hello")
l=str(l)
print(l)
colr=["red","blue","black","white","green","yellow","grey","cyan","magenta"]
bg_colr=["on_red","on_blue","on_black","on_white","on_green","on_yellow","on_grey","on_cyan","on_magenta"]
def color(x:str):
    a=len(x)
    for i in range(a):
        col=random.choice(colr)
        bg=random.choice(bg_colr)
        print(colored(x[i],col,bg),end="")
    print()
    return x
color(input("enter string:"))
time.sleep(10)