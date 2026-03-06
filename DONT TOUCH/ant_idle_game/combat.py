import random
def log(mob1,mob2):
    with open("DONT TOUCH\\ant_idle_game\\log\\combat_log.txt","a") as f:
        f.write(f"{mob1.mob_id} fought {mob2.mob_id}\nAnd {mob1.mob_id} has {mob1.energy} energy left\nAnd {mob2.mob_id} has {mob2.energy} energy left\n\n")

class Combat:
    def __init__(self):
        self.pwr_lvls:dict[str,int]={
            "Adult": 2,
            "Elder": 3,
            "Ancient": 4,
            "Weak": 1,
            "Strong": 2
        }
    def fight(self,mob1:'Mob',mob2:'Mob'):
        mon1 = self.pwr_lvls[mob1.mob_type]+mob1.energy-mob1.age/10
        mon2 = self.pwr_lvls[mob2.mob_type]+mob2.energy-mob2.age/10
        if mon1 > mon2:
            mob1.energy += mob2.energy/2
            mob2.energy = 0
        elif mon2 > mon1:
            mob2.energy += mob1.energy/2
            mob1.energy = 0
        else:
            mob1.energy /= 2
            mob2.energy /= 2
        log(mob1,mob2)