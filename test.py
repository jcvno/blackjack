import blackjack as bj

def test():
	print
	chips = 100
	print "***Testing method: changeNumDecks()***"
	"""Test for valid user input"""
	numDecks = bj.changeNumDecks()
	assert 0 < numDecks <= bj.MAX_DECKS
	print "PASSED\n"

	print "***Testing deck construction***"
	deck = bj.shuffleDeck(numDecks)
	"""Test for correct number of cards in deck"""
	assert len(deck) == 52*numDecks
	"""Check if all appropriate cards are in deck"""
	for r in '23456789TJQKA'*numDecks:
		for s in 'SHDC':
			assert r+s in deck
			index = deck.index(r+s)
			del deck[index]
	print "PASSED\n"

	print "***Testing method: deal(deck)***"
	"""Test if method correctly pops card"""
	deck = bj.shuffleDeck(1)
	for i in range(len(deck)):
		bj.deal(deck)
	assert len(deck) == 0
	print "PASSED\n"

	print "***Testing method: rank(hand)***"
	"""Test validity of ranks of all cards in a deck"""
	deck = bj.shuffleDeck(1)
	for card in deck:
		assert 0 < bj.rank([card]) <= 11
	print "PASSED\n"

	print "***Testing method: placeBet(chips)***"
	"""Test method returns a bet value that is not greater than chips value"""
	bet = bj.placeBet(chips)
	assert 1 <= bet <= chips
	print "PASSED\n"

	print "***Testing method: menu()***"
	"""Test for valid menu() return value"""
	choice = bj.menu()
	assert choice in bj.menuChoices
	print "PASSED\n"

	print "***Testing method: blackjackMenu(playerCards,chips,bet)***"
	"""Test for valid menu() return value"""
	playerCards = [bj.deal(deck), bj.deal(deck)]
	choice = bj.blackjackMenu(playerCards,chips,bet)
	assert choice in bj.blackjackChoices
	print "PASSED\n"

	print "***Testing method: getPayout(dealer, player, chips, bet)***"
	"""Test for player blackjack and correct payout"""
	# Blackjack pays 3:2
	# 100 bet: 100(bet) + 150(payout) + 0(chips) = 250
	assert bj.getPayout(['5D', '5C'], ['AH', 'JS'], 0, 100) == 250
	# 50 bet: 50(bet) + 75(payout) + 25(chips) = 150
	assert bj.getPayout(['5D', '5C'], ['AH', 'JS'], 25, 50) == 150
	"""Test for Blackjack with decimal place"""
	# 2.5 bet: 2.5(bet) + 3.75(payout) + 2.5(chips) => round(8.75,1) = 8.8
	assert bj.getPayout(['5D', '5C'], ['AH', 'JS'], 2.5, 2.5) == 8.8
	"""Test for Blackjack with decimal place"""
	# 1.25 bet: 1.25(bet) + 1.875(payout) + 0(chips) => round(3.125,1) = 3.1
	assert bj.getPayout(['5D', '5C'], ['AH', 'JS'], 0, 1.25) == 3.1
	"""Test for player bust"""
	# 50 bet: 0(lost bet) + 0(payout) + 25(available chips) = 25
	assert bj.getPayout(['5D', '5C'], ['3H', 'JS', 'KH'], 25, 50) == 25
	"""Test for player win"""
	# 100 bet: 100(bet) + 100(payout) + 100(chips) = 300
	assert bj.getPayout(['TD', '7C'], ['JS', 'KH'], 100, 100) == 300

	print "PASSED\n"

	print "All tests passed! :)"

if __name__ == "__main__":
	test()