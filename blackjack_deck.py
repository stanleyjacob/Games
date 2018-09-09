from graphics import *
import time
import random 

def calculate_card_list(list_cards):
	value = 0
	count_aces = 0
	for i in range(len(list_cards)):
		temp = list_cards[i][0]
		if temp == 'jack' or temp == 'queen' or temp == 'king':
			value += 10
		elif temp == 'ace':
			count_aces += 1
		else:
			value += int(temp)
	
	temp = 11 * count_aces + value
	count = 0

	while count_aces != 0 and temp > 2:
		temp -= 11
		temp += 1
		count += 1
		if count == count_aces:
			break
	value = temp
	return value

class BlackjackDeck:
	def create_deck(self):
		self.total_card_count = self.num_decks * self.card_count
		self.complete_deck = []
		for k in range(self.num_decks):
			for i in range(len(self.card_names)):
				for j in range(len(self.card_suites)):
					self.complete_deck.append((self.card_names[i], self.card_suites[j]))

	def shuffle_deck(self):
		random.shuffle(self.complete_deck)

	def __init__(self, num_decks):
		self.num_decks = num_decks
		self.card_names = ['ace', '2', '3', '4', '5', '6', \
			'7', '8', '9', '10', 'jack', 'queen', 'king']
		self.card_suites = ['diamonds', 'hearts', 'spades', 'clubs']
		self.card_count = len(self.card_names) * len(self.card_suites)
		self.create_deck()
		self.shuffle_deck()

win = GraphWin("blackjack", 600, 400)
num_decks = 6
full_deck = BlackjackDeck(num_decks)
num_players = 1

def determineCardValue(name, cards, win, img_list):
	break_condition = False
	print name + "'s cards: "
	print cards
	offset = 60
	start = 170
	total_offset = 120

	while(break_condition != True):
		decision = raw_input("Hit or stand: ")
		
		if decision == 'H':
			temp = full_deck.complete_deck.pop()
			cards.append(temp)
			print(temp)
			updateProbabilities([temp])

			new_img_obj = drawCard(win, temp, start, 280, total_offset)
			total_offset += 60
			img_list.append(new_img_obj)

		elif decision == 'S':
			break_condition = True

		user_value = calculate_card_list(cards)
		if user_value >= 21:
			break_condition = True
		
	return user_value, cards, img_list



# def updateCount(current_count, cards_list):
# 	# heuristic: +1 for 7 to 9
# 	# -1 for 2 to 4
# 	# +2 for 10


# def counterAction(current_count):
# 	# hit when < card value 12 and count > 0

# 	# hit when < card value 16 and count > 20

# 	# stand when > card value 16 and count > 0

# def baselinePolicy():
	

global_card_counts = [] # ordered by A, 2, 3, ..., 10
for i in range(9):
	global_card_counts.append(4*num_decks)
global_card_counts.append(16*num_decks)
probabilities = []
for i in range(10):
	probabilities.append(float(global_card_counts[i])/(52*num_decks))
#print probabilities

expected_values1 = []
for i in range(10):
	expected_values1.append(probabilities[i]*(i+1))

expected_values2 = []
for i in range(10):
	expected_values2.append(probabilities[i]*(i+1))
expected_values2[0] = 11 * probabilities[0]


def updateProbabilities(cards_list):
	for i in range(len(cards_list)):
		temp = cards_list[i][0]
		if temp == 'ace':
			global_card_counts[0] -= 1
		elif temp == '10' or temp == 'jack' or temp == 'queen' or temp == 'king':
			global_card_counts[9] -= 1
		else:
			global_card_counts[(int(temp)-1)] -= 1
	for i in range(10):
		probabilities[i] = float(global_card_counts[i])/sum(global_card_counts)
		expected_values1[i] = probabilities[i]*(i+1)
		expected_values2[i] = probabilities[i]*(i+1)
	expected_values2[0] = 11 * probabilities[0]


def determineDealerValue(name, cards, user_value, win, dealer_imgs):
	print name + "'s cards: "
	print cards
	dealer_value = 0
	dealer_cards_complete = cards
	offset_ind = 120

	while dealer_value <= user_value:
		temp = full_deck.complete_deck.pop()
		dealer_cards_complete.append(temp)
		print(temp)
		cards.append(temp)
		dealer_value = calculate_card_list(cards)
		updateProbabilities([temp])
		new_dealer_card = drawCard(win, temp, start, 110, offset_ind)
		offset_ind += 60
		dealer_imgs.append(new_dealer_card)
		if dealer_value > 21:
			break
	
	dealer_cards_complete.pop()
	

	return dealer_value, dealer_cards_complete, dealer_imgs

def drawCard(win, curr_card, start_pixel_x, start_pixel_y, offset, faceUp = True):
	base_path = "/Users/qldo18/Desktop/cards4/"
	if faceUp:
		new_value = curr_card[0]
		new_card_name = curr_card[1]
		file_name = base_path + new_value + "_of_" + new_card_name + ".gif"
		card_to_display = Image(Point(start_pixel_x + offset, start_pixel_y), file_name)
		card_to_display.draw(win)
	else:
		back_card = base_path + "back.gif"
		card_to_display = Image(Point(start_pixel_x + offset, start_pixel_y), back_card)
		card_to_display.draw(win)
	return card_to_display

user_money = 1000

def cleanTable(win, cards):
	for i in range(len(cards)):
		cards[i].undraw()

while(1):
	# print probabilities
	# print expected_values1
	# print expected_values2
	# print sum(expected_values1)
	# print sum(expected_values2)

	user_bet = raw_input("Place bet: ")
	user_money -= int(user_bet)

	dealer_face_up = full_deck.complete_deck.pop()
	updateProbabilities([dealer_face_up])

	dealer_face_down = full_deck.complete_deck.pop()
	dealers_cards = [dealer_face_up, dealer_face_down]
	print "Dealer's card: "
	print dealer_face_up

	start = 170
	dealer1 = drawCard(win, dealer_face_down, start, 110, 0, False)
	dealer2 = drawCard(win, dealer_face_up, start, 110, 60)

	user_cards = []

	temp = full_deck.complete_deck.pop()
	user_cards.append(temp)

	offset = 60
	total_offset = 0
	user_card_img1 = drawCard(win, temp, start, 280, total_offset)
	total_offset += offset

	temp = full_deck.complete_deck.pop()
	user_cards.append(temp)
	user_card_img2 = drawCard(win, temp, start, 280, total_offset)

	list_user_imgs = [user_card_img1, user_card_img2]

	updateProbabilities(user_cards)
	user_value, user_cards_complete, img_list = determineCardValue("User", user_cards, win, list_user_imgs)

	if user_value > 21:
		print "Bust"
	
	updateProbabilities([dealer_face_down])
	
	dealer1.undraw()
	dealer1 = drawCard(win, dealer_face_down, start, 110, 0)
	list_dealer_imgs = [dealer1, dealer2]

	dealer_value, dealer_cards_complete, dealer_img_list = \
		determineDealerValue("Dealer", dealers_cards, user_value, win, list_dealer_imgs)
	
	if user_value > 21:
		print "Dealer wins"
	elif dealer_value >= user_value:
		print "Dealer wins"
	elif user_value == 21:
		print "Winner winner chicken dinner"
		user_money += int(user_bet) * 2
	else:
		print "User wins"
		user_money += int(user_bet) * 2

	print "User cash: " + str(user_money)

	time.sleep(5)

	cleanTable(win, img_list)
	cleanTable(win, dealer_img_list)

# print len(card_names)
# print len(card_suites)

