# factory pattern Method
# Goal 1/ faciliter créa objets tout pres 2/ masquer les détails d'implentation


class Polygone:
	def __init__(self, nb_side=3, diameter=100, color="Black", position=(0, 0), 
		thickness=2):
		self.nb_side = nb_side
		self.diameter = diameter
		self.color = color
		self.position = position
		self.thickness = thickness

class ShapeFactory:
	def create_red_triangle():
		nb_side = 3
		diameter = 100
		color = "Red"
		position = (0, 0)
		thickness = 2

	def create_yellow_square():
		nb_side = 4
		diameter = 90
		color = "Yellow"
		position = (0, 1)
		thickness = 2

	def create_green_pentagon():
		nb_side = 5
		diameter = 120
		color = "Green"
		position = (2, 1)
		thickness = 7

#Test lines
polygone = Polygone()
pentagone = ShapeFactory.create_green_pentagon()
print(polygone(pentagone))
