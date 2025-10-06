import time as t
import random as r
import pyautogui as p
print(p.size())
for a in range(10,768,50):
    for b in range(10,1366,50):
        p.moveTo(b,a)
p.moveTo(420,69)
