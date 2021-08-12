# CLASS: Herd
# Author: Tyler Kanter
# Create Date: August 11th, 2021


# Constructor

from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

# METHODS

    def create_herd(self):
        dino_one = Dinosaur("Rex", 40)
        dino_two = Dinosaur("Tiny", 50)
        dino_three = Dinosaur("Arlo", 65)
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
        
