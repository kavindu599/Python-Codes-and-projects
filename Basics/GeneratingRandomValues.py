#bulit in random library
import random

#1
for i in range(3):
    print(random.random())


#2
for i in range(3):
    print(random.randint(12, 20))


#3
members = ['john', 'mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)

#4
class Dice:
    def roll(self):
        number1 = random.randint(1,6)
        number2 = random.randint(1,6)
        return number1, number2


dice = Dice()
print(dice.roll())


