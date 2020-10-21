#./app/app.py
from flask import Flask
from time import time
import math
import random
import logging
import re

app = Flask(__name__);

#Devuelve el máximo valor de una lista
#Se utiliza en ordenacion_seleccion
#Ejercicio 2
def buscar_max(lista, ini, fin):
	p_max = ini;
	for i in range(ini+1, fin+1):
			if lista[i] > lista[p_max]:
					p_max = i
	return p_max



#Ejercicio 2
def ordenacion_burbuja(lista):
	num = len(lista);
	lista_aux = lista;
	i = 0;
	while i < num:
		j = i;
		while j < num:
			if lista_aux[i] > lista_aux[j]:
				aux = lista_aux[i];
				lista_aux[i] = lista_aux[j];
				lista_aux[j] = aux;
			j = j + 1;
		i = i + 1;
	return lista_aux;

#Ejercicio 2
def ordenacion_seleccion(lista):
	num = len(lista) - 1;
	lista_aux = lista;

	while num > 0:
		max = buscar_max(lista_aux, 0, num);
		aux = lista_aux[max];
		lista_aux[max] = lista_aux[num];
		lista_aux[num] = aux;
		num = num - 1;
	return lista_aux;

#Mantiene siempre una sublista ordenada al principio de la lista.
#Va añadiendo un item nuevo al final y ordena la sublista del principio
#Ejercicio 2
def ordenacion_insercion(lista):
	lista_aux = lista;

	for i in range(0,len(lista)-1):

		valor = lista_aux[i];
		pos = i;

		#Si el valor anterior es mayor, se cambian las posiciones
		while pos > 0 and lista_aux[pos-1] > valor:
				lista_aux[pos]=lista_aux[pos-1];
				pos = pos-1;

		lista_aux[pos]=valor;
	return lista_aux;

#Función de Fibonacci
#Ejercicio 3
def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)

#Comprueba si una cadena de "[" y "]" está balanceada
#Ejercicio 5
def cadenaBalanceada(cadena):
	cadena_aux = list();
	for val in cadena:
		cadena_aux.append(val);
	cad = "";

	balanceada = True;
	i = 0;
	hay_corchete = False;

	while i < len(cadena_aux) and balanceada == True:
		simbolo = cadena_aux[i];
		cadena_aux.pop(i);
		j = 0;
		
		hay_corchete = False;
		if simbolo == "[":
			while j < len(cadena_aux) and hay_corchete == False:
				if cadena_aux[j] == "]":
					cadena_aux.pop(j);
					hay_corchete = True;
					cad = cad + "entra1";
				else:
					j = j+1;
					cad = cad + "entra2";
		else:
			balanceada = False;

	if len(cadena_aux) != 0 or hay_corchete == False:
		balanceada = False;

	
	return balanceada;



@app.route('/')
def hello_world():
 return 'Esta es la página principal'

#Ejercicio 2
@app.route('/ordenar/<lista>')
def ordenar(lista):
	lista2 = list();
	for valor in lista:
		# Elimino las comas
		if valor != ",":
			lista2.append(int(valor));

	#Ejecuto el algoritmo burbuja y mido el tiempo
	t_burbuja_i = time(); 
	lista_b = ordenacion_burbuja(lista2);
	t_burbuja_f = time();
	t_burbuja = t_burbuja_f - t_burbuja_i;

	string_dev = "Burbuja: "
	for valor in lista_b:
		string_dev = string_dev + str(valor);
	string_dev = string_dev + " Tiempo: " + str(t_burbuja) + "\n";

	#Ejecuto el algoritmo seleccion y mido el tiempo
	t_seleccion_i = time(); 
	lista_s = ordenacion_seleccion(lista2);
	t_seleccion_f = time();
	t_seleccion = t_seleccion_f - t_seleccion_i;

	string_dev = string_dev + " Selección: "
	for valor in lista_s:
		string_dev = string_dev + str(valor);
	string_dev = string_dev + " Tiempo: " + str(t_seleccion) + "\n";
	
	#Ejecuto el algoritmo inserción y mido el tiempo
	t_insercion_i = time(); 
	lista_i = ordenacion_insercion(lista2);
	t_insercion_f = time();
	t_insercion = t_insercion_f - t_insercion_i;

	string_dev = string_dev + " Inserción: "
	for valor in lista_i:
		string_dev = string_dev + str(valor);
	string_dev = string_dev + " Tiempo: " + str(t_insercion) + "\n";

	return string_dev;

#Ejercicio 3
@app.route('/criba/<valor>')
def criba_erastotenes(valor):
	num = int(valor);
	lista = [];
	primos = [];
	string_dev = "";

	i = 2;

	while i <= num:
		lista.append(i);
		i=i+1;

	while lista[0] <= math.sqrt(num):
		valor = lista[0];
		primos.append(lista[0]);
		k = 0
		while k < len(lista):
			if lista[k] % valor == 0:
				lista.pop(k);
			k=k+1;
		
	primos.extend(lista);

	for valor in primos:
		string_dev = string_dev + str(valor) + " ";

	return string_dev;


#Ejercicio 4
@app.route('/fibonacci')
def fibonacci_flask():

	nombre_archivo = "./textos/ejercicio4.txt";
	nombre_escritura = "./textos/ejercicio4_return.txt"
	# Leer de un archivo
	with open(nombre_archivo, "r") as archivo:
	    contenido = archivo.read();

	if contenido != '':
		num = int(contenido)
		with open(nombre_escritura, "w") as archivo:
			archivo.write("El valor " + contenido + " de la sucesión de Fibonacci de " + contenido + 
				" es " + str(fibonacci(num-1)));
		return "Archivo completo";
	else:
		return "No hay ningún número en " + nombre_archivo;

#Ejercicio 5
@app.route('/cadena')
def cadena():
	tam_cadena = random.randint(1,10);
	cadena = "";
	# Generación de cadena aleatoria con "[" o "]"
	for i in range(1, tam_cadena):
		valor = random.randint(0, 10)
		if valor % 2 == 0:
			cadena = cadena + "[";
		else:
			cadena = cadena + "]";
	devolver = cadena;
	
	if cadenaBalanceada(cadena) == True:
		devolver = devolver + " - " + "Cadena balanceada";
	else:
		devolver = devolver + " - " + "Cadena NO balanceada";

	return devolver;

#Ejercicio 6.1
@app.route('/ex_mayusculas/<cadena>')
def ex_mayusculas(cadena):
	return str(re.findall('[a-zA-Z]+\s[A-Z]{1}?',cadena));

#Ejercicio 6.2
@app.route('/ex_correo/<cadena>')
def ex_correo(cadena):
	patron = re.compile(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}")

	if patron.search(cadena): # Comprobemos sí este es un correo electronico valido
		return "Correo valido";
	else:
		return "Correo no válido";

@app.errorhandler(404)
def page_not_found(e):
	return "Error 404: página no encontrada";