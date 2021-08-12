# CLASS: Dinosaur
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100


# Methods

    def attack(self, robot):
        robot.health -= self.attack_power

    def __str__(self):
        return self.name
