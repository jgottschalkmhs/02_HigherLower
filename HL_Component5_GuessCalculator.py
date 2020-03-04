# HL component 5 - Guess Calculator
# Calculates how many guesses the user has dependant on the range of numbers given.

# Module import
import math


for item in range(0,4): # Loop component for easy testing

    low = int(input("Low: ")) # Int check in final code
    high = int(input("High: ")) # Int check in final code

    range = high - low + 1
    max_raw = math.log2(range) # gets maximum number of guesses using binary search
    max_upped = math.ceil(max_raw) # Rounds up max_raw
    max_guesses = max_upped + 1 # Gives the user an extra guess incase they mess up
    print("Max Gueses: {}".format(max_guesses)) # Displays amount of guesses to user
    print()