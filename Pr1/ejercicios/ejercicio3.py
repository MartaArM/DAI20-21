# ejercicio3.py
# Criba de erastótenes

print("Escriba un número")
num = input()
num = int(num)
lista = []
primos = []

i = 2;

while i <= num:
	lista.append(i)
	i=i+1

while len(lista) != 0:
	valor = lista[0]
	i = 0
	while i < len(lista):
		if lista[i] % valor == 0:
			lista.pop(i)
		i=i+1
	if lista[0] ** 2 > 20:
		primos.append(lista)
		break
	primos.append(lista)

		
print (primos)	