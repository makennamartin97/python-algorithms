# As you can see, peons have limited abilities. They only have default health 
# point of 100 and can't attack but can only takeDamage.

# Imagine that you wanted to create a new class called Warrior. You want 
# warrior to have everything that a Peon has. You also want the warrior to 
# do everything that a Peon can do. In addition, however, you want to set it 
# up such that

# when a warrior is created, you want the default hp to be 200!
# you want the warrior to have a default 'armor' of 70, which means 70% of the damage will be reduced.
# you want to add a new method called attack(), which returns a random integer between 10 to 20.
# you want the warrior to override the takeDamage(dmg) method.  This time, its hp would only go down by 30% of dmg (as its armor would have absorbed 70% of dmg).
# Finish implementing class Warrior using inheritance.

import random

class Peon:
    def __init__(self):
         self.hp = 100
    
    def takeDamage(self, dmg):
         self.hp = self.hp - dmg
    
    def returnHP(self):
        return self.hp
# note that we're creating a new class Warrior that EXTENDS from an existing class Peon
class Warrior(Peon):
    def __init__(self):
        self.hp = 200
        self.armor = 70

    def attack(self):
        return random.randint(10,21)

    def takeDamage(self, dmg):
        self.hp = self.hp - (dmg * .30)
        return self.hp

       

# testing
warrior1 = Warrior()
warrior2 = Warrior()

print(warrior1.returnHP()) #200
print(warrior1.armor) #70
print(warrior1.attack()) 
print(warrior1.takeDamage(100)) #170.0
print(warrior2.takeDamage(200)) #140.0
print(warrior1.returnHP()) #170.0
print(warrior2.armor) #70
