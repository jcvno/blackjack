#!/usr/bin/python
# -----------
# Blackjack
#
# Cards are represented as strings labeled as their rank and suit
# Examples: "7H" - 7 Hearts
#			"TS" - 10 Spades
#
#
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

# Return the sum of the ranks in a hand
# Face cards are of rank 10
# Aces are of rank 11 or 1
def rank(hand):
	# Extract all ranks from hand
	ranks = [10 if r == 'T' or r == 'J' or r =='Q' or r == 'K' else
			11 if r == 'A' else
			int(r) for r,s in hand]

	# While there are 11-ranked Aces in hand and hand rank is greater than 21,
	while 11 in ranks and sum(ranks) > 21:
		# Change rank of Aces to 1
		# one Ace at a time
		# until hand rank is less than 21
		# or until there are no more 11-ranked Aces
		index = ranks.index(11)
		ranks[index] = 1
	return sum(ranks)

# Print cards on screen
# If player's turn, then hide dealer's first card
def showCards(dealer,player,turn="player"):
	print "Dealer Cards:", rank(dealer) if turn is "dealer" else ""
	for card in dealer[::-1]:
		if card is dealer[0] and turn is "player":
			card = "--"
		print card,
	print 
	print "Player Cards:", rank(player)
	for card in player:
		print card,

	# Check blackjack
	if turn is "player" and rank(dealer) == 21:
		return "lose"
	return None

def blackjack():
	return
	
def main():
	deck = initDeck(1)
	dealer, player = [], []

	# Deal cards by appending cards to list
	dealer.append(deal(deck))
	dealer.append(deal(deck))
	player.append(deal(deck))
	player.append(deal(deck))

	blackjack.turn = "player"
	while blackjack.turn == "player":
		blackjack.status = showCards(dealer,player,blackjack.turn)
		if blackjack.status == "lose":
			print "Dealer got blackjack!"
			showCards(dealer,player,"dealer")
			return
		choice = raw_input("\nhit or stand? ")

		if choice == "hit":
			player.append(deal(deck))

		elif choice == "stand":
			blackjack.turn = "dealer"


if __name__ == "__main__":
	main()

