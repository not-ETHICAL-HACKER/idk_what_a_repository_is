import winsound as w,time,sys
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
def conveyor_belt_animation(frames, fps=10, sound=False):
    text = ''.join(frames)#try to add color next time
    delay = 1 / fps
    while True:
        sys.stdout.write("\r" + text)
        sys.stdout.flush()
        if sound:
            w.Beep(600, 50)
        time.sleep(delay)
        text = text[1:] + text[0]  # rotate left
import sys, time, math, os

def wave_animate(frames, fps=2, amplitude=3, wavelength=6, speed=1):
    text = ''.join(frames)
    delay = 1 / fps
    t = 0  # time offset for animation

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear screen for each frame
        
        height = amplitude * 2 + 1  # total height of wave (top to bottom)
        lines = [" " * len(text) for _ in range(height)]  # prepare empty canvas
        
        # create wave pattern
        frame_chars = list(text)
        for i, ch in enumerate(frame_chars):
            y = int(amplitude * math.sin((i / wavelength) + t))  # wave displacement
            row = amplitude - y  # invert so wave goes up/down correctly
            
            # replace the right char in the right row
            line = list(lines[row])
            line[i] = ch
            lines[row] = ''.join(line)
        
        # print all lines stacked vertically
        print("\n".join(lines))
        sys.stdout.flush()
        time.sleep(delay)
        t += 0.3 * speed  # wave moves smoothly forward
        
        # horizontal scroll
        text = text[1:] + text[0]
import winsound as w
import sys as s
import time
from random import shuffle, randint

def animate_byai(frames: list, fps: float = 10, sound=True):
    target = ''.join(frames)
    shuffled = frames.copy()
    shuffle(shuffled)  # letters start all scrambled
    delay = 1 / fps

    print("Target:", target)
    print("\nStarting magnetic animation...\n")
    time.sleep(0.1)

    assembled = ["_"] * len(frames)  # empty placeholders

    while assembled != list(target):
        for i in range(len(frames)):
            # if the right letter is nearby, "magnetically" snap it into place
            if assembled[i] != target[i] and shuffled:
                next_letter = shuffled.pop()
                if next_letter == target[i]:
                    assembled[i] = next_letter
                    if sound:
                        w.Beep(800, 50)
                else:
                    shuffled.insert(0, next_letter)

        # print current state
        s.stdout.write("\r" + ''.join(assembled))
        s.stdout.flush()
        time.sleep(delay)

    print("\n\n✨ Magnetic join complete ✨")
    w.Beep(1200, 200)

# run it
letters = list("magnetized")
animate_byai(letters, fps=100)


wave_animate(l)