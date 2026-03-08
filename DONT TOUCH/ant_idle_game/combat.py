import math
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH1 = os.path.join(BASE_DIR, "log", "combat_log.txt")
LOG_PATH2 = os.path.join(BASE_DIR, "log", "aoe_log.txt")

def log_1v1(mob1, mob2):
    with open(LOG_PATH1, "a") as f:
        f.write(f"{mob1.mob_id} fought {mob2.mob_id}\n"
                f"  {mob1.mob_id} energy: {mob1.energy:.1f}\n"
                f"  {mob2.mob_id} energy: {mob2.energy:.1f}\n\n")

def log_aoe(center, affected):
    with open(LOG_PATH2, "a") as f:
        f.write(f"{center.mob_id} used AOE\n")
        for mob in affected:
            f.write(f"  - {mob.mob_id}\n")
        f.write("\n")

class Combat:
    def __init__(self):
        self.pwr_lvls: dict[str, int] = {
            "Weak": 1, "Strong": 2,
            "Adult": 2, "Elder": 3, "Ancient": 4
        }

    def fight(self, mob1: 'Mob', mob2: 'Mob'):
        mon1 = (self.pwr_lvls[mob1.mob_type] + mob1.energy - mob1.age )/ 10
        mon2 = (self.pwr_lvls[mob2.mob_type] + mob2.energy - mob2.age )/ 10
        if mob1.old_type == "Weak" and mob2.old_type == "Weak" and (mob1.mob_type == "Ancient" or mob2.mob_type == "Ancient"):#? old_type = mob's origin type, unchanging even as mob_type evolves
            return
        if mon1 > mon2:
            mob1.energy += max(0,mob2.energy)**0.5
            mob2.energy = 0
        elif mon2 > mon1:
            mob2.energy += max(0,mob1.energy)**0.5
            mob1.energy = 0
        else:
            mob1.energy /= 2
            mob2.energy /= 2
        log_1v1(mob1, mob2)

    def aoe_damage(self, center: 'Mob', mobs: list['Mob']):
        rad = {"Weak": 0, "Strong": 1, "Adult": 1, "Elder": 2, "Ancient": 3,"Nuke": 6}
        dmg_range = {
            "Weak":   (10,  25),  "Strong": (25,  50),
            "Adult":  (50,  100), "Elder":  (100, 200), "Ancient": (200, 400),
            "Nuke" : (100,500)
        }
        r = rad[center.mob_type]
        weak_flag = center.old_type == "Weak"
        lo, hi = dmg_range[center.mob_type]
        cx, cy = center.coords
        affected = []
        for mob in mobs:
            mx, my = mob.coords
            if mob is not center and abs(mx - cx) <= r and abs(my - cy) <= r and not (weak_flag or (mob.old_type == "Weak")): #? old_type = mob's origin type, unchanging even as mob_type evolves
                mob.energy -= max(0,random.randint(lo, hi))
                affected.append(mob)
        if affected:
            log_aoe(center, affected)