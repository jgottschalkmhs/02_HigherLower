# Higher Lower random number generator

# To Do
# - Get how many rounds
# - Get upper bound and lower bound from user
# - Make a random number between an upper bound and lower bound for each round

import random

# Get Input
low_num = int(input("Choose a low number"))
high_num = int(input("Choose a high number"))
rounds = int(input("Amount of rounds"))

# Generate random num
for item in range(0, rounds):
    random_num = random.randint(low_num,high_num)
    print(random_num)