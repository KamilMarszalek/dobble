# Dobble Game Project Documentation
# Author: Kamil Marszałek

## Overview
My assignment was to implement Dobble Game. I had to enable user to choose:
* how many computer player's to play with (from 1 to 3), 
* what difficulty level from(1 to 3),
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


