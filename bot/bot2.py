import time as t
import random as r
import pyautogui as p
print(p.size())
for i in range(500):
    t.sleep(0.1)
    ra=r.randint(0,500)
    p.moveTo(500+(ra//10),ra)

