from .Dog import Dog 
def start():
	print("starting...")

def addDoggy(name,tricks):
	instance = Dog(name)
	for trick in tricks:
		instance.add_trick(trick)
	print(instance.tricks)
	return instance
