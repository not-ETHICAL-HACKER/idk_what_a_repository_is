import winsound as w
l=list("abcdefghijklmnopqrstuvwxyz")
import sys as s
import time
def animate(frames:list,fps:float=60,Title:bool=False):
    a=0
    new=False
    if not Title:
        while True:
            if new:
                print()
                new=False
            for i in range(len(frames)):
                s.stdout.write((" "*(i-a))+(frames[i-a])+("\r"))
                s.stdout.flush()
                w.Beep(500,100)
                time.sleep(1/fps)
            a+=1
            if a==len(frames):
                a=0
                new=True
    else:
        while True:
            for i in range(len(frames)):
                a=len(frames)-1
                #for alternate animation ie,|\-/ at the same time at diff animate times ig
frames = ["[=     ]", "[ =    ]", "[  =   ]", "[   =  ]", "[    = ]", "[     =]", "[    = ]", "[   =  ]", "[  =   ]", "[ =    ]"]
animate(frames, fps=5)

animate(l)