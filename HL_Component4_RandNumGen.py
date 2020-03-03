# Higher Lower random number generator

# To Do
# - Get how many rounds
# - Get upper bound and lower bound from user
# - Make a random number between an upper bound and lower bound for each round

import random

# Get Input
low_num = int(input("Choose a low number")) # Get lowest of range
high_num = int(input("Choose a high number")) # Get highest of range
rounds = int(input("Amount of rounds")) # Get how many rounds

# Generate random num
for item in range(0, rounds): # Loops code for amount of rounds
    random_num = random.randint(low_num,high_num) # Generates random number
    print(random_num) # Displays random number
    # -v- heh