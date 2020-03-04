# HL Component 6 - Comparing the users guess to the secret number

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