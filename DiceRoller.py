 
#! Random Dice:
#!
#! Asks the user for the number of 
#! sides and generates random value 
#! between and given range. 

import random as random

#? default value: True
#? User will be prompted after every round to change 
#? its value
tryAgain = True  

start = 1
#? Inputs how many sides from the user and coverts
#? into integer
maxValue = int(input("How many sides do you need? "))
num = 1

def rollDie(start, maxValue, num):
    for j in range(1):
        return random.randint(1, maxValue)

while tryAgain:
    number = rollDie(start, maxValue, num)
    print(number)
    
    ask = input("Do you wish to roll again? (y/n) ")

    if ask == "y":
        tryAgain = True
    elif ask =="n":
        tryAgain = False
        