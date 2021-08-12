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
        self.display_welcome()

    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs! Prepare for war!")
        print("Select your attacker, then defender")

    def battle(self):
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
            self.show_robo_opponent_options()
            chosen_index = int(input())
            chosen_robot = self.fleet.robots[chosen_index]
            self.robo_turn(chosen_robot)

            if len(self.herd.dinosaurs) > 0:
                self.show_dino_opponent_options()
                chosen_index = int(input())
                chosen_dinosaur = self.herd.dinosaurs[chosen_index]
                self.dino_turn(chosen_dinosaur)

    def dino_turn(self):
        self.show_robo_opponent_options()
        chosen_index = int(input())
        chosen_robot = self.fleet.robots[chosen_index]
        self.dino_turn(chosen_robot)

    def robo_turn(self):
        self.show_dino_opponent_options()
        chosen_index = int(input())
        chosen_dinosaur = self.herd.dinosaurs[chosen_index]
        self.robo_turn(chosen_dinosaur)

    def show_dino_opponent_options(self):
        chosen_index = int(input())
        print("choose your dinosaur:")
        index = 0
        for dinosaur in self.fleet.dinosaurs:
            print(f'Type {index} for {dinosaur}')
            index += 1
        

    def show_robo_opponent_options(self):
        chosen_index = int(input())
        print("choose your robot:")
        index = 0
        for robot in self.fleet.robots:
            print(f'Type {index} for {robot}')
            index += 1

    def display_winners(self):
        self.display_winners()



