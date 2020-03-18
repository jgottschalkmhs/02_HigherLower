# Summary Results

# Get results in each round and store in a list
# Display the score from each round and if they won the round or not
# Also show the users best round score , worst round score, and average score

# For this one hope to look for different ways to do it
# This one also has if they win or lose

game_stats_guesses = [3, 5, 7, 5, 5]
game_stats_winsloss = ["win", "loss", "win", "win", "loss"]
print("*** Game Statistics ***")
print("Round #  |Guesses Left  |Win/Lose   |")
list_count = 0
for item in game_stats_guesses:
    if game_stats_winsloss[list_count] == "win":
        print("Round {}  |{}             |{}        |".format(list_count, game_stats_guesses[list_count],  game_stats_winsloss[list_count]))
    if game_stats_winsloss[list_count] == "loss":
        print("Round {}  |{}             |{}       |".format(list_count, game_stats_guesses[list_count],  game_stats_winsloss[list_count]))

    list_count += 1

game_stats_guesses.sort()
best_round = game_stats_guesses[0]
worst_round = game_stats_guesses[-1]
average_round = sum(game_stats_guesses)/len(game_stats_guesses)

print()
print("*** Summary ***" )
print("Best Score: {}".format(best_round))
print("Worst Score: {}".format(worst_round))
print("Average Score: {}".format(average_round))