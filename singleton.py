#veut class instancier(nb creation d'objet) 1 seul fois = 1 seul Objet

class Singleton:
	instance = None
	def __new__(cls):
		if cls.instance is None:
			cls.instance = object.__new__(cls)

		return cls.instance

print(Singleton())
print(Singleton())
print(Singleton())

#singleton == unique, même adresse pour chaques.
#A utiliser uniquement dans des cas précis (et si besoin, c'est que programme mal conçu à la base)