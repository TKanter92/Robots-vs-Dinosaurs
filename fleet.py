# CLASS: Fleet
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor
from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

# Methods

    def create_fleet(self):
        robot_one = Robot("Kitt")
        robot_two = Robot("Wall-E")
        robot_three = Robot("BayMax")
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)


