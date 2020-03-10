# HL Component 8 - Makes sure that the user cant guess the same thing twice



max_guesses = int(input("Max guesses: "))
guesses = 0
already_guessed = []
while guesses < max_guesses:
    guess = int(input("Guess: "))
    if guess in already_guessed:
        print("You have guessed this number already, please try again")
        continue
    guesses += 1
    already_guessed.append(guess)
    guesses_left = max_guesses - guesses

    if guesses_left >= 1:
        print("You have {} guesses left".format(guesses_left))
    else:
        print("you have run out of guesses")