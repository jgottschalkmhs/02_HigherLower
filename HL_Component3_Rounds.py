# Rounds system and counter

# To do
#  - loop for amount of rounds
#  - store amount of rounds played as a variable so it can be displayed later

rounds = int(input("How many rounds?: "))
rounds_played = 0

while rounds_played < rounds:
    rounds_played += 1
    print("Rounds played: {}".format(rounds_played))
print("End of game")