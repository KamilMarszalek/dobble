# Dobble Game Project Documentation
## Author: Kamil Marszałek

## Overview
My assignment was to implement Dobble Game. I had to enable user to choose:
* how many computer player's to play with (from 1 to 3), 
* what difficulty level (from 1 to 3),
* how many symbols should be on a card (from 3 to 8).
Cards should be generated according to Dobble Game algorithm.
Game begins with shuffling and dealing.
Also one card is chosen to be middlecard.
Instead of using images I decided to use numbers in polish.
User have to write a common symbol or click on it depending on which gamemode he choosed:
* terminal version (main.py)
* pygame version (ui_pygame.py)
Computer players automatically after appropriate amount of time put their card on the middlecard.
Game ends when one of the players runs out of cards.

## Classes

### Card
Class Card represents a single card. It contains symbols which are on a card. It has a method to shuffle symbols on a card and methods to draw the card.
It also has an event handler which is called when on of the symbols is clicked.

### Player
Class Player represents a user. It holds a collection of his cards which was given to him during dealing. It has a method to remove card. Also to check if he has won and returning first card 
of his pack.

### Computer
Class Computer represents a computer player in the game.
It inherits from class Player. Additionaly it holds a name (id) of the computer player in order to make computers distinguishable. It has a method to find common symbol between given card and first card in the pack.

### Game
Class Game represents a whole game of dobble.
It handles every element of the game.
Calling play method enables to play in the terminal.
It holds:
* amount of computer players
* difficulty level
* number of symbols.
During initialization there is verification of the given parameters.
It also has method to set timeout according to difficulty level.
There is also a method to create cards which are being shuffled.
After creating cards the cards are being dealt.
It also has methods to choose winner from computer players if user fails.

### Menu
Class Menu represents the Dobble game menu. The menu is created using Tkinter package.

### DobbleGame
Class DobbleGame represents a whole game of dobble in pygame.
It uses methods of class Game to run the game in pygame.
It has methods display a message, draw cards, handle events. 

## Instruction
In order to play terminal version run main.py, but it is crucial to use Unix terminal.
In order to play pygame version run ui_pygame.py you have to setup virtual environment using file 
requirements.txt.
Tkinter module should be installed with python.



