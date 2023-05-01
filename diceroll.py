import random

def roll_dice(num_dice, num_sides):
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        total += roll
        print(f"Die {i+1}: {roll}")
    print(f"Total: {total}")

num_dice = int(input("How many dice would you like to roll? "))
num_sides = int(input("How many sides do the dice have? "))

roll_dice(num_dice, num_sides)
