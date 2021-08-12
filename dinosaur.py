# CLASS: Dinosaur
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = '100'
        self.attack_power = attack_power


# Methods

    def dino_attack(self, robot):
        robot.health -= self.attack_power
