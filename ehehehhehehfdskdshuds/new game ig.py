#new password guessr game ig
from random import randint
from time import sleep
n=1
for i in range (2):
    r = randint(1000,9999)
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
        for i in range(5):
            print(f"this is your {n} time cracking the code")
for i in range (100):
    r=randint(1000,9999)
    r=str(r)
    r=list(r)
    if r[0]==r[1]:#for finding same starting digits
        print(r)
    elif r[2]==r[3]:
        print(r)# dont forget to remove break
    else:
        print()
