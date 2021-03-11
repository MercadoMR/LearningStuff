def gcd(a,b):
	""" Function to find the greatest common divisor of two numers """
	if a == b:	return a
	elif a > b: return gcd(a-b,b)
	else:	return gcd(a,b-a)

a,b = input("Ingresa dos números para su mcd:").split(' ')
a,b = int(a),int(b)

print("El mcd es de {} y {} es {}".format(a,b,gcd(a,b)))
	