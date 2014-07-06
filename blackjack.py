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

# Builds, shuffles, and returns a deck of 52 * numDecks cards
def initDeck(numDecks):
	deck = [r+s for r in '23456789TJQKA'*numDecks for s in 'SHDC']
	random.shuffle(deck)
	return deck

# Prompts user to change the number of decks to use
def changeNumDecks():
	numDecks = 0
	while numDecks <= 0:
		try:
			numDecks = int(raw_input("Enter number of decks to use: "))
			assert numDecks > 0
		except (ValueError, AssertionError):
			print "Invalid input! Must be integer value greater than 0"
	return numDecks

# Prompts user for bet value
# User input must be greater than 0 and less than chips
def getBet(chips):
	bet = 0
	while bet <= 0 or bet > chips:
		try:
			bet = float(raw_input("Enter desired bet: "))
			assert bet > 0 and bet <= chips
		except (ValueError, AssertionError):
			print "Invalid input! Must be integer or float value greater than 0 and less than the number of available chips"
	return bet

# Prompts user to choose Blackjack option:
# 1 - Hit
# 2 - Stand
# Can be extended for advanced options, i.e. split, double
blackjackChoices = ['',"HIT","STAND"]
def getChoice():
	choice = 0
	maxChoice = len(blackjackChoices)
	while choice <= 0 or choice >= maxChoice:
		try:
			choice = int(raw_input("1 - Hit | 2 - Stand\n% "))
			assert choice >= 1 and choice < maxChoice
		except (ValueError, AssertionError):
			print "Invalid choice! Must be [1-" + str(maxChoice-1) + "]"
	return blackjackChoices[choice]

# Menu
# Prompts the user to choose menu option:
# 1 - Play again
# 2 - Change # of decks
# 3 - Exit
menuChoices = ['',"PLAY","DECK","EXIT"]
def menu():
	choice = 0
	maxChoice = len(menuChoices)
	while choice <= 0 or choice >= maxChoice:
		try:
			choice = int(raw_input("1 - Play Again | 2 - Change # of Decks | 3 - Exit\n% "))
			assert choice >= 1 and choice < maxChoice
		except (ValueError, AssertionError):
			print "Invalid choice! Must be [1-" + str(maxChoice-1) + "]"
	return menuChoices[choice]

# Pops the first card in deck and appends to hand
# Return new hand
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
# If player's turn, then hide dealer's second card
def showCards(dealer,player,turn="player"):
	print "*" * 20
	# If it is player's turn, show rank of dealer's face-up card
	# Else show the rank of dealer's hand
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
	print "*" * 20

# Evaluates and compares dealer and player hands
# Calculates bet and returns remaining chips
def blackjack(dealer, player, chips, bet):
	# Player bust
	if rank(player) > 21:
		print "Bust!"

	# Push
	elif rank(dealer) == rank(player):
		chips += bet
		print "Push"

	# Player gets Blackjack
	elif rank(player) == 21 and len(player) == 2:
		chips += 2.5*bet
		print "You got Blackjack!"

	# Dealer bust or player beats dealer
	elif rank(dealer) > 21 or rank(player) > rank(dealer):
		chips += 2*bet
		print "You win!"

	# Dealer beats player
	else:
		print "You lose!"

	return chips
	
def main():
	chips = 100
	numDecks = changeNumDecks()

	# while there are still chips available to bet
	while chips > 0:
		print "chips:", chips
		bet = getBet(chips)
		chips = chips - bet
		print "chips:", chips
		print "bet:", bet
		deck = initDeck(numDecks)
		dealerCards, playerCards = [], []
		dealerRank, playerRank = 0, 0

		# Deal cards by appending the first card from deck to list
		playerCards.append(deal(deck))
		dealerCards.append(deal(deck))
		playerCards.append(deal(deck))
		dealerCards.append(deal(deck))

		# Player goes first
		blackjack.turn = "player"

		# Check for dealer Blackjack
		if rank(dealerCards) == 21:
			print "\nDealer got blackjack!"
			showCards(dealerCards,playerCards,"dealer")
			blackjack.turn = None

		# Check player for Blackjack
		elif rank(playerCards) == 21:
			showCards(dealerCards,playerCards)
			blackjack.turn = None

		# Else show cards
		else:
			showCards(dealerCards,playerCards)

		# Player's turn
		while blackjack.turn is "player":
			choice = getChoice()

			if choice == "HIT": 
				playerCards.append(deal(deck))
			elif choice == "STAND":
				blackjack.turn = "dealer"
				break

			showCards(dealerCards,playerCards)
			playerRank = rank(playerCards)

			# Bust
			if playerRank > 21:
				blackjack.turn = None
			# Twenty-One
			elif playerRank == 21:
				print "\nYou got 21!"
				time.sleep(1)
				blackjack.turn = "dealer"

		print

		# Dealer's turn
		while blackjack.turn is "dealer":
			showCards(dealerCards,playerCards,blackjack.turn)
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
		chips = blackjack(dealerCards, playerCards, chips, bet)
		print

		# Display menu
		# if choice == "PLAY" then continue the game
		if chips > 0:
			choice = menu()
			if choice == "DECK":
				numDecks = changeNumDecks()
				print "Changed # of decks to:", numDecks
			elif choice == "EXIT":
				print "\nCashing out with", chips, "chips..."
				print "Thanks for playing!\n"
				return



	print "No more chips available"
	print "Thanks for playing!\n"






if __name__ == "__main__":
	main()

