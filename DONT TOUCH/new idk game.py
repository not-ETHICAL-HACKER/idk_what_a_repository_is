import time,sys,random,threading,pyautogui
class env():
    def __init__(self):
        self.x=1
    def hill(self):
        print("""          /\\
         /**\\
        /****\   /\\
       /      \ /**\\
      /  /\    /    \        /\    /\  /\      /\            /\/\/\  /\\
     /  /  \  /      \      /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \/  \\
    /  /    \/ /\     \    /    \ \  /    \/ /   /  \/  \/  \  /    \   \\
   /  /      \/  \/\   \  /      \    /   /    \\
__/__/_______/___/__\___\__________________________________________________""")
    def cliff(self):
        print("NOt DONE YET")
class m_art():
    def __init__(self):
        self.x=1
    def dragon(self):
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
    def bat(self):
        print("""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
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
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣁⣼⣿⣿⣿⣿⣆⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
class player():
    def __init__(self):
        self.x=1
        self.dmg=10
        self.hp=100
        self.mana=50
        self.dex=5
        self.luck=10
        self.exp=0
        self.lvl=1
        self.inv=["wooden sword","healing potion"]
        self.coins=0
    def stats(self):
        dmg=random.randint(1,20)
        hp=random.randint(50,100)
        mana=random.randint(20,50)
        dex=random.randint(1,10)
        luck=random.randint(1,100)
        print(f"DMG: {dmg}\nHP: {hp}\nMANA: {mana}\nDEX: {dex}\nLUCK: {luck}")
        return [dmg,hp,mana,dex,luck]
    def lvl_up(self,exp):
        if exp>=10:
            print("LEVEL UP!")
            lvl=exp//10
            print(f"YOU ARE NOW LEVEL {lvl}")
            exp=exp-(lvl*10)
            print(f"your stats are now:")
            print(f"DMG: {self.dmg+(lvl*2)}\nHP: {self.hp+(lvl*5)}\nMANA: {int(self.mana+(lvl*(1.2+lvl//2)))}\nDEX: {int(self.dex+(lvl*(1.5+lvl//2)))}\nLUCK: {self.luck+(lvl)}")
            return exp
        else:
            print(f"{10-exp} EXP TILL NEXT LEVEL")
            return exp
    def death(self):
        if self.hp<=0:
            print("YOU DIED")
            sys.exit()
        else:
            print("You have beaten death. For now...")
    def inv(self,add:str=None,remove:str=None):
        if add is not None:
            self.inv.append(add)
            print(f"{add} added to inventory")
        if remove is not None:
            if remove in self.inv:
                self.inv.remove(remove)
                print(f"{remove} removed from inventory")
            else:
                print(f"{remove} not in inventory")
        print(f"Inventory:")
        for item in self.inv:
            print(f"=> {item}")
class misc:
    def __init__(self):
        self.x=1
    def bit_check(self,bits:int=1):
        print(f"This funtion will check the final digit is even or odd :\n{bits}->{bits&1}")
misc().bit_check(1001)