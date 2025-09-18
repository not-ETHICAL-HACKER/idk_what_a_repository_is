#new password guessr game ig
from random import randint
from time import sleep
n=1
i,j=0,5
ii,jj=0,2
ran=0
while ii<jj:
    ii+=1
    r = randint(1000,9999)
    r=ran
    print("you are playing a gme abt how to find the password")
    print(r)
    sleep(1)
    if r%2 != 0:
        print("the last number is a odd number.")
    else:
        print("the last number is an even number.")
    sleep(1)
    r=r//10
    if r%2 != 0:
        print("the third number is a odd number.")
    else:
        print("the third number is an even number.")
    r=r//10
    sleep(1)
    if r%2 != 0:
        print("the second number is a odd number.")
    else:
        print("the second number is an even number.")
    r=r//10
    sleep(1)
    if r%2 != 0:
        print("the first number is a odd number.")
    else:
        print("the first number is an even number.")
    print("would you like to break the password now?")
    a=input("(y/n)")
    if a=="y":
        print("the password has to be cracked in 5 attempts or else you fucking die")
        while i<j:
            print(f"this is your {n} time cracking the code")
            b=int(input("enteer your guess"))
            if b==ran:#try using lists to try to predict the password like wordle
                print("you guessed correctly you win")
                i+=5
            elif b!=ran:
                print("ur wrong\ntry again")
                i+=1
            n+=1
    elif a=="n":
        print("allright dumahh")
