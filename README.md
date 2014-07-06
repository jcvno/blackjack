Blackjack
=========

This is a simple Python program of the game Blackjack (http://en.wikipedia.org/wiki/Blackjack), developed for a coding challenge from the 2014 Insight Data Engineering Fellows Program application.

# Usage
Simply download the source and run in the Python interpreter

`python blackjack.py`

# Gameplay
Single player begins with 100 chips and plays against the dealer. Game first prompts the player how many decks to use. Cards are recycled and deck is shuffled after every round.

Player will be asked to place a bet of at least one (1) chip. Once bet is place, the round starts and the dealer deals out the cards and appropriately checks for Blackjack. Once the round has begun, the player will have the option to either Hit or Stand.

When the player stands, or gets 21, the dealer will play its turn. There is a small one (1) second delay so the player can keep track of every move.

## Menu
* Play
	- Play a new hand of Blackjack
* Change # of decks
	- Change number of decks to use
* Exit
	- Exit/Quit the program

## Blackjack Menu
* Hit
	- Dealer deals you another card
* Stand
	- Pass the turn to the dealer
	
Currently, only "Hit" and "Stand" actions are available. Advanced actions such as "Double Down" and "Splitting" may be developed in a later version.

## Winnings
* Blackjack
	- Winnings total 2.5 times player bet
* Win
	- Winnings total 2 times player bet
* Push
	- Winnings total 1 times player bet
* Lose
	- Winnings total 0
