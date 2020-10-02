# ejercicio3.py
# Criba de erastótenes
import math

while True:
	print("Escriba un número")
	num = input()
	num = int(num)
	lista = []
	primos = []

	i = 2;

	while i <= num:
		lista.append(i)
		i=i+1

	while lista[0] <= math.sqrt(num):
		valor = lista[0]
		primos.append(lista[0])
		k = 0
		while k < len(lista):
			if lista[k] % valor == 0:
				lista.pop(k)
			k=k+1
		
	primos.extend(lista)
	print (primos)	