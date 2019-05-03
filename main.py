# Wilson Burchenal
# Main file for running the hangman game through CLI


import game


def run_new():
	""" Core function to run game in CLI. Calls Game methods """
	print("Welcome to a new game of Hangman\n")
	new_game = game.Game()
	username = input("Please enter your username\n")
	new_game.start_game(username)

	while 1:
		# Displaying ASCII block and target string
		print(new_game.construct_block()+"\n")
		print("Here is the word to guess:\n")
		print(new_game.construct_target())
		print("\nGuesses so far:")
		print(new_game.guesses)

		guess = input("Please guess a letter\n")
		print(new_game.make_guess(guess)+"\n")

		# Needed to calculate correct tally prior to checking win/loss conditions
		new_game.construct_target()

		print(new_game.check_status())
		if new_game.gameover:
			if new_game.won:
				print("Congratulations you have won the game of Hangman")
				game.save_score(username)
			else:
				print(new_game.construct_block()+"\n")
			break

	print("\nHighscores by number of wins: \n")
	print(game.get_scores() + "\n")



if __name__=='__main__':
	run_new()