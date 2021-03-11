class Base:
	def met1(self):
		print("First method of the base class")
	def met2(self):
		print("Second method of the base class")

class Derived(Base):
	def met1(self):
		print("First method of the derived class")
		print("Example of overriding")
		print("Now calling the super method")
		super().met1()
	def met2(self):
		print("Second method of the derived class")
		print("Calling the overrided method on a different way")
		super().met2()

d = Derived()
d.met1()
Derived.met2(d)