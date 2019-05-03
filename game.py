# Wilson Burchenal
# Game class and model for major game functions


import pickle
import os
import random
import collections


class Game():
	""" Core game object """
	target = ''
	guesses = ''
	incorrect = 0
	correct = 0
	gameover = False
	won = False
	username = ''


	def start_game(self, name):
		""" Initializes variables and picks random word from given word list """
		self.guesses = ''
		self.incorrect = 0
		self.correct = 0
		self.gameover = False
		self.won = False
		self.username = name

		word_list = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']
		self.target = word_list[random.randint(0, 5)]

	def construct_target(self):
		""" Constructs target string based on prior guesses. Also tallies correct guesses """
		target_string = ''
		self.correct = 0

		for i in self.target:
			if i in self.guesses:
				target_string += i
				self.correct += 1
			else:
				target_string += '_'

		return target_string

	def construct_block(self):
		""" Creates ASCII display block based on number of incorrect guesses """
		switch = {
			0:  """
			|------|
			|      |
			|
			|
			|
				""",
			1:  """
			|------|
			|      |
			|      O
			|
			|
				""",
			2:  """
			|------|
			|      |
			|      O
			|      |
			|
		 		""",
			3:  """
			|------|
			|      |
			|      O
			|     -|-
			|
		 		""",
			4:  """
			|------|
			|      |
			|      O
			|     -|-
			|     /
		 		""",
			5:  """
			|------|
			|      |
			|      O
			|     -|-
			|     / \\
		 		"""
		}
		block = switch[self.incorrect]
		return block

	def make_guess(self, guess):
		""" Makes sure that guess is kosher and returns string based on outcome of guess """
		guess = guess.lower()

		if len(guess) != 1:
			return "Please enter one letter at a time."

		if guess in self.guesses:
			return "You have already guessed that. Try another letter."

		self.guesses += guess
		if guess not in self.target:
			self.incorrect += 1
			return "Guess incorrect :("
		else:
			return "Guess correct!"

	def check_status(self):
		""" Checks for win/loss conditions """
		if self.incorrect >= 5:
			self.gameover = True
			return '\nYou ran out of guesses! Better luck next time.\n'
		elif self.correct >= len(self.target):
			self.gameover = True
			self.won = True
			return '\nCongratulations you won this game of Hangman!!!\n'
		else:
			return ""


def save_score(name):
	""" Saves score to file on disk. Score based on number of wins per username """
	if os.path.getsize("score_history.pkl") > 0:
		with open("score_history.pkl", "rb") as history:
			scores = pickle.load(history)

		if name in scores:
			scores[name] = scores[name]+1
		else:
			scores[name] = 1

		sorted_temp = sorted(scores.items(), key=lambda kv: kv[1])
		sorted_temp.reverse()
		sorted_scores = collections.OrderedDict(sorted_temp)
		with open("score_history.pkl", "wb") as history:
			pickle.dump(sorted_scores, history)

	else:
		scores = {name: 1}
		with open("score_history.pkl", "wb") as history:
			pickle.dump(scores, history)


def get_scores():
	""" Retrieves scores """
	if os.path.getsize("score_history.pkl") > 0:
		with open("score_history.pkl", "rb") as history:
			scores = pickle.load(history)

	return str(scores).strip("OrderedDict")
