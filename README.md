# Dobble Game Project Documentation
## Author: Kamil Marszałek

## Overview
My assignment was to implement <span style="color: red;"><b>Dobble Game</b></span>. I had to enable user to choose:
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
Class Card represents a single card. It contains symbols which are on a card.

### UICard
Class UICard has static methods to draw the card and handle clicking.
It was created to separate this functions from class Card. 

### Player
Class Player represents a user.
It holds a collection of his cards which was given to him during dealing.
Also it holds the name of the player.

### Computer
Class Computer represents a computer player in the game.
It inherits from class Player.

### Game
Class Game represents a whole game of dobble.
It handles every element of the game.
Calling play method enables to play in the terminal.

### Menu
Class Menu represents the Dobble game menu.
The menu is created using Tkinter package.

### DobbleGame
Class DobbleGame represents a whole game of dobble in pygame.
It uses methods of class Game to run the game in pygame.
It has methods display a message, draw cards, handle events. 

## Instruction
In order to play terminal version run main.py, but it is crucial to use Unix terminal.
In order to play pygame version run ui_pygame.py you have to setup virtual environment using file 
requirements.txt.
Tkinter module should be installed with python.

## Reflective part
I started creating my project on 25<sup>th</sup> November. 
Firstly I decided to make my game in the terminal.
The game was using only built-in packages:
* termios
* sys
* select
* random
After creating the first-prototype, 
I changed my mind and started working on
a gui version in the pygame module. 
I considered using images on the cards, 
but it seemed time-consuming to make 57 graphics.
So I used again the same dictionary with numbers in polish.
