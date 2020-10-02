# ejercicio1.py
import random

num = random.randrange(101)
n = 0

print ("Adivine el número...")

while n<10:
	num_user = input()
	num_user = int(num_user)

	if num_user <  num:
		print ("El número que busca es mayor")
		n=n+1
	elif num_user > num:
		print ("El número que busca es menor")
		n=n+1
	else:
		print ("Ha acertado!!")
		break
		

if n>=10:
	print("Ha sobrepasado el número de intentos")
