import random
import time
import sys
def effect(text,delay=0.01):
     for char in text:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(delay)

h=("heads","HEADS","Heads","h")
t=("tails","TAILS","Tails","t")

b=0
s=0
play=0
r=10**10
p_lvl=0
w_p=0
l_p=0
luck=0
t_s=0
ach=""
t_play=0
r3=0

while r>b:
    print("\t\t\t\t\U00002666 YOUR PRESTIGE LEVEL IS",p_lvl,"\U00002666")
    play+=1
    t_play+=play
    a=input("\n\t\t\t\t\tHEADS or TAILS\n\t\t\t\t\t")
    r1=random.randint(1,2)
    r2=random.randint(1+luck,100-luck)
    if r2<=50:
        r3+=r2+50
    elif r2<=75:
        r3+=r2+20
    print("your luck:",r3)
    if r2==50:
        print("you hit the jackpot")
        b+=1
        s+=10**10
        t_s+=s
        ach+="JACKPOT"
        print(ach)
    elif a in h:
        if r1==1:
            print("you win")
            s+=1+w_p
            t_s+=s
        elif r1==2:
            print("you lose")
            s+=l_p
            t_s+=s
    elif a in t:
        if r1==1:
            print("you lose")
            s+=l_p
            t_s+=s
        elif r1==2:
            print("you win")
            s+=1+w_p
            t_s+=s
    v=input("Continue?(y/n)\n")
    if v=="y":
        b+=1
        continue
    elif v=="n":
        p=(s/play)*100
        print("your total points is:",s,"\nwin percentage=",p,"%")
    p_lvl+=1
    sh=input("would you like to enter the prestige shop?(y/n)[press 'q' to exit]\n")
    s=0
    play=0
    if sh=="y":
        print("what would you like to buy?\n")
        shop=int(input("1.more luck\n2.more points\n3.points for losing\nChoice:"))
        if shop==1:
            print("you gain more luck")
            luck+=10
            if luck>50:
                luck=49
            else:
                print()
            continue
        elif shop==2:
            print("you gain more points when winning")
            w_p+=1
            print()
            continue
        elif shop==3:
            print("you gain points even by losing")
            print()
            l_p+=1
            continue
    elif sh=="n":
        print("good luck in your nxt lvl")
    elif sh=="q":
        print("please play my game again :)")
        b+=1+r
    #find a way to implement prestige lvl and scores to be shown atlast
effect("thank you for playing")
t_per=(t_s/t_play)*100
print("\nYour total score is:",t_s,"\npoint percentage=",t_per,"%","\nThe prestige level:",p_lvl,"\nAcheivements:",ach)
time.sleep(10)