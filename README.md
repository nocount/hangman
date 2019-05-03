# Hangman Game

## Hangman Coding Assignment for 3dHubs interview process. Instructions will follow.

This is my simple implementation of a Hangman game for a programming assignment. It is playable two ways, either through the command line or through simple API calls. 


# Instructions

### CLI version:
Simply run **main.py** and follow the ingame prompts

### API version:
Start **app.py** and then make http requests to localhost:5000
First you need to make a start game request by passing in your username and then you can make guesses **(Examples Below)**

Purpose of the game is to guess the word that is signified by the underscores. Each underscore represents a separate letter. You get 5 guesses to guess all of the letters. Each incorrect guess will cause a strike and part of the figure on the gallows will be filled in. Once it is completely full you have lost the game.

# API Endpoints

**game_request**
Path: /hangman/newgame
Method: POST
Parameters: name
Example: curl -X POST http://localhost:5000/hangman/newgame -H "Content-Type: application/json" -d '{"name":"Wil"}'

**post_guess**
Path: /hangman/makeguess
Method: POST
Parameters: guess
Example: curl -X POST http://localhost:5000/hangman/makeguess -H "Content-Type: application/json" -d '{"guess":"a"}'

**get_highscores**
Path: /hangman/highscores
Method: GET
Example: curl -X GET http://localhost:5000/hangman/highscores



# Improvements still to be made:

Create start menu so both versions can be kicked off from one place / see highcores
Add gameid so multiple games can be played simultaneously
Settings like number of guesses, difficulty of words, etc.
Increase number of guessable words