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

def ShuffleDeck(numDecks):
	"""
	Builds, shuffles, and returns a deck of 52 * numDecks cards
	Deck is represented as a list of cards
	Cards are represented as strings labeled as their rank and suit
	Examples: '7H' - 7 Hearts
			  'TS' - 10 Spades
	"""
	deck = [r+s for r in '23456789TJQKA'*numDecks for s in 'SHDC']
	random.shuffle(deck)
	return deck

def ChangeNumDecks():
	"""
	Prompts user to change the number of decks to use
	Returns new number of decks to use
	"""
	numDecks = 0
	while numDecks <= 0:
		try:
			numDecks = int(raw_input("Enter number of decks to use:\n% "))
			assert numDecks > 0
		except (ValueError, AssertionError):
			print "Invalid input! Must be integer value greater than 0"
	return numDecks

def GetBet(chips):
	"""
	Prompts user for bet value
	User input must be greater than 0 and less than chips
	Returns bet
	"""
	bet = 0
	while bet <= 0 or bet > chips:
		try:
			bet = float(raw_input("How much do you wanna bet?\n% "))
			assert bet > 0 and bet <= chips
		except ValueError:
			print "Invalid input! Must be integer or float value greater"
			print "than 0 and less than the number of available chips"
		except AssertionError:
			print "You don't have that many chips!"
	return bet

menuChoices = ['', "PLAY", "DECK", "EXIT"]
def Menu():
	"""
	Menu
	Prompts the user to choose menu option:
	1 - Play
	2 - Change # of decks
	3 - Exit
	Returns user selection
	"""
	choice = 0
	maxChoice = len(menuChoices)
	while choice <= 0 or choice >= maxChoice:
		try:
			print "Menu"
			print "-" * 10
			print "[1] Play"
			print "[2] Change # Decks"
			print "[3] Exit"
			choice = int(raw_input("% "))
			assert choice >= 1 and choice < maxChoice
		except (ValueError, AssertionError):
			print "Invalid choice! Must be [1-" + str(maxChoice-1) + "]"
	return menuChoices[choice]

blackjackChoices = ['', "HIT", "STAND"]
def BlackjackMenu():
	"""
	Prompts user to choose Blackjack option:
	1 - Hit
	2 - Stand
	Can be extended for advanced options, i.e. split, double
	Returns user selection
	"""
	choice = 0
	maxChoice = len(blackjackChoices)
	while choice <= 0 or choice >= maxChoice:
		try:
			print "Actions:"
			print "-" * 10
			print "[1] Hit"
			print "[2] Stand"
			choice = int(raw_input("% "))
			assert choice >= 1 and choice < maxChoice
		except (ValueError, AssertionError):
			print "Invalid choice! Must be [1-" + str(maxChoice-1) + "]"
	return blackjackChoices[choice]

def Deal(deck):
	"""
	Pops and returns the first card in deck
	"""
	card = deck[0]
	del deck[0]
	return card

def Rank(hand):
	"""
	Return the sum of the ranks in a hand
	Face cards are of rank 10
	Aces are of rank 11 or 1
	Example: Rank(['7H','AS','JD']) => 18
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

def ShowCards(dealer, player, turn="player"):
	"""
	Print cards on screen
	If player's turn, hide dealer's second card and rank
	"""
	print "=" * 20
	print "Dealer Cards:", Rank([dealer[0]]) if turn is "player" else Rank(dealer)
	for card in dealer:
		if card is dealer[1] and turn is "player":
			card = "--"
		print card,
	print
	print "Player Cards:", Rank(player)
	for card in player:
		print card,

	print
	print "=" * 20

def Blackjack(dealer, player, chips, bet):
	"""
	Evaluates and compares dealer and player hands
	Calculates winnings and adds to chips
	Returns chips
	"""
	# Player bust
	if Rank(player) > 21:
		print "Bust!"

	# Push
	elif Rank(dealer) == Rank(player):
		chips += bet
		print "Push"

	# Player gets Blackjack
	elif Rank(player) == 21 and len(player) == 2:
		chips += 2.5*bet
		print "You got Blackjack!"

	# Dealer bust or player beats dealer
	elif Rank(dealer) > 21 or Rank(player) > Rank(dealer):
		chips += 2*bet
		print "You win!"

	# Dealer beats player
	else:
		print "You lose!"

	return chips

def main():
	chips = 100
	numDecks = ChangeNumDecks()
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
			choice = Menu()
			if choice == "DECK":
				numDecks = ChangeNumDecks()
				print "Changed # of decks to:", numDecks
			elif choice == "EXIT":
				print "\nCashing out with", chips, "chips..."
				print "Thanks for playing!\n"
				return

		print "*" * 50
		print "Chips:", chips
		bet = GetBet(chips)
		print "*" * 50
		chips = chips - bet
		print "Chips:", chips
		print "Bet:", bet
		
		deck = ShuffleDeck(numDecks)
		dealerCards, playerCards = [], []
		dealerRank, playerRank = 0, 0

		# Deal cards by appending the first card from deck to list
		playerCards.append(Deal(deck))
		dealerCards.append(Deal(deck))
		playerCards.append(Deal(deck))
		dealerCards.append(Deal(deck))

		# Player goes first
		Blackjack.turn = "player"

		if Rank(dealerCards) == 21:
			"Check for dealer Blackjack"
			print "\nDealer got blackjack!"
			ShowCards(dealerCards, playerCards, "dealer")
			Blackjack.turn = None
		elif Rank(playerCards) == 21:
			"Check player for Blackjack"
			ShowCards(dealerCards, playerCards)
			Blackjack.turn = None
		else:
			ShowCards(dealerCards, playerCards)

		while Blackjack.turn is "player":
			"Player's turn"
			choice = BlackjackMenu()

			if choice == "HIT":
				playerCards.append(Deal(deck))
			elif choice == "STAND":
				Blackjack.turn = "dealer"
				break

			ShowCards(dealerCards, playerCards)
			playerRank = Rank(playerCards)

			if playerRank > 21:
				"Bust"
				Blackjack.turn = None
			elif playerRank == 21:
				"Twenty-One"
				print "\nYou got 21!"
				# Pause so player notices 21
				time.sleep(1)
				Blackjack.turn = "dealer"

		print

		while Blackjack.turn is "dealer":
			"Dealer's turn"
			ShowCards(dealerCards, playerCards, Blackjack.turn)
			dealerRank = Rank(dealerCards)

			if dealerRank > 21:
				print "\nDealer busts!"
				Blackjack.turn = None
			elif dealerRank < 17:
				print "\nDealer hits"
				dealerCards.append(Deal(deck))
			else:
				Blackjack.turn = None

			# Pause between dealer moves so player can see dealer's actions
			time.sleep(1)

		# Compare hands and update available chips
		chips = Blackjack(dealerCards, playerCards, chips, bet)
		choice = ''
		print

	print "No more chips available"
	print "Thanks for playing!\n"

print "*" * 50
print """
		BLACKJACK
		by Justin Cano
	"""
print "*" * 50
if __name__ == "__main__":
	main()