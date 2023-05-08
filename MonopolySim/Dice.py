import random

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def rollDice(self):
        num = random.randint(1, self.sides)
        return num