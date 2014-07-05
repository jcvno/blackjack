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
import time

# This builds a deck of 52 * numDecks cards
def initDeck(numDecks):
	deck = [r+s for r in '23456789TJQKA'*numDecks for s in 'SHDC']
	random.shuffle(deck)
	return deck

# Pops the first card in deck and appends to hand
# Return new hand
def deal(deck, hand):
	card = deck[0]
	del deck[0]
	hand.append(card)
	return hand

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
	print "*" * 20
	print "Dealer Cards:", rank(dealer) if turn is "dealer" else ""
	for card in dealer:
		if card is dealer[1] and turn is "player":
			card = "--"
		print card,
	print 
	print "Player Cards:", rank(player)
	for card in player:
		print card,

	print
	print "*" * 20

def blackjack(dealer, player):
	if rank(player) > 21:
		print "\nYou lose!"
	elif rank(dealer) > 21 or rank(player) > rank(dealer):
		print "\nYou win!"
	elif rank(dealer) == rank(player):
		print "\nDraw!"
	else:
		print "\nYou lose!"
	
def main():
	chips = 100
	numDecks = 1
	deck = initDeck(1)
	dealerCards, playerCards = [], []
	dealerRank, playerRank = 0, 0

	# Deal cards by appending cards to list
	dealerCards = deal(deck, dealerCards)
	dealerCards = deal(deck, dealerCards)
	playerCards = deal(deck, playerCards)
	playerCards = deal(deck, playerCards)

	blackjack.turn = "player"
	while blackjack.turn is "player":
		showCards(dealerCards,playerCards)
		dealerRank, playerRank = rank(dealerCards), rank(playerCards)

		if playerRank > 21:
			print "\nBust!"
			blackjack.turn = None
			break

		if dealerRank == 21:
			print "\nDealer got blackjack!"
			showCards(dealerCards,playerCards,"dealer")
			return

		try:
			choice = int(raw_input("\n1 - hit | 2 - stand\n"))
			assert choice >= 1 and choice <= 2

			if choice == 1:
				playerCards = deal(deck, playerCards)

			elif choice == 2:
				blackjack.turn = "dealer"
				
		except (ValueError, AssertionError):
			print "Invalid choice! Must be [1-2]"


		print "\n"

	while blackjack.turn is "dealer":
		showCards(dealerCards,playerCards,blackjack.turn)
		dealerRank, playerRank = rank(dealerCards), rank(playerCards)

		if dealerRank > 21:
			print "\nDealer busts!"
			blackjack.turn = None
		elif dealerRank < 17:
			print "\nDealer hits"
			dealerCards = deal(deck, dealerCards)
		else:
			blackjack.turn = None
		
		print "\n"
		time.sleep(.5)

	blackjack(dealerCards, playerCards)





if __name__ == "__main__":
	main()

