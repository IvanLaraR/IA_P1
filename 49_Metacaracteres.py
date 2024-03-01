#Los metacaracteres y las secuencias especiales

import re #se importa la funcion re 

var = "La pícara pájara pica la típica jícara; a la típica jícara, pica la pícara pájara" #se declara una variable 
buscar = re.findall("[a-i]", var) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime

print("\n")
#Esta condición es una abreviación del if (if buscar:), el equivalente es: if buscar == True

import re

var = "El cueerpo logra lo que la mente cree" #se crea una variable
buscar = re.findall("cue{2}rpo", var) #se crea una variable y se igauala a la funcion 
if buscar: #se crea una condicional
	print("Hay coincidencias.") #se imprime
else: #si no se cumple se ejecuta
	print("No hay coincidencias.") #se imprime

print("\n")

var = "El cueerpo logra lo que la mente cree" #se crea una variable
buscar = re.findall("fracasar|lograr", var) #se crea una variable y se igauala a la funcion 
if buscar: #se crea una condicional
	print("Hay coincidencias.") #se imprime
else: #si no se cumple se ejecuta
	print("No hay coincidencias.") #se imprime


print("\n")

var = "El cueerpo logra lo que la mente cree" #se crea una variable
buscar = re.findall("cue...o", var) #se crea una variable y se igauala a la funcion 
if buscar: #se crea una condicional
	print("Hay coincidencias.") #se imprime
else: #si no se cumple se ejecuta
	print("No hay coincidencias.") #se imprime


print("\n")

var = "El cueerpo logra lo que la mente cree" #se crea una variable
buscar = re.findall("^mente cree", var) #se crea una variable y se igauala a la funcion 
if buscar: #se crea una condicional
	print("Hay coincidencias.") #se imprime
else: #si no se cumple se ejecuta
	print("No hay coincidencias.") #se imprime



print("\n")

var = "El cueerpo logra lo que la mente cree" #se crea una variable
buscar = re.findall("gra.$", var) #se crea una variable y se igauala a la funcion 
if buscar: #se crea una condicional
	print("Hay coincidencias.") #se imprime
else: #si no se cumple se ejecuta
	print("No hay coincidencias.") #se imprime


