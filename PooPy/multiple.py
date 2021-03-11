class A:
	def __init__(self):
		print("Constructor de A!")
	def __del__(self):
		print("Destructor de A!")
	def f(self):
		print("Funcion de A...")

class B:
	def __init__(self):
		print("Constructor de B!")
	def __del__(self):
		print("Destructor de B!")
	def f(self):
		print("Funcion de B...")

class C(A,B):
	def __init__(self):
		A.__init__(self)
		B.__init__(self)
		print("Constructor de C!")
	def __del__(self):
		print("Destructor de C!")
		B.__del__(self)
		A.__del__(self)
	def f(self):
		print("Funcion de C...")
		print("Llamando funciones de clases bases")
		super().f()
		B.f(self)

c = C()
c.f()
del c