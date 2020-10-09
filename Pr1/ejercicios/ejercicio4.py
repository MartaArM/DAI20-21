# ejercicio4.py
# fibonacci
# lee de un fichero de texto un número entero n y escriba en otro fichero de texto el n-ésimo número de la sucesión de Fibonacci.

def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)


nombre_archivo = "./textos/ejercicio4.txt"
# Leer de un archivo
with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()

if contenido != '':
	num = int(contenido)
	print ("El valor " + contenido + " de la sucesión de Fibonacci de " + contenido + " es " + str(fibonacci(num-1)))

else:
	print("No hay ningún número en " + nombre_archivo)


