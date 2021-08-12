# CLASS: Battlefield
# Author: Tyler Kanter
# Create Date: August 11th, 2021

from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet 
from herd import Herd

# Constructor
class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


# Methods

    def run_game(self):
        self.welcome_notice()

    def welcome_notice(self):
        print("Welcome! Prepare for war!")

    while ((Robot.health != 0) and (Dinosaur.health != 0)):
        def attack_rounds(self):
            self.fleet.robot_fleet[0].robot_attack(self.herd.dino_herd[0])
            self.fleet.robot_fleet[1].robot_attack(self.herd.dino_herd[1])
            self.fleet.robot_fleet[2].robot_attack(self.herd.dino_herd[2])
            self.herd.dino_herd[0].dino_attack(self.robot.fleet[0])
            self.herd.dino_herd[1].dino_attack(self.robot.fleet[1])
            self.herd.dino_herd[2].dino_attack(self.robot.fleet[2])

        if (Robot.health == 0):
            print("The Dinosaur herd has won!")
            break
        elif (Dinosaur.health == 0):
            print("The Robot fleet has won!")
            break


