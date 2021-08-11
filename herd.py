# CLASS: Herd
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor

from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        dino_one = Dinosaur("Rex", 40)
        dino_two = Dinosaur("Tiny", 50)
        dino_three = Dinosaur("Arlo", 65)
        self.dino_herd = [dino_one, dino_two, dino_three]


# Methods