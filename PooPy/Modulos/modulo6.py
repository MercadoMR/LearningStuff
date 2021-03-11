def fun2():
	print("Función perteneciente al módulo 3")
	return
if __name__ == "__main__":
	print("Soy el módulo 5 y me ejecuto como script")
	import paqueton.paquetin.back1
	paqueton.paquetin.back1.f()
	import paqueton.paquetin.back2
	paqueton.paquetin.back2.f()
	
else:
	print("Soy el módulo 2 y me ejecuto como módulo")