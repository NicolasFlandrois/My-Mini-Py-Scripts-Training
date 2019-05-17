#!/usr/bin/python3
#UTF8
#Date: Mon 04 Feb 2019 05:14:35 PM CET 
#Author: Nicolas Flandrois
#Description: Exercice on Python Classes, and Object oriented Programming
import random

class Card(object):
	def __init__(self, suit, val):
		"""docstring"""
		self.suit = suit
		self.value = val

	def show_card(self):
		"""docstring"""
		print("{} of {}").format(self.value, self.suit)

class Deck(object):
	def __init__(self):
		"""docstring"""
		self.cards = []
		self.build()

	def build(self):
		"""docstring"""
		for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
			for v in range(1, 14):
				if v == 11:
					v = "Jack"
				elif v == 12:
					v = "Queen"
				elif v == 13:
					v = "King"
				self.cards.append(Card(s, v))

	def show_deck(self):
		"""docstring"""
		for c in self.cards:
			c.show_card()

	def shuffle(self):
		"""docstring"""
		for i in range(len(self.cards)-1, 0, -1):
			r = random.randint(0, i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	def draw_card(self):
		"""docstring"""
		return self.cards.pop()

class Player(object):
	def __init__(self, name):
		"""docstring"""
		self.name = name
		self.hand = []

	def show_name(self):
		"""dostring"""
		return self.name

	def draw_hand(self, deck):
		"""docstring"""
		self.hand.append(deck.draw_card())
		return self

	def show_hand(self):
		for card in self.hand:
			card.show_card()

	def discard(self):
		"""docstring"""
		return self.hand.pop

####################### TEST LINES #########################
deck = Deck()
deck.shuffle()
deck.show_deck()
print("################## Players in place, lets Deal. ######################")
bob = Player("Bob")
print(bob.show_name())
bob.draw_hand(deck).draw_hand(deck).draw_hand(deck).draw_hand(deck).draw_hand(deck)
bob.show_hand()

daniel = Player("Daniel")
print(daniel.show_name())
daniel.draw_hand(deck).draw_hand(deck).draw_hand(deck).draw_hand(deck).draw_hand(deck)
daniel.show_hand()

henry = Player("Henry")
print(henry.show_name())
henry.draw_hand(deck).draw_hand(deck).draw_hand(deck).draw_hand(deck).draw_hand(deck)
henry.show_hand()

john = Player("John")
print(john.show_name())
john.draw_hand(deck).draw_hand(deck).draw_hand(deck).draw_hand(deck).draw_hand(deck)
john.show_hand()
