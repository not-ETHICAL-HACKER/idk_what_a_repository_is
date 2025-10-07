def lvl_up(exp):
    lvl=lvl+(exp//5)
    exp=exp%5
    luck=luck
    hp=hp+(10*lvl)
    dmg=dmg+(10*lvl)
    mp=mp+(10*lvl)
    dex=dex+(10*lvl)
    ("your currrent level is:",lvl)
    print("Your stats are:\nSTR:",dmg,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nLUCK:",luck)
    return exp,lvl
import time
import sys
def d_end_scr():
    print("\t\U00002620YOU HAVE DIED\U00002620")
    time.sleep(0.5)
    print("\t\t\tEND SCREEN")
    print("Your stats are:\nSTR:",dmg,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nLUCK:",luck)
    print(f"Thank you for playing my game;)")
    sys.exit()
def fatigue(fatigue):
    if fatigue>100:
        print("you are too fatigued")
        dmg=dmg/2
        hp=hp/2
        mp=mp/2
        dex=dex/2
        print("Your stats are:\nSTR:",dmg,"\nMP:",mp,"\nHP:",hp,"\nDEX:",dex,"\nLUCK:",luck)
    elif fatigue>200:
        print("you are now super fatiged")
        dmg=dmg/4
        hp=hp/4
        mp=mp/4
        dex=dex/4
        print(f"")
    else:
        print("you are fatigued but can still function")
        fatigue+=10