Blackjack
=========

This is a simple text-based Python program of the game Blackjack (http://en.wikipedia.org/wiki/Blackjack), developed for a coding challenge from the 2014 Insight Data Engineering Fellows Program application.

# Usage
Simply download the source and run in your favorite Python interpreter, e.g. run from terminal:

`$ python blackjack.py`

# Gameplay
Single player begins with 100 chips and plays against the dealer. Game first prompts the player how many decks to use. Cards are recycled and deck is shuffled after every round.

Available chips will be rounded to the nearest tenth. The player will be asked to place a bet of at least one (1) chip, also rounded to the nearest tenth. Once bet is place, the round starts and the dealer deals out the cards and appropriately checks for Blackjack. Once the round has begun, the player will have the option to either Hit, Stand, or Double Down (when appropriate).

When the player stands, or gets 21, the dealer will play its turn. The dealer follows the soft 17 rule, which means that the dealer will keep hitting until its gets 17 or greater, even if it's a soft 17 (e.g. 'AH', '6S'). There is a small two (2) second delay so the player can keep track of every move.

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
	- Double Down is only available at the beginning of the round, if player has enough chips
	
Currently, only "Hit", "Stand", and "Double Down" actions are available. Advanced actions such as "Splitting" may be developed in a later version.

## Winnings
* Blackjack
	- 3:2 payout
* Win
	- 2:1 payout
* Push
	- 1:1 payout
* Lose/Bust
	- Lose bet

Available chips are rounded to the nearest tenth.

## Gameflow
Psuedo code gameflow algorithm

```
chips = 100 # Single player starts with 100 chips
while there are still chips available:
	play blackjack:
		place bet
		deal cards
		check for blackjack
		player's turn
		dealer's turn
		compare hands
		calculate and receive payout
```

# Unit Testing
The module `test.py` contains various testing statements to assert the correctness of the different methods of the `blackjack.py` module.

# Comments
I decided to write this program using Python 2.7.5, so I can further practice and sharpen my Python developing skills.