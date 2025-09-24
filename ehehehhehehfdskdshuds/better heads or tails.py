import random
def age(x:int):
    rating=""
    if 0<x<18:
        print("get out of here ya minor")
        rating+="minor"
        print(f"your age rating is -{rating}-")
    elif x==18 or x==17 or x==19:
        rating+="barely legal"
        print(f"your age rating is '{rating}'")
    elif x>18:
        rating+="good luck bruh"
        print(f"your rating is+{rating}+")
    else:
        rating+="how tf?"
        print(f"ur lying (rating is _{rating}_)")
    return rating
score=0
def coin_toss(x:int,A_rated: bool=False):
    random_cointoss=random.randint(1,2)
    global score
    if x==random_cointoss:
        print("ya woon yippe")
        score+=1
    elif x!=random_cointoss:
        if A_rated==False:
            print("ya lost")
            score+=-1
            if score<0:
                print("ur too stupid at ts")
        else:
            print("you stpid fucking idiot ur rong")
            score+=-1
            if score<0:
                print("ya fucking retard\nya lost ")
    return score
for i in range(3):
    a=input("heads or tails? (1 or 2)\n('q' for quitting )\n")
    if a.lower()=="q":
        break
    else:
        a=int(a)
    coin_toss(int(input(a)))
print(f"YOur Score is {score}")