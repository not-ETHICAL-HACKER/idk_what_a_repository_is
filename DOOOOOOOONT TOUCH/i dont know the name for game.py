import sys
import random
import time
import threading
#im so tired trying to code just 400 lines bruh
#alll of this code is made from if statements
#i gotta learn how to actually code
def effect(text,delay=0.001):
     for char in text:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(delay)
def easter_egg():
    print("you found an easter egg")
    print("⨕,⨋,⟁,⧎,⚿,⛝,⛶,⛾,⯐,♂,♀,❂")
    print("it has been 60 seconds")
    threading.Timer(60, easter_egg).start()#do more of ts
#create a function for ebery game mechanic im llaly af
# please listendubfyvcxhjb 
regress_count=0
#create smth with admin and titles and stuff
#add sex?
#remeber max limit should be 2^32
m_ascii="""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⡀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣠⠘⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠟⠋⠡⢤⣴⣶⣶⣶⣦⣤⣬⣉⠛⠿⣿⣿⣿⠃⣼⣃⠘⠿⠟⠛⠛⠛⠛⠻⠿⠟⢠⣿⡆⢸⣿⠛⠉⣤⣤⣶⣶⣶⣶⣶⣶⣦⣤⣍⡙⠻⢿⣿⣿⣿⣿⣿
⣶⣶⣶⣦⣌⠻⣿⣿⣿⣿⣿⣿⡷⠂⣨⣿⡿⠀⢿⣈⣤⣶⣾⣿⣿⣿⣿⣷⣀⣴⣿⣿⠇⣸⣿⣿⣆⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣌⠙⢿⣿⣿
⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⠃⣾⣿⡟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣠⡈⢿⣿⣿⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠓⠄⠙⣿
⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⠀⣿⠏⡠⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢻⣿⠁⢿⣿⣿⣿⣿⣿⣿⣿⡇⣴⣿⣿⣿⣿⣿⣿⣦⣼
⣿⣿⣿⢋⣀⣩⣭⣉⠙⢿⣿⣿⣆⠘⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠃⣼⣾⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣶⠈⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⠛⢿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⡟⠛⣁⣴⣾⣿⣿⣿⠟⢉⣭⣬⣉⡙⠻⠈⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠛⣋⣉⠁⣿⣿⣿⣿⣿⡿⡄⣾⣿⣿⣷⣤⣾⣿⣿⣿⣿⣿⣿⣀⣌⡉⠙⠛⠿⣿⠀⣿⣿⣿⣿⣿⣷⣦⣈⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣾⣿⣿⡆⢨⣿⣿⣿⣿⣤⣶⣶⣶⣦⣤⣉⠙⣻⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣶⣌⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡙⠛⠿⢿⣿⣿⣿⣿⣿⣿⠿⣿⣿⢉⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠠⡄⢠⣤⣤⣤⣆⠙⡏⢸⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣁⣼⣿⣿⣿⣿⣆⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

dragon_ascii=("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
admin_pwrs= ["johan","irene","admin","j"]
alpha_testers=["sonish","hema","dk"]
exp=1
admin=1
test=1#use this var to give the playtesters more power
diff=1#use this variable to change the difficulty
lvl=0
status="normal"
inv="few gold coins,a rusty longswod"

while regress_count<(2**10):
    G=random.randint(1,2)#for gambling
    r = random.randint(1,20)#for dmg
    ra= random.randint(1,20)#for mana
    ran= random.randint(1,20)#for hp
    rand=random.randint(1,20)#for attack spped
    R = random.randint(1,100)#for general
    s=random.random()#for wattack speed
    spd=round(s,3)

    dmg=10+r
    dex=rand+10
    mp=ra+10
    hp=ran+10
    luck=R+50
    fatigue=R-25#if fatigue > 100 reduce stats by 50%
    gold=R//10

    mob = random.randint(1,10)#for number of mobs
    mobs = random.randint(1,100)#for grater number of mobs
    f_mobs = random.randint(150,1000)#for final stage mobs
    m_dmg = random.randint(1,10)#for dmg lidht monsters
    m_hp = random.randint(1,15)#hp of light monsters
    mo_dmg = random.randint(10,50)#for dmg midbosses
    mo_hp = random.randint(15,60)#hp for midbosses
    mon_dmg = random.randint(50,100)#for dmg bosses
    mon_hp = random.randint(60,120)#hp for boss monsters
    f_boss_dmg =random.randint(250,500)#for final boss dmg
    f_boss_dmg =random.randint(300,600)#for final boss hp
    f_boss_mini_dmg = random.randint(100,150)#minion dmg for final stage
    f_boss_mini_hp = random.randint (125,1775)#minion hp for final stage
    effect("""  _____                     _   _            ______ _   _ _______ ______ _____    _                
 |  __ \                   | | | |          |  ____| \ | |__   __|  ____|  __ \  | |               
 | |__) | __ ___  ___ ___  | |_| |__   ___  | |__  |  \| |  | |  | |__  | |__) | | | _____ _   _   
 |  ___/ '__/ _ \/ __/ __| | __| '_ \ / _ \ |  __| | . ` |  | |  |  __| |  _  /  | |/ / _ \ | | |  
 | |   | | |  __/\__ \__ \ | |_| | | |  __/ | |____| |\  |  | |  | |____| | \ \  |   <  __/ |_| |_ 
 |_|   |_|  \___||___/___/  \__|_| |_|\___| |______|_| \_|  |_|  |______|_|  \_\ |_|\_\___|\__, (_)
                                                                                            __/ |  
                                                                                           |___/   """)#coolest thing i haave did yet
    #now it is lol
    input()
    effect("Hello there  adventurer, what is your name?")  
    a=input("\nChoose your character's name:")
    time.sleep(0.5)
    print ("you have gained exp")
    time.sleep(0.5)
    print("Your stats are:\nSTR:",dmg,"\nattack speed:",spd,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nLUCK:",luck)

    if a in admin_pwrs:
        input()
        admin=2**32
        print("\U0001F43C You have unlocked admin powers")
        title="ADMIN"
        input()
        print("a small amount of exp is added")
        exp*=admin
        time.sleep(1)
        if exp>=5:
            lvl=lvl+(exp//5)
            exp=exp%5
            hp=hp+(10*lvl)
            dmg=dmg+(10*lvl)
            mp=mp+(10*lvl)
            dex=dex+(10*lvl)
            print("your currrent level is:",lvl)
            print("Your stats are:\nSTR:",dmg,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nLUCK:",luck)
        else:
            print("your too weak")
        dmg=dmg*admin
        hp=hp*admin
        mp=mp*admin
        dex=dex*admin
        luck=luck-(admin/(2**10))
        time.sleep(1.5)
        print("Your new admin stats are:\nSTR:",dmg,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nLUCK:",luck)
    elif a in alpha_testers:
        #do the same thng u did with admin_pwrs
        print("you have gained 'playtester' title")
        title="PLAYTESTER"
        print(a," huh what  an interesting name there")
        test=(1.1**R)
    else:
        print(a," huh what  an interesting name there")
    input()
    print("would you like a tutorial on how the game works?")
    c=input("(y/n)")
    if c=="n":
        print("Since you know the rules i'll make the game harder\nDIFFICULTY INCREAAAAAAAAAAAAAASED")
        diff+=1
    elif c=="y":
        effect("There are a few stats tht drastically affect gameplay")
        effect("dmg tells how much damage your attacks do.\ndmg also is a part of strnght checks(ie,to make ur character crush things)")
        effect("\nmp describes ur ability to do majic. its very hard to improve.\nit also affects intelligence checks")
        effect("\nhp is the amount of hitpoints you have.if ur hp goes below 0 u die")
        effect("\ndex is the ability to perform actions successfully.\nactions like lockpicking require high dex stats")
        effect("\nluck is a stat that contols the difficulty of the world.")
        effect("\nDifficulty is a experimental option which controls the overall difficulty of the game.\nHigher rewards will be provided")
    input()
    print("now , where are you going adventurer?")
    print("press 1 for going toward the river\n press 2 for going to the loud noises")
    b=int(input("choose your path="))
    if b>2:
        print("\U00002620YOU HAVE DIED\U00002620")
        input()
        print("\t\t\tEND SCREEN")
        print("your inventory = ",inv)#change the stats diplayed in the end screen
        print("your current lvl =",lvl)
        print("your current gold =",gold,"\U0001FA99")
        print("your luck = "+str(r),ra,ran,rand,R,sep="\U00002694")
        input()
        sys.exit()
    else:
        effect("you move in that direction")
        input()
        effect(dragon_ascii)
        input()
        b=int(input("you encounter a dragon. \ntype 1 to run into  a dungeon\ntype 2 to run into a forest:"))
    if b>1:
        print('you have entered the forset')
        input()
        print("you have encounterred a monster")
        input()
        effect(m_ascii)
        input()
        c=int(input("1.run , 2.fight"))
        if c==1:
            print("You have succesfullly fled the MONSTER ")
            print('current exp =',exp-1)
        else :
            dmg=dmg*test
            print("monster's hp =",m_hp)
            print("your dmg is",dmg,"\U0001F5E1")
            if dmg>=m_hp:
                int()
                print("you have succesfully defeated the monster")
                input()
                print("you have gained knowleddge of the monster")
                exp=exp+1
                print("would you like to loot it?")
                a=int(input("1.yes 2.no"))
                if a==1:
                    loot=2*R
                    if loot>=100:
                        print("you have obtained the CORE OF THE BEAST(D-)")
                        time.sleep(1)
                        inv=inv+",CORE OF THE BEAST(D-)"
                        print("YOU BGIN TO UNDERSTAND THE PHYSICAL WORLD")
                        time.sleep(1)
                        exp=exp+2
                    else :
                        print("ypu habe failed\nyou lose exp")
                        exp=exp-1
                else:
                    print("the corpse has withered away")
                    exp=exp+1
            else:
                print("\U00002620YOU HAVE DIED\U00002620")
                input()
                print("\t\t\tEND SCREEN")
                print("your inventory = ",inv)
                print("your current exp =",exp*admin)
                print("your current gold =",gold*admin,"\U0001FA99")
                print("your luck = "+str(r),ra,ran,rand,R,sep="\U00002694")
                input()
                sys.exit()
        print("You leave the forest")
        time.sleep(1)
        if exp>=5:
            lvl=lvl+(exp//5)
            exp=exp%5
            hp=hp+(10*lvl)
            dmg=dmg+(10*lvl)
            mp=mp+(10*lvl)
            dex=dex+(10*lvl)
            spd=spd+(0.1*lvl)
            print("your currrent level is:",lvl)
            print("Your stats are:\nSTR:",dmg,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nattack speed",spd,"\nLUCK:",luck)
        else:
            print("you dont have enough exp for lvling up")
        a=int(input("1.go up a nearby mountain\n2.continue along the river"))
        if a==1:
            print("""          /\\
         /**\\
        /****\   /\\
       /      \ /**\\
      /  /\    /    \        /\    /\  /\      /\            /\/\/\  /\\
     /  /  \  /      \      /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \/  \\
    /  /    \/ /\     \    /    \ \  /    \/ /   /  \/  \/  \  /    \   \\
   /  /      \/  \/\   \  /      \    /   /    \\
__/__/_______/___/__\___\__________________________________________________""")
            print("you try to climb the mountain")
            str_check=dmg*dex*luck
            print(str_check)
            if str_check>2000:
                print("you succed")
                input()
                print("you see a dragon in the distance\nit seems to be moving towards a small town")
                b=int(input("1.run away\n2.go to the town"))
                if b == 1:
                    print("you chose to flee death\you have earned the title'SURVIVALIST'.")
                    title=title+",SURVIVALIST"
                    exp=exp+1
                    dex=dex+10
                    hp=hp+5
                    dmg-=5
                else :
                    print("you have chosen the path of selflessness\nyou have gained the title'ROOKIE HERO'")
                    title=title+",ROOKIE HERO"
                    exp=exp+50
                    if exp>=5:
                        lvl=lvl+(exp//5)
                        exp=exp%5
                        hp=hp+(10*lvl)
                        dmg=dmg+(10*lvl)
                        mp=mp+(10*lvl)
                        dex=dex+(10*lvl)
                        ("your currrent level is:",lvl)
                        print("Your stats are:\nSTR:",dmg,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nLUCK:",luck)
                        time.sleep(1)
                        print("\nyou move toward  the village")
                    else:
                        print()
            else:
                print("you plummet to your death")
                hp=0
                print("\t\U00002620YOU HAVE DIED\U00002620")
                input()
                print("\t\t\tEND SCREEN")
                print("your current hp =",hp*admin)
                print("your current exp =",exp*admin)
                print("your current gold =",gold*admin,"\U0001FA99")
                print("your luck = "+str(r),ra,ran,rand,R,sep="\U00002694")
                sys.exit()
        else:
            print("you move along the river")
            time.sleep(1)
            print("You find a small cabin near the sea shore")
            cond=5/10
            #cond variablle decribes the struture of cabin(if it is lower than zero destroy cabin)
            time.sleep(1)
            a=input("Enter the cabin? (y/n)")
            if a=="y":
                print("you decide to rest at the cabin")
                print("use your str stat",dmg,".or your dex and int stats",dex,',',mp)
                a=int(input("1.dmg\n2.dex and int"))
                if a==1:
                   print("SUCCESS")
                   print("You enter the cabin")
                   cond=cond-3/10
                else:
                   print("You begin to use your mind ")
                   int_chk=dex*mp
                   if int_chk>100:
                        print("SUCCESS")
                        print("You enter the cabin")
                   else:
                        print("You FAILED miserably")
                        time.sleep(1)
                        print("the weak structure falls on you")
                        time.sleep(0.5)
                        print("\t\U00002620YOU HAVE DIED\U00002620")
                        input()
                        print("\t\t\tEND SCREEN")
                        print("your current hp =",hp)
                        print("your current lvl =",lvl)
                        print("your current gold =",gold,"\U0001FA99")
                        print("your luck = "+str(r),ra,ran,rand,R,sep="\U00002694")
                        sys.exit()
            else:
              print("you see a group of tiny wolves")
              a=input("massacre?(y/n)")
              if a=="y":
                print("you succesfully killed the pack")
                print("you gain exp")
                exp+=2*mob
                print("You are fatigued\nrest immediatly or lose effectivness in life")
                a=input("would you like to rest?(y/n)")
                if a=='y':
                    print("you begin to rest")
                    status="rested"
                    fatigue=fatigue-25
                    if fatigue<0:
                        print("you are fully rested")
                        fatigue=0
                        print("your stats have slightly increased")
                        dmg=dmg+5
                        hp=hp+5
                        mp=mp+5
                        dex=dex+5
                        print("Your stats are:\nSTR:",dmg,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nLUCK:",luck)
                elif a=='n':
                    print("you have chosen to be fatigued")
                    fatigue=fatigue+25
                    if fatigue>100:
                        print("you are too fatigued")
                        dmg=dmg/2
                        hp=hp/2
                        mp=mp/2
                        dex=dex/2
                        print("Your stats are:\nSTR:",dmg,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nLUCK:",luck)
                    else:
                        print("you are fatigued but can still function")
                else:
                    print("you have failed to choose")
                    print(" your inability to choose has confused you")
                    print("you lose 10 hp and 10 mp")
                    mp=mp-10
                    hp=hp-10
    else:           
        print("you have entered the dungeon")
        input()
        print("You encounter a chest")
        a=int(input("press 1 to open it\npress 2 to leave it"))
        if a==1:
            print("the chest had some gold coins")
            gold=gold+(R//10)
        else:
            print("you move towards the strange sound")
        input()
        print("you encounter a fork in the path")
        b=int(input("1. towards the noise\n2.towards the light"))
    if b==1:
        print("You witness a hoard wywern hatchlings")
        m_hp=5*mob
        h_dmg=2*m_dmg    
        a=int(input("1.attack\n2.run"))
        if a==1:
            hp=hp-h_dmg
            m_hp=m_hp-dmg
            if m_hp<=0:
                print("you have defeated the hatchlings")
                time.sleep(1)
                print("you have gained the title'INFANTICIDE'")
                exp+=1
                title=title+",INFANTICIDE"
                print(title)
            else:
                print("you have failed,would you like to try again?")
    elif b==2:
        print("you encountr a puzzle")
        time.sleep(1)
        print("Attempt to deciper it?")
        a=int(input("1.yes\n2.no"))
        if a == 1:
            print("you brgin to understand it")
            time.sleep(1)
            if mp>10:
                print("you understand the runes engraved on the door")
                time.sleep(1)
                print("the runes tell of a arithmetic problem")
                time.sleep(1)
                print("The area of a rectangular plot is 528 m^2. The length of the plot (in metres) is one more than twice its breadth.find lenght")
                b=int(input("enter ur ans:"))
                if b==33:
                    print("you solved the puzzle.")
                    time.sleep(0.5)
                    print("you loot the gold inside")
                    gold=gold+1000
                    mp=mp+10
                    dex=dex+5
                else:
                    print("its wrong")
                    time.sleep(0.5)
                    print("ur too stupid")
                    time.sleep(0.5)
                    print("\t\U00002620YOU HAVE DIED\U00002620")
                    input()
                    print("\t\t\tEND SCREEN")
                    print("your current hp =",hp)
                    print("your current lvl =",lvl)
                    print("your current gold =",gold,"\U0001FA99")
                    print("your luck = "+str(r),ra,ran,rand,R,sep="\U00002694")
                    sys.exit()
            else:
                print("ur too dum.increses ur int")
        else:
            print("you walk away.")
#think of beter ways to implement color and othertxt effects 
#r is the random numnber generator tht determines combat
#implement r into combat
#implement attack speed into combat
#implement mana and hp into cmbat
    if hp<0:
        print("\t\U00002620YOU HAVE DIED\U00002620")
        input()
        print("\t\t\tEND SCREEN")
        print("your current hp =",hp)
        print("your current exp =",exp)
        print("your current gold =",gold,"\U0001FA99")
        print("your luck = ")
        sys.exit()
    print("\t\t\tEND SCREEN")
    print("hope you enjoyed the game :)")
    time.sleep(1)
    print("your current hp =",hp)
    print("your current lvl =",lvl)
    print("your current gold =",gold,"⧰")
    print("your luck = ",R)
    print(title)
    regress=input("Would You Like To Try again?(y/n)")
    if regress=="y":
            regress_count+=1
    elif regress == "n":
            regress_count+=1024
time.sleep(6.9420)
print("1st_EASTER_EGG_15_08_2025")
time.sleep(5)
effect("⨕,⨋,⟁,⧎,⚿,⛝,⛶,⛾,⯐,♂,♀,❂",delay=1)#misc materials for the game