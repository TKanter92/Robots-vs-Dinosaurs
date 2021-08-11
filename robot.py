# CLASS: Robot
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor



class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon
        self.attack_type = ''
        self.attack_dinosaur = ''


# Methods
    def robot_attack(self, dinosaur):
       dinosaur.health -= self.weapon.attack_power