import random 

class Dice:
    def __init__(self,sides):
        self.sides=sides
    def roll(self):   
        return random.randint(1,self.sides)


dice=Dice(8)
for roll in range (100):
    print(dice.roll())