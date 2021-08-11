# CLASS: Fleet
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor

from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        new_weapon = Weapon("Sword", 25)
        new_weapon1 = Weapon("Ray Gun", 60)
        new_weapon2 = Weapon("Grenade", 75)
        my_robot = Robot("BayMax", new_weapon)
        my_robot1 = Robot("Kitt", new_weapon1)
        my_robot2 = Robot("Wall-E", new_weapon2)
        self.robot_fleet = [my_robot, my_robot1, my_robot2]


# Methods

