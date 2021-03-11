class CPR:
	def __del__(self):
		print('Destructor invocado!')

cpr1 = CPR()
cpr2 = cpr1
del cpr1
del cpr2