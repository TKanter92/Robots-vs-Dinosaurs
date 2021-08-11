# CLASS: Battlefield
# Author: Tyler Kanter
# Create Date: August 11th, 2021

from fleet import Fleet 
from herd import Herd

# Constructor
class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


# Methods

my_fleet = Fleet()
my_fleet.robot_fleet[0].robot_attack("Rex")
my_fleet.robot_fleet[1].robot_attack("Tiny")
my_fleet.robot_fleet[2].robot_attack("Arlo")

