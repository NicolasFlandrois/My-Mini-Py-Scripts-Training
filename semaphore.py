# conteur d'instance
# Static Method/Semaphore
class Ticket:
	nb_ticket = 0
	def __init__(self):
		Ticket.nb_ticket += 1

	def get_nb():
		return Ticket.nb_ticket

#test
ticket = Ticket()
ticket = Ticket()
ticket = Ticket()
ticket = Ticket()
print(Ticket.get_nb())