import winsound as w,time,sys,threading
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
def print_vs_write():
    import sys
    import time
    import matplotlib.pyplot as plt

    # Sizes of input
    sizes = [10**3, 10**4, 10**5, 10**6,10**7,10**8,10**9]
    print_times = []
    stdout_times = []

    for n in sizes:
        # Measure print()
        start = time.time()
        for i in range(n):
            pass  # comment out printing to avoid freezing terminal
            # print(i, end='')
        print_times.append(time.time() - start)
        
        # Measure sys.stdout.write()
        start = time.time()
        for i in range(n):
            pass
            # sys.stdout.write(str(i))
        stdout_times.append(time.time() - start)
    # Plot
    plt.plot(sizes, print_times, marker='o', label='print()')
    plt.plot(sizes, stdout_times, marker='o', label='sys.stdout.write()')
    plt.xlabel("Number of Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("Performance: print() vs sys.stdout.write()")
    plt.legend()
    plt.grid(True)
    plt.show()
def anime(frames:list,fps:float=100):
    """
    The function `anime` displays a sequence of frames at a specified frames per second (fps) rate.
    
    :param frames: The `frames` parameter is a list of strings representing individual frames of an
    animation. Each string in the list corresponds to a frame that will be displayed in sequence to
    create the animation
    :type frames: list
    :param fps: The `fps` parameter in the `anime` function stands for frames per second, which
    determines the speed at which the frames from the `frames` list are displayed. The default value for
    `fps` is set to 100 frames per second, defaults to 100
    :type fps: float (optional)
    """
    #?
    #!
    #*
    fps=1/fps
    while True:
        for frame in frames:
            sys.stdout.write(frame+"\r")
            sys.stdout.flush()
            time.sleep(fps)
frames=list("abcdefghijklmnopqrstuvwxyz")
t = threading.Thread(target=anime,args=(frames,10))
t.daemon = True
t.start()
for i in range(20):
    break
    print(i)
    time.sleep(0.5)
    import sys
import time
import threading
j=1
print(j)
print(j)
def anime1(frames: list, fps: float = 10):
    delay = 1 / fps
    while True:
        for frame in frames:
            # Move cursor to top-left  
            sys.stdout.write(frame + "\r")  # animation line
            sys.stdout.flush()
            time.sleep(delay)

frames = list("abcdefghijklmnopqrstuvwxyz")
t = threading.Thread(target=anime1, args=(frames, 10))
t.daemon = True
t.start()

# Main program prints below the animation
for i in range(20):
    sys.stdout.write(f"Counting: {i}\n")
    sys.stdout.flush()
    time.sleep(0.5)
    print(help)