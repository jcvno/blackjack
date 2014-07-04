#!/usr/bin/python
# -----------
# Blackjack
#

import random


# This builds a deck of 52 * numDecks cards
def initDeck(numDecks):
	deck = [r+s for r in '23456789TJQKA'*numDecks for s in 'SHDC']
	random.shuffle(deck)
	return deck

# Pops and returns the first card in deck
def deal(deck):
	card = deck[0]
	del deck[0]
	return card

# Print cards on screen
# If player's turn, then hide dealer's first card
def showCards(dealer,player,turn="player"):
	print "Dealer Cards:"
	for card in dealer[::-1]:
		if card is dealer[0] and turn is "player":
			card = "--"
		print card,
	print 
	print "Player Cards:"
	for card in player:
		print card,

	
def main():
	deck = initDeck(1)
	dealer, player = [], []

	# Deal cards by appending cards to list
	dealer.append(deal(deck))
	dealer.append(deal(deck))
	player.append(deal(deck))
	player.append(deal(deck))

	showCards.turn = "player"
	while showCards.turn == "player":
		showCards(dealer,player,showCards.turn)
		
		showCards.turn = "dealer"


if __name__ == "__main__":
	main()

