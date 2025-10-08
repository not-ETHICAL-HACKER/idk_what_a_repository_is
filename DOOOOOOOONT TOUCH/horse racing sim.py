from random import randint,random
from time import sleep,perf_counter
import sys

a=0
b=10
d_cnt=0
race=100
pace=0
race_v1=100
race_v2=100
h=""
status=""
scr=0
e1_scr=0
e2_scr=0
horse_1=["1","horse"]
horse_2=['2',"no horse"]
horse_3=['3',"why horse?"]
t=0
head="="*111
print(head)
c=input("What horse do u pick?\n1.horse\n2.no horse\n3.why horse?\n")
if c in horse_1:
    print("You have chosen HORSE")
    h="1"
elif c in horse_2:
    print("You have chosen NO HORSE")
    h="2"
elif c in horse_3:
    print("You have chosen WHY HORSE?")
    h="3"
print(head)
print("The Debut Race Has Started.")
while scr<100:
    rh=random()
    rh=rh*10
    rh=round(rh,0)
    h1=randint(1+rh,20+rh)
    h2=randint(1+rh,21+rh)
    h3=randint(1+rh,19+rh)
    r_t=perf_counter()
    if h=="1":
        print(race,"paces left")#find a way to implement other horses too
        sleep(1)
        inj_cnt=randint(1+scr,1000-scr)                #mabye use import time to count how long it takes or a counter for time s
        scr+=h1
        e1_scr+=h2
        e2_scr+=h3
        race-=h1
        if inj_cnt== 500:
            print("your horse has been injured")
            status="injured"
    elif h=='2':
        print(race,"paces left")
        sleep(1)
        inj_cnt=randint(1+scr,1000-scr)
        if inj_cnt== 500:
            print("your horse has been injured")
            status="injured"
        scr+=h2
        e1_scr+=h1
        e2_scr+=h3
        race=race-h2
    elif h=="3":
        print(race,"paces left")
        sleep(1)
        inj_cnt=randint(1+scr,1000-scr)
        if inj_cnt== 500:
            print("your horse has been injured")
            status="injured"
        scr+=h3
        e1_scr+=h1
        e2_scr+=h2
        race=race-h3
print(head)
if status=='injured':
    print("your horse lost due to its leg injury")
    d_cnt=1
if scr>=100 or e2_scr>=100 or e1_scr>=100:
    t_scr = max(scr,e1_scr,e2_scr)
    print("The highest score is",t_scr)
    if t_scr==scr:
        print("HORSE won the debut match")
        if c in horse_1:
            print("you won")
            d=2
        elif c not in horse_1:
            print("you lost")
    elif t_scr==e1_scr:
        print("NO HORSE won the match")
        if c in horse_2:
            print("you won")
            d=2
        elif c not in horse_2:
            print("you lost")
        d=2
    elif t_scr==e2_scr:
        print("WHY HORSE? won the match")
        if c in horse_3:
            print("you won")
            d=2
        elif c not in horse_3:
            print("you lost")
        d=2#find a way to check if players horse won
r_ft=perf_counter()
t=r_ft-r_t
t=round(t,1)
print(head)
a=input("would you like to join more races?(y/n)\n")
if a=="n":
    print("initiating EUTHANSIA")
    sys.exit()
elif a=="y":
    print("initiating EUTHANSIA")
    sys.exit()
if d_cnt==1:
    print("unfortunately yuor horse cannot enter\ndue to its injury")
    sleep(1)
    print("performing EUTHANASIA")
    sleep(1)
    sys.exit()
elif d_cnt==2:
    a=input("would you like to kill the horse?(y/n)\n")
    if a=="y":
        print("your horse was a good horse ;)")
        print("performing EUTHANASIA")
        sys.exit()
        #implement stats like uma musume
    elif a=="n":
        print("you and ur horse go to the nxt race")
