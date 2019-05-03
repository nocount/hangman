# Wilson Burchenal
# App server for API side of the hangman game. Runs separately from main.


from flask import Flask
from flask import request
from flask import abort
import game


app = Flask(__name__)

# Default game to be accessed by APIs
new_game = game.Game()


@app.route('/hangman/newgame', methods=['POST'])
def game_request():
	""" Post request for creating a new game. Username is only required parameter """
	if not request.json or 'name' not in request.json:
		abort(400)

	name = request.json['name']

	# Initializing game with random word from list and default values
	new_game.start_game(name)
	target = new_game.construct_target()
	res = "Welcome to a new game of Hangman " + name + ".\nHere is the word to guess:\n" + target +"\n\n"
	return res


@app.route('/hangman/makeguess', methods=['POST'])
def post_guess():
	""" Post request for making guesses to active game """
	if not request.json or 'guess' not in request.json:
		abort(400)

	# Constructing response based on outcome of users guess
	guess = request.json['guess']
	outcome = new_game.make_guess(guess)
	target = new_game.construct_target()
	prev_guess = "\nGuesses so far:\n" + new_game.guesses + "\n"
	block = new_game.construct_block()
	fin = new_game.check_status()

	# Checking if victory/loss conditions have been met and adjusting response
	if new_game.gameover:
			if new_game.won:
				game.save_score(new_game.username)
				res = "\nCongratulations you won this game of Hangman!!!\n\n"
			else:
				res = block + "\nYou ran out of guesses! Better luck next time.\n\n"
	else:
		res = outcome + "\n\n" + block + "\nHere is the word now: \n" + target + "\n\n" + prev_guess

	return res


@app.route('/hangman/highscores', methods=['GET'])
def get_highscores():
	""" Get request to return highscores """
	return game.get_scores()


if __name__ == '__main__':
    app.run(debug=True)
