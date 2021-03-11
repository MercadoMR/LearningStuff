def esPrimo(n):
	for i in range(2,n//2 + 1):
		if n%i == 0:	return False
	return True

n = int(input("Ingresa un entero positivo: "))
if esPrimo(n): print("El numero ingreado es primo!")
else: print("El numero ingreado no es primo...")