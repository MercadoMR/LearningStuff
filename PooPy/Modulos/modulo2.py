def fun2():
	print("Función perteneciente al módulo 2")
	return
if __name__ == "__main__":
	print("Soy el módulo 2 y me ejecuto como script")
	import modulo1
	fun2()
	modulo1.fun1()
else:
	print("Soy el módulo 2 y me ejecuto como módulo")