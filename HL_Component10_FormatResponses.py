# HL Component 8 - Makes sure that the user cant guess the same thing twice


# Functions go here
def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char * len(statement))
    print()


# Main routine goes here
rounds = int(input("How many rounds?: "))
max_guesses = int(input("Max guesses: "))
secret_num = int(input("Secret Number:"))

num_won = 0
rounds_played = 0
already_guessed = []
while rounds_played < rounds:
    rounds_played += 1 # This round has started so add 1 to how many rounds are played
    round_statement = hl_statement("*** Round 1 ***","*")
    guesses_left = max_guesses
    guess = 0
    while guesses_left >= 1 and guess != secret_num:
        guess = int(input("Guess: "))


        if guess in already_guessed:
            guessed_statement = hl_statement("-- You Have already guessed this number | {} Guess left --".format(guesses_left), "-")
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guess < secret_num:
            too_low = hl_statement("^^ Higher | {} guesses left ^^".format(guesses_left),"^")
        elif guess > secret_num:
            too_high = hl_statement("vv Lower | {} guesses left vv".format(guesses_left), "v")
        else:
            congratulations = hl_statement("!! Congratulations, you got it right in {} guesses !!".format(max_guesses - guesses_left),"!")
            num_won += 1




