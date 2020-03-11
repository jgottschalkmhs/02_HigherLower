# HL Component 8 - Makes sure that the user cant guess the same thing twice

rounds = int(input("How many rounds?: "))
max_guesses = int(input("Max guesses: "))
secret_num = int(input("Secret Number:"))

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    rounds_played += 1 # This round has started so add 1 to how many rounds are played
    guesses_left = max_guesses
    guess = 0
    while guesses_left >= 1 and guess != secret_num:
        guess = int(input("Guess: "))
        guesses_left -= 1

        if guess < secret_num:
            print("Higher")
        elif guess > secret_num:
            print("Lower")
        else:
            print("Congratulations, You got it right")
            num_won += 1

        if guesses_left >= 1 and guess != secret_num:
            print("You have {} guesses left".format(guesses_left))
        elif guess != secret_num:
            print("you have run out of guesses")
    print("Won: {} | Lost: {}".format(num_won, rounds_played - num_won))

