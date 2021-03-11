from abc import ABC, abstractmethod #Abstract Base Classes
#https://www.python-course.eu/python3_magic_methods.php
class Animal(ABC): #Declaring an abstract class
	def __init__(self,name):
		self.name = name
		super().__init__()
		print("El {} se ha creado".format(name))
	@abstractmethod
	def growl(self):
		pass

class Dog(Animal):
	def __init__(self,name):
		super().__init__(name)		
	def growl(self):
		print("Dog barks: Wow wow!")
	def traerPelota(self):
		print("I'm catching the ball")
	
class Cat(Animal):
	def __init__(self,name):
		super().__init__(name)
		print("Cat constructed!")
	def growl(self):
		print("Cat meows: Meow meow!")
	def tirarLazo(self):
		print("I'm playing with the lace")
		
animals = []
perro = Dog("Perro")
perro.traerPelota()
gato = Cat("Gato")
gato.tirarLazo()
animals.append(perro)
animals.append(gato)
for animal in animals:
	animal.growl()