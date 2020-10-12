# # Objectives
# Let's create a class called Fighter.

# A fighter should have the following attributes:

# level of 1
# hp of 100
# mp of 20
# strength of 20
# armor of 60 (this means damaged is reduced by 60%)
# It should also have the following methods:

# attack() - return a random integer between strength/2 and strength
# takeDamage(amount) - updates hp based on the damage amount.  Apply the 
# armor damage reduction.
# level_up() - increases strength, and armor by 20%.  Increase hp and mp 
# by 30 and level by 1.  For example, if the fighter had a hp and mp of 2 
# before leveling up, update its hp and mp to 32.  Note that majority of 
# games don't have the character level up like this, but in this game, 
# we'll follow this rule.

import random
class Fighter:
    def __init__(self):
        self.level = 1
        self.hp = 100
        self.mp = 20
        self.strength = 20
        self.armor = 60
    def attack(self):
        low = self.strength/2
        r = random.randint(low, self.strength)
        return r
    def takeDamage(self, dmg):
        dmg = dmg - (dmg*(self.armor/100))
        self.hp = self.hp-dmg

    def level_up(self):
        self.level+=1
        self.hp+=30
        self.mp+=30
        self.strength = self.strength + self.strength*.2
        self.armor = self.armor + self.armor*.2