from random import randint

class Die():

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, side):
        print("Roll the {0}".format(side))

die = Die(6)
for x in range(1, 11):
    side = randint(1, die.sides)
    die.roll_die(side)

die1 = Die(10)
for x in range(1, 11):
    side = randint(1, die1.sides)
    die1.roll_die(side)

die2 = Die(20)
for x in range(1, 11):
    side = randint(1, die2.sides)
    die2.roll_die(side)
