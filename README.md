Blackjack
=========

This is a simple text-based Python program of the game Blackjack (http://en.wikipedia.org/wiki/Blackjack), developed for a coding challenge from the 2014 Insight Data Engineering Fellows Program application.

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
* Double Down
	- Double bet and pass turn after dealer deals another card
	
Currently, only "Hit", "Stand", and "Double Down" actions are available. Advanced actions such as "Splitting" may be developed in a later version.

## Winnings
* Blackjack
	- 3:2 payout
* Win
	- 2:1 payout
* Push
	- 0 payout
* Lose
	- Lose bet

# Unit Testing
The module `test.py` contains various testing statements to assert the correctness of the different methods of the `blackjack.py` module.
