import winsound,time
from random import randint
while True:
    break
    r=randint(100,500)
    frequency = randint(1000, 2000)
    duration = randint(500, 1000)
    print(frequency,duration,r)
    winsound.Beep(frequency, duration)
    time.sleep(r)
import winsound as w
l=list("abcdefghijklmnopqrstuvwxyz")
import sys as s
import time
def animate(frames:list,fps:float=10000,Title:bool=False):
    a=0
    new=False
    if not Title:
        while True:
            if new:
                print()
                new=False
                w.Beep(500,100)
            for i in range(len(frames)):
                s.stdout.write((" "*(i-a))+(frames[i-a])+("\r"))
                s.stdout.flush()
                time.sleep(1/fps)
            a+=1
            if a==len(frames):
                a=0
                new=True
    else:
        while True:
            for i in range(len(frames)):
                a=len(frames)-1
                #for alternate animation ie,|\-/
import sys, time, winsound as w

def animate1(frames, fps=10, sound=False):
    text = ''.join(frames)
    delay = 1 / fps
    while True:
        sys.stdout.write("\r" + text)
        sys.stdout.flush()
        if sound:
            w.Beep(600, 50)
        time.sleep(delay)
        text = text[1:] + text[0]  # rotate left

animate1(l)