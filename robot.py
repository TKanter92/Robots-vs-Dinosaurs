# CLASS: Robot
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor

from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = '100'
        self.weapons = []
        self.new_weapon = Weapon("Sword", 25)
        self.new_weapon1 = Weapon("Ray Gun", 60)
        self.new_weapon2 = Weapon("Grenade", 75)
# Methods
    def robot_attack(self, dinosaur):
       dinosaur.health -= self.weapon.attack_power

    def arsenal_fill(self):
        self.weapons.append(self.new_weapon)
        self.weapons.append(self.new_weapon1)
        self.weapons.append(self.new_weapon2)