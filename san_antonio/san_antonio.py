# -*- coding: utf8 -*-

quotes = [
	"Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
	"On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
	"alvin et les Chipmunks",
	"Babar",
	"betty boop",
	"calimero",
	"casper",
	"le chat potté",
	"Kirikou"
]

def get_random_quote(my_list):
	"""This fonction show a random quote from a list."""
#	import random
#	n = random.randrange(0, 2, 2)
	item = my_list[0]
	return item
user_answer = "A"
while user_answer != "B":
	user_answer = input("Tappez 'Entrer' pour executer le programme, et 'B' pour quitter le programme. ")
	print(get_random_quote(quotes))

for character in characters:
	n_character = character.capitalize()
	print(n_character)