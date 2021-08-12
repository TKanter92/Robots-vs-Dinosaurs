# CLASS: Fleet
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor

from robot import Robot

class Fleet:
    def __init__(self):
        my_robot = Robot("BayMax")
        my_robot1 = Robot("Kitt")
        my_robot2 = Robot("Wall-E")
        self.robot_fleet = [my_robot, my_robot1, my_robot2]


