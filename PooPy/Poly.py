class Animal:
	def __init__(self):
		print("Constructing an animal...")
	def __del__(self):
		print("Destroying the animal...")
	def growl(self):
		print("The animal is growling")

class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("Dog constructed!")
	def __del__(self):
		print("Dog destroyed!")
		Animal.__del__(self)
	def growl(self):
		Animal.growl(self)
		print("Dog barks: Wow wow!")
	
class Cat(Animal):
	def __init__(self):
		super().__init__()
		print("Cat constructed!")
	def __del__(self):
		print("Cat destroyed!")
	def growl(self):
		super().growl()
		print("Cat meows: Meow meow!")

animals = []
animals.append(Dog())
animals.append(Cat())
for animal in animals:
	animal.growl()
	del animal

