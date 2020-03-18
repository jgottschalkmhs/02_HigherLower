# HL Complete program
# Im putting together the code as i make the components
import math
import random


# Functions go here
def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char * len(statement))
    print()


def intcheck(question, low=None, high=None):
    valid = False
    # Error messages
    if low is not None and high is not None:  # Error message if variables are given
        error = "Please enter a whole number between {} and {} (Inclusive) ".format(low, high)
    elif low is not None and high is None:  # Error message if only low variable is given
        error = "Please enter a whole number equal to or above {} ".format(low)
    elif low is not None and high is None:  # Error message if only high variable is given
        error = "Please enter a whole number equal to or below {} ".format(high)
    else:  # Error message if no variables are given
        error = "please enter a whole number"

    while not valid:
        try:
            # Gets user input
            response = int(input(question.format(low, high)))
            # Checks number is not too low
            if low is not None and response < low:
                print(error)  # If its too low  display error
                continue
            # Checks number is not too high
            if high is not None and response > high:
                print(error)  # If it is too high print error
                continue

            return response
        # If input is not a number or is a decimal then display error
        except ValueError:
            print(error)
            print()


def guess_calc(high, low):
    given_range = high - low + 1
    max_raw = math.log2(given_range)  # gets maximum number of guesses using binary search
    max_upped = math.ceil(max_raw)  # Rounds up max_raw
    max_guesses = max_upped + 1  # Gives the user an extra guess incase they mess up
    return max_guesses


# Main routine goes here
rounds = intcheck("How many rounds do you want to play?: ", 1)  # Asks how many rounds user wants to play
rounds_played = 0  # Counts rounds played

num_won = 0  # Counts rounds won
game_stats_guesses = []  # Stores the guesses in each round
game_stats_winsloss = []  # Store whether they won or lost a round

# Gets range for secret number from the user
low_num = intcheck("What do you want the lowest number to be: ")  # Gets lowest number from the user
# Gets the highest number from the user
high_num = intcheck("What do you want the highest number to be: ".format(low_num), low_num)

while rounds_played < rounds:

    print()  # separates each round

    rounds_played += 1  # This round has started so add 1 to how many rounds are played
    already_guessed = []  # List that contains all guesses in this round

    round_statement = hl_statement("*** Round {} ***".format(rounds_played), "*")  # Display what round the user is on

    # Round setup
    maximum_guesses = guess_calc(high_num, low_num)  # Generates the max number of guesses
    secret_num = random.randint(low_num, high_num)  # Generates random number
    guesses_left = maximum_guesses  # Sets amount of guesses fo the user
    print("You have a max of {} guesses".format(guesses_left))  # Tells user their max amount of guesses

    guess = ""
    # loops question until user runs out of guess or gets it right
    while guesses_left >= 1 and secret_num != guess:
        # Gets user guess between low number and high number
        guess = intcheck("What is your guess: ", low_num, high_num)

        # Checks if user has guessed the number before if the user has it loops the question.
        if guess in already_guessed:
            guessed_statement = hl_statement("-- You Have already guessed this number | {} Guess left --".format(guesses_left), "-")
            continue

        guesses_left -= 1 # Takes one guess away from how many guesses user has left
        already_guessed.append(guess)  # Adds the current guess to the list of already_guessed above

        if guesses_left >= 1:  # Compares users guess to the secret number and gives appropriate feedback
            if guess < secret_num:  # If guess is lower than secret number tell user to go higher
                if guesses_left > 1:
                    too_low = hl_statement("^^ Higher | {} guesses left ^^".format(guesses_left), "^")  # Feedback
                else:
                    too_low = hl_statement("^^ Higher | {} guess left ^^".format(guesses_left), "^")   # Grammatically correct feedback for only one guess

            elif guess > secret_num:  # If guess is higher than secret number tell user to go lower
                if guesses_left > 1:
                    too_high = hl_statement("vv Lower | {} guesses left vv".format(guesses_left), "v")  # Feedback
                else:
                    too_high = hl_statement("vv Lower | {} guess left vv".format(guesses_left), "v")  # Grammatically correct feedback for only one guess
            elif guess == secret_num:  # if user gets it right then congratulate them
                if guesses_left == maximum_guesses - 1:
                    congratulations = hl_statement("!! Amazing, you got it right in 1 guess !!", "!")
                else:
                    congratulations = hl_statement("!! Congratulations, you got it right in {} guesses !!".format(maximum_guesses - guesses_left), "!")

                num_won += 1
                game_stats_winsloss.append("win")
        # Displays the "you lose" messages
        if guesses_left < 1 and guess != secret_num:
            lose_statement = hl_statement("|| you ran out of guesses ||", "|")
            game_stats_winsloss.append("loss")


    game_stats_guesses.append(maximum_guesses - guesses_left)  # Stores how many guesses this round took
    round_summary = hl_statement("| Won: {} | Lost: {} |".format(num_won, rounds_played - num_won), "-") # Displays a round summary

# After all rounds are finished show an end game summary

print("*** Game Statistics ***")
print("Round #  |Guesses  |Win/Lose   |")
list_count = 0
for item in game_stats_guesses:
    if game_stats_winsloss[list_count] == "win":
        print("Round {}  |{}        |{}        |".format(list_count + 1, game_stats_guesses[list_count],  game_stats_winsloss[list_count]))
    if game_stats_winsloss[list_count] == "loss":
        print("Round {}  |{}        |{}       |".format(list_count + 1, game_stats_guesses[list_count],  game_stats_winsloss[list_count]))

    list_count += 1

game_stats_guesses.sort()
best_round = game_stats_guesses[0]
worst_round = game_stats_guesses[-1]
average_round = sum(game_stats_guesses)/len(game_stats_guesses)

print()
print("*** Summary ***" )
print("Best Score: {}".format(best_round))
print("Worst Score: {}".format(worst_round))
print("Average Score: {:.2f}".format(average_round))
