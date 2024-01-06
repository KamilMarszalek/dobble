# Dobble Game Project Documentation
## Author: Kamil Marszałek

## Overview
My assignment was to implement <b>Dobble Game</b>. I had to enable the user to choose:
* how many computer players to play with (from 1 to 3), 
* what difficulty level (from 1 to 3),
* how many symbols should be on a card (from 3 to 8).
Cards should be generated according to Dobble Game algorithm.
Game begins with shuffling and dealing.
Also, one card is chosen to be middlecard.
Instead of using images, I decided to use numbers in Polish.
The user has to write a common symbol or click on it depending on which gamemode he chose:
* terminal version (main.py)
* pygame version (ui_pygame.py)
Computer players automatically after appropriate amount of time put their card on the middlecard.
Game ends when one of the players runs out of cards.

## Classes

### Card
Class Card represents a single card. It contains symbols on a card.

### UICard
Class UICard has static methods to draw the card and handle clicking.
It was created to separate these functions from class Card. 

### Player
Class Player represents a user.
It holds a collection of cards given to the player during dealing.
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
It has methods to display a message, draw cards, handle events. 

## Instruction
To play the terminal version, run main.py using a Unix terminal.
In order to play the pygame version, run ui_pygame.py. You have to set up a virtual environment using the requirements.txt file.
The Tkinter module should be installed along with Python.

## Reflective part
I began my project on November 25<sup>th</sup>. 
Firstly I decided to make my game in the terminal.
The game was using only built-in packages:
* termios
* sys
* select
* random

<br>
<p>After creating the first prototype, 
I changed my mind and started working on
a GUI version in the <u>pygame</u> module. 
I considered using images on the cards, 
but it seemed time-consuming to make 57 graphics.
So I used again the same dictionary with numbers in Polish.</p>
<p>After creating GUI version, I spotted an issue with starting the game,
it was still using the terminal to gather 
the information required to start the game.
Then I decided to make a GUI menu.
I chose the Tkinter module due to its simplicity.</p>
<p>After completing it, I began refactoring my code.
I managed to simplify it slightly.
After that I asked for a code review.
I got feedback that some parts of my code
had not been respecting SOLID principles 
and others had been hard to read.</p>
<p>The issues were related with Card and Player class.
I think that I managed to fix Card class,
but I do not have an idea how to fix the Player class.</p>
<p>I found it difficult to make a pack of cards for five or seven symbols, 
so I decided to create it in an approximate way. 
This might not exactly match Dobble rules. 
Using the standard way to generate symbols, 
some cards had no common symbol. 
Therefore, I think it is better to have two 
or maybe three common symbols on a card, 
ensuring that at least one common symbol 
is always present.</p>
