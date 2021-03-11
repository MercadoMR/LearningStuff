
def fun1(a,b=5,**d):
	""" Function for additional arguments """
	print(a,b)
	print(type(d))
	for k,v in d.items():
		print("El valor de {} es {}".format(k,v))
		print("Es decir:",d[k])
	return

def fun2(*args):
	""" Function for variable arguments """
	print(type(args))
	i = 0
	for arg in args:
		i += arg
	print(i)
	return
	
#A keyword argument cannot be followed by a non-keyword argument.
#fun(*args,a,b) will take all given arguments as the *args tuple

def fun3(*args,a,b=2): #default value could be in both, a or b
	""" Variable arguments and keyword arguments """
	for arg in args:
		print("Argumento extra:",arg)
	print("a y b respectivamente",a,b)
	return

def fun4(a,b=0,*c,**d):
	""" Non-keyword, default, variable and additional arguments"""
	print("a:",a)
	print("b:",b)
	print("Variable arguments (tupla)")
	for x in c:
		print("Indice {} valor {}".format(c.index(x),x))
	print("Additional arguments (dict)")
	for clave,valor in d.items():
		print("Clave {} valor {}".format(clave,valor))
	return 
	
fun1(3,2,c=5,d=2,e=1,f=2)
fun2(1,2,3,4,5,6)
fun3(1,2,3,1,2,a=1,b=0)
fun4(0,1,5,5,5,5,4,h=9,g=9,i=2)