def fun2():
	print("Función perteneciente al módulo 3")
	return
if __name__ == "__main__":
	print("Soy el módulo 3 y me ejecuto como script")
	import paqueton
	from paqueton import front1, front2
	front1.f()
	front2.f()
	
else:
	print("Soy el módulo 2 y me ejecuto como módulo")