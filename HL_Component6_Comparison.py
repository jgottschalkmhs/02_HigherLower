# HL Component 6 - Comparing the users guess to the secret number

correct_guess = False
secret_num = int(input("Secret number: "))
while correct_guess is False:
    guess = int(input("Guess: "))
    if guess < secret_num:
        print("Higher")
    elif guess > secret_num:
        print("Lower")
    else:
        print("Congratulations, You got it right")
        correct_guess = True