# Rounds system and counter

# To do
#  - loop for amount of rounds
#  - store amount of rounds played as a variable so it can be displayed later


rounds = int(input("How many rounds?: ")) # Get how many rounds the user wants to play
rounds_played = 0

while rounds_played < rounds:
    rounds_played += 1 # This round has started so add 1 to how many rounds are played
    print("Rounds played: {}".format(rounds_played)) # Display how many rounds played to the user
print("End of game") # Tell the user the game has ended