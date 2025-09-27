from time import sleep
def plane():
    a=0
    b=0
    while True:
        if a>=100:
            b=1
            if b==1:
                print("\n"*10)
                print("""  _______   _        _     
 |__   __| | |      (_)    
    | | ___| |_ _ __ _ ___ 
    | |/ _ \ __| '__| / __|
    | |  __/ |_| |  | \__ \\
    |_|\___|\__|_|  |_|___/
                           
                           """)
                break
        print(" "*137+"|"*25)
        print(" "*137+"|"*25)
        print(" "*137+"|"*25)
        print(" "*(17+a)+("_"*4)+(" "*3)+("_"*4)+(" "*8+"/")+(" "*1+"|"*25))
        print(" "*(17+a)+("\\"*4)+(" "*3)+("/"*4)+(" "*7+"/")+(" "*2+"|"*25))
        print(" "*(20+a)+("="*10)+"D>-<|"+(" "*3+"|"*25))
        print(" "*(17+a)+("/"*4)+(" "*3)+("\\"*4)+(" "*7+"\\")+(" "*2+"|"*25))
        print(" "*(17+a)+("¯"*4)+(" "*3)+("¯"*4)+(" "*8+"\\")+(" "*1+"|"*25))
        print(" "*137+"|"*25)
        print(" "*137+"|"*25)
        print(" "*137+"|"*25)
        a+=1
        sleep(0.1)
'''
class solution:
        def __init__(self,nums):
            self.nums=nums
        def sum_wo_ai(nums,target):
            l=[]
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i]+nums[j]==target:
                        l.append([i])
                        print(l)
            return l
solution.sum_wo_ai([1,23,67,73,2,1],69)'''
l=[
    [
        [1,2,3],
        [2,3,1],
        [3,2,1]
    ],
    [
        [4,5,6],
        [5,6,4],
        [6,5,4]
    ],
    [
        [7,8,9],
        [8,9,7],
        [9,8,7]
    ]
]
import random
def bet_print(printf,jumbler=False,font=False,sussy_mode=False):
        if jumbler==False and font==False and sussy_mode==False:
            print(printf)
        if jumbler==True and sussy_mode==True and font==True:
            print("no,im not doing that")

        if jumbler==True:
            for _ in range(len(printf)):
                ra=random.randrange(0,len(printf))
                print(printf[ra],end="")
            print()
        if font==True:
            for ch in printf:
                if ch.isalpha():
                    print(ch.upper(),end="")
                else:
                    print(ch,end="")
        if sussy_mode==True:
            print("\nඞ Sussy baka detected! ඞ")
            print('ඞ'*10)
            if sussy_mode==True and font==True:
                for ch in printf:
                    if ch.isalpha():
                        print(ch.upper(),end="")
                    else:
                        print(ch,end="")
                    print("ඞ",end="")
bet_print("My Name is JOHAN",jumbler=True,font=True,sussy_mode=True)