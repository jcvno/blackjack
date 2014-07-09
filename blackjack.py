#!/usr/bin/python

# Copyright 2014 Justin Cano
#
# This is a simple Python program of the game Blackjack
# (http://en.wikipedia.org/wiki/Blackjack), developed for
# a coding challenge from the 2014 Insight Data Engineering
# Fellows Program application.
#
# Licensed under the GNU General Public License, version 2.0
# (the "License"), this program is free software; you can
# redistribute it and/or modify it under the terms of the
# License.
#
# You should have received a copy of the License along with this
# program in the file "LICENSE". If not, you may obtain a copy of
# the License at
#	http://www.gnu.org/licenses/gpl-2.0.html
#
import random
import time

MAX_DECKS = 8

def shuffleDeck(numDecks):
	"""
	Builds, shuffles, and returns a deck of 52 * numDecks cards
	Deck is represented as a list of cards
	Cards are represented as strings labeled as their rank and suit, e.g.
	'7H' - 7 Hearts
	'TS' - 10 Spades
	"""
	deck = [r+s for r in '23456789TJQKA'*numDecks for s in 'SHDC']
	random.shuffle(deck)
	return deck

def changeNumDecks():
	"""
	Prompts user to change the number of decks to use
	Returns new number of decks to use
	"""
	numDecks = 0
	while numDecks <= 0 or numDecks > MAX_DECKS:
		try:
			print "Enter number of decks to use (1-" + str(MAX_DECKS) + "):"
			numDecks = int(raw_input("% "))
			assert 0 < numDecks <= MAX_DECKS
		except (ValueError, AssertionError):
			print "Invalid input! Must be integer value greater than 0"
			print "and less than 8"
	return numDecks

def placeBet(chips):
	"""
	Prompts user for bet value
	User input must be greater than 0 and less than chips
	Fixed bet precision to one decimal place
	Returns bet, rounded to nearest tenth
	"""
	bet = 0
	while bet < 1 or bet > chips:
		try:
			print "How much do you wanna bet (1-" + str(chips) + ")?"
			# Round bet to the nearest tenth
			bet = round(float(raw_input("% ")),1)
			assert 1 <= bet <= chips
		except (ValueError, AssertionError):
			print "Invalid input! Must be integer or float value at least 1"
			print "and less than the number of available chips"
	return bet

menuChoices = ['', "PLAY", "DECK", "EXIT"]
def menu():
	"""
	Menu
	Prompts the user to choose menu option:
	1 - Play
	2 - Change # of decks
	3 - Exit
	Returns user selection
	"""
	choice = 0
	maxChoice = len(menuChoices)-1
	while choice <= 0 or choice > maxChoice:
		try:
			print "Menu"
			print "-" * 10
			print "[1] Play"
			print "[2] Change # Decks"
			print "[3] Exit"
			choice = int(raw_input("% "))
			assert 1 <=choice <= maxChoice
		except (ValueError, AssertionError):
			print "Invalid choice! Must be [1-" + str(maxChoice) + "]"
	return menuChoices[choice]

blackjackChoices = ['', "HIT", "STAND", "DOUBLE"]
def blackjackMenu(playerCards, chips, bet):
	"""
	Prompts user to choose Blackjack option:
	1 - Hit
	2 - Stand
	3 - Double Down (uses playerCards, chips, and
		bet to determine if player can Double Down)
	Can be extended for advanced options, i.e. split
	Returns user selection
	"""
	choice = 0
	maxChoice = len(blackjackChoices)-2
	while choice <= 0 or choice > maxChoice:
		try:
			print "Actions:"
			print "-" * 10
			print "[1] Hit"
			print "[2] Stand"
			if len(playerCards) == 2 and chips >= bet:
				"Double Down allowed"
				print "[3] Double Down"
				maxChoice += 1
			choice = int(raw_input("% "))
			assert 1 <= choice <= maxChoice
		except (ValueError, AssertionError):
			print "Invalid choice! Must be [1-" + str(maxChoice) + "]"
	return blackjackChoices[choice]

def deal(deck):
	"""
	Pops and returns the first card in deck
	"""
	card = deck[0]
	del deck[0]
	return card

def rank(hand):
	"""
	Return the sum of the ranks in a hand
	Face cards are of rank 10
	Aces are of rank 11 or 1
	Example: rank(['7H','AS','JD']) => 18
	"""
	# Extract all ranks from hand
	ranks = [10 if r == 'T' or r == 'J' or r =='Q' or r == 'K' else
				11 if r == 'A' else
				int(r) for r,s in hand]

	# While there are 11-ranked Aces in hand and hand rank is greater than 21,
	while 11 in ranks and sum(ranks) > 21:
		"""
		Change rank of Aces to 1
		one Ace at a time
		until hand rank is less than 21
		or until there are no more 11-ranked Aces
		"""
		index = ranks.index(11)
		ranks[index] = 1
	return sum(ranks)

def showCards(dealer, player, turn="player"):
	"""
	Print cards on screen
	If player's turn, hide dealer's second card and rank
	"""
	print "=" * 20
	print "Dealer Cards:", rank([dealer[0]]) if turn is "player" else rank(dealer)
	for card in dealer:
		if card is dealer[1] and turn is "player":
			card = "--"
		print card,
	print
	print "Player Cards:", rank(player)
	for card in player:
		print card,

	print
	print "=" * 20

def getPayout(dealer, player, chips, bet):
	"""
	Evaluates and compares dealer and player hands
	Calculates winnings and adds to chips
	Fixed chips precision to one decimal place
	Returns chips rounded to nearest tenth
	"""
	if rank(player) > 21:
		"Player bust"
		print "Bust!"
	elif rank(dealer) == rank(player):
		"Push"
		chips += bet
		print "Push"
	elif rank(player) == 21 and len(player) == 2:
		"Player gets Blackjack"
		chips += 2.5*bet
		print "You got Blackjack!"
	elif rank(dealer) > 21 or rank(player) > rank(dealer):
		"Dealer bust or player beats dealer"
		chips += 2*bet
		print "You win!"
	else:
		"Dealer beats player"
		print "You lose!"

	return round(chips,1)

def blackjack(deck,chips):
	"""
	Play a round of (single player) Blackjack
	using deck and chips. Player will be ask to
	enter a valid bet value. Payout will be added
	to available chips.
	Return chips after payout.
	"""
	print "*" * 50
	print "Chips:", chips
	bet = placeBet(chips)
	print "*" * 50
	chips = chips - bet
	print "Chips:", chips
	print "Bet:", bet

	dealerCards, playerCards = [], []
	dealerRank, playerRank = 0, 0

	# Deal starting cards by appending the
	# first card from deck to list
	playerCards.append(deal(deck))
	dealerCards.append(deal(deck))
	playerCards.append(deal(deck))
	dealerCards.append(deal(deck))

	# Player goes first
	blackjack.turn = "player"

	if rank(dealerCards) == 21:
		"Check for dealer Blackjack"
		showCards(dealerCards, playerCards, "dealer")
		print "\nDealer got blackjack!"
		blackjack.turn = None
	elif rank(playerCards) == 21:
		"Check player for Blackjack"
		showCards(dealerCards, playerCards)
		blackjack.turn = None
	else:
		showCards(dealerCards, playerCards)

	while blackjack.turn is "player":
		"Player's turn"
		choice = blackjackMenu(playerCards, chips, bet)

		if choice == "HIT":
			playerCards.append(deal(deck))
		elif choice == "STAND":
			blackjack.turn = "dealer"
			break
		elif choice == "DOUBLE":
			print "Double Down! Good luck!"
			chips = chips - bet
			print "Chips:", chips
			bet = 2*bet
			print "Bet:", bet
			playerCards.append(deal(deck))
			showCards(dealerCards, playerCards)
			time.sleep(2)
			blackjack.turn = "dealer"

		if choice != "DOUBLE":
			showCards(dealerCards, playerCards)
		playerRank = rank(playerCards)

		if playerRank > 21:
			"Bust"
			blackjack.turn = None
		elif playerRank == 21:
			"Twenty-One"
			print "\nYou got 21!"
			# Pause so player notices 21
			time.sleep(1)
			blackjack.turn = "dealer"

	print

	while blackjack.turn is "dealer":
		"Dealer's turn"
		showCards(dealerCards, playerCards, blackjack.turn)
		dealerRank = rank(dealerCards)

		if dealerRank > 21:
			print "\nDealer busts!"
			blackjack.turn = None
		elif dealerRank < 17:
			print "\nDealer hits"
			dealerCards.append(deal(deck))
		else:
			blackjack.turn = None

		# Pause between dealer moves so player can see dealer's actions
		time.sleep(1)

	# Compare hands and update available chips
	chips = getPayout(dealerCards, playerCards, chips, bet)
	time.sleep(1.5)
	print
	return chips

def main():
	chips = 100
	numDecks = changeNumDecks()
	choice = ''

	while chips > 0:
		"""
		While there are still chips available to bet,
		give the player the option to keep playing
		"""
		print "*" * 50
		print "Chips:", chips

		while choice != "PLAY":
			"Display menu"
			choice = menu()
			if choice == "DECK":
				numDecks = changeNumDecks()
				print "Changed # of decks to:", numDecks
			elif choice == "EXIT":
				print "\nCashing out with", chips, "chips..."
				print "Thanks for playing!\n"
				return

		deck = shuffleDeck(numDecks)
		chips = blackjack(deck,chips) # Play a game of blackjack
		choice = ''
		
	print "No more chips available"
	print "Thanks for playing!\n"

if __name__ == "__main__":
	print chr(27) + "[2J" # Clear screen
	print "*" * 50
	print """
		BLACKJACK
		by Justin Cano
		"""
	print "*" * 50
	main()