# To solve the expected number of moves required to beat snakes and ladders

import random
import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

blockPrint()

def RollDice():
    x = random.randint(1, 6)
    return x

countarray = []

for i in range (10000):

    tile = 0
    count = 1
    y = RollDice()

    while tile == 0 and y != 6:
        print("You rolled a", y , "you cannot move")
        y = RollDice()
        count += 1

    print(count)
    tile = tile + y

    while tile < 100:
        if tile == 2:
            tile = 23
            print("You climbed a ladder")
        elif tile == 6:
            tile = 45
            print("You climbed a ladder")
        elif tile == 20:
            tile = 59
            print("You climbed a ladder")
        elif tile == 52:
            tile = 72
            print("You climbed a ladder")
        elif tile == 57:
            tile = 96
            print("You climbed a ladder")
        elif tile == 71:
            tile = 92
            print("You climbed a ladder")
        elif tile == 43:
            tile = 17 
            print("You slid down a snake")
        elif tile == 50:
            tile = 5
            print("You slid down a snake")
        elif tile == 56:
            tile = 8 
            print("You slid down a snake")
        elif tile == 73:
            tile = 15
            print("You slid down a snake")
        elif tile == 87:
            tile = 49
            print("You slid down a snake")
        elif tile == 84:
            tile = 63
            print("You slid down a snake")
        elif tile == 98:
            tile = 40
            print("You slid down a snake")
        else:
            tile = tile     

        y = RollDice()
        count += 1
        tile = tile + y
        if tile > 100:
            tile = 100 - (tile -100)
        print("You rolled a", y)
        print("You are on tile", tile)
    
    countarray.append(count)

z = sum(countarray) / len(countarray) 

enablePrint()
print(z)

twoPlayerArray = []

for i in range(0, len(countarray), 2):
    twoPlayerArray.append(min(countarray[i: i+2]))        
print(sum(twoPlayerArray) / len(twoPlayerArray))

fourPlayerArray = []

for i in range(0, len(countarray), 4):
    fourPlayerArray.append(min(countarray[i: i+4]))        
print(sum(fourPlayerArray) / len(fourPlayerArray))