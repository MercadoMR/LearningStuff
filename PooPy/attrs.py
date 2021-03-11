class MiClase:
	""" Docstring de la clase """
	def __init__(self):
		self.a = 3
		self.b = 1
		print("Clase creada!")
	def metodo(self):
		""" Docstring del metodo """
		print("Metodo default de la clase")

c = MiClase()
print(c.__doc__)
print(c.metodo.__doc__)
print(c.__dict__)
print(MiClase.__dict__)