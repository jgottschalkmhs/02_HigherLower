# HL Complete program
# Im putting together the code as i make the components

import random, math

#Functions go here
def intcheck(question,low = None,high = None):
    valid = False
    # Error messages
    if low is not None and high is not None: # Error message if variables are given
        error = "Please enter a whole number between {} and {} (Inclusive) ".format(low,high)
    elif low is not None and high is None: # Error message if only low variable is given
        error = "Please enter a whole number equal to or above {} ".format(low)
    elif low is not None and high is None: # Error message if only high variable is given
        error = "Please enter a whole number equal to or below {} ".format(high)
    else: # Error message if no variables are given
        error = "please enter a whole number"


    while not valid:
        try:
            # Gets user input
            response = int(input(question.format(low, high)))
            # Checks number is not too low
            if low is not None and response < low:
                print(error) # If its too low  display error
                continue
            # Checks number is not too high
            if high is not None and response > high:
                print(error) # If it is too high print error
                continue

            return response
        # If input is not a number or is a decimal then display error
        except ValueError:
            print(error)
            print()

def GuessCalc(high,low):
    range = high - low + 1
    max_raw = math.log2(range)  # gets maximum number of guesses using binary search
    max_upped = math.ceil(max_raw)  # Rounds up max_raw
    max_guesses = max_upped + 1  # Gives the user an extra guess incase they mess up
    return max_guesses

#Main routine goes here
rounds = intcheck("How many rounds do you want to play?: ",1)# Asks how many rounds user wants to play
rounds_played = 0

while rounds_played < rounds:
    rounds_played += 1 # This round has started so add 1 to how many rounds are played
    print("Rounds played: {}".format(rounds_played)) # Display how many rounds played to the user
    low_num = intcheck("What do you want the lowest number to be: ") # Gets lowest number from the user
    high_num = intcheck("What do you want the highest number to be: ".format(low_num),low_num) # Gets the highest number from the user
    max_guesses = GuessCalc(high_num,low_num)
    random_num = random.randint(low_num, high_num)  # Generates random number
    guess = intcheck("What is your guess: ",low_num,high_num) # Gets user guess between low number and high number





