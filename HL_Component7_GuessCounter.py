# HL Component 7 - Get maximum amount of guesses. If user guesses over the limit say that they have run out of guesses.
#                  Also say how many guesses user has left after each guess

correct_guess = False

max_guesses = int(input("Max guesses: "))
guesses = 0
while guesses < max_guesses:
    guess = int(input("Guess: "))
    guesses += 1
    guesses_left = max_guesses - guesses
    if guesses_left >= 1:
        print("You have {} guesses left".format(guesses_left))
    else:
        print("you have run out of guesses")