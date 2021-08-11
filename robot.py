# CLASS: Robot
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor

from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self, name):
        self.name = ''
        self.health = 100
        self.weapon = ''
        self.attack_type = ''
        self.attack_dinosaur = ''


# Methods

def robot_details(self):
    self.name = input("What is the name of your robot?")

def robot_attack(self, dinosaur):
    self.attack_dinosaur = dinosaur
    self.attack_type = ''