# ejercicio4.py
# expresiones regulare
import re
#Identificar cualquier palabra seguida de un espacio y una única letra mayúscula (por ejemplo: Apellido N).
def funcion1(cadena):
	return re.findall('[a-zA-Z]+\s[A-Z]{1}?',cadena)


nombre_archivo = "./textos/ejercicio6.txt"
# Leer de un archivo
with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()

print(funcion1(contenido))