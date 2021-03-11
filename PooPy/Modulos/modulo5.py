def fun2():
	print("Función perteneciente al módulo 3")
	return
if __name__ == "__main__":
	print("Soy el módulo 5 y me ejecuto como script")
	from paqueton.paquetin import back1,back2
	back1.f()
	back2.f()
else:
	print("Soy el módulo 2 y me ejecuto como módulo")