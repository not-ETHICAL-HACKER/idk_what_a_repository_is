import pyautogui
import time
import random
pyautogui.moveTo(1250,25,duration=0)
pyautogui.leftClick()
a=0
boost=0
n=0
pyautogui.moveTo(777,370,duration=1)
pyautogui.click()
pyautogui.write("slither.io",interval=0.1)
pyautogui.keyDown("enter")
pyautogui.keyUp("enter")
pyautogui.moveTo(690,455,duration=1)
time.sleep(6)
pyautogui.write("this is a bot",interval=0.05)
time.sleep(3)
pyautogui.moveTo(777+a,170+a,duration=0.1)
time.sleep(1)
pyautogui.moveTo(65,646,duration=0.1)#65,646 is skin coords
pyautogui.doubleClick()
pyautogui.moveTo(350,411,duration=0.1)#350,411 is arrow coords
for j in range(4):#the numbber in the range is how many times you click
    pyautogui.leftClick()
pyautogui.moveTo(690,546,duration=0.1)
pyautogui.leftClick()
time1=time.perf_counter()
for i in range(60*10):
    pyautogui.keyDown("enter")
    n+=1
    x=random.randint(100,1000)
    y=random.randint(50,650)
    if n<10:
        pyautogui.moveTo(x+a,y+a,duration=0.1)
    if n>10:
        pyautogui.moveTo(x-a,y-a,duration=0.1)
    a+=10
    if a>100:
        a*=-1
    if n>20:
        n=0
    if boost == 10:
        pyautogui.mouseDown(button="left")
    elif boost== 20:
        boost=0
        pyautogui.mouseUp(button="left")
    boost+=1
time2=time.perf_counter()
t_time=time2-time1
print(t_time)
print(pyautogui.position())
pyautogui.moveTo(1350,25,duration=1)
print( pyautogui.pixel(1350,25))
pyautogui.click()
time.sleep(1)
