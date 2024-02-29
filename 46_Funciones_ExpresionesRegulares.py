#Que son las funciones y Como funciones

import re #se importa la funcion re 

var = "Hola Mundo" #se declara una variable 
buscar = re.search("o", var) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime

print("\n")

#Ejemplo de como se veria si no hay hay ningun caracter que estes buscando
var = "Hola Mundo" #se declara una variable 
buscar = re.search("h", var) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime

print("\n")
#Ejemplo de busquedas con palabras o mas caracteres

var = "Hola Mundo" #se declara una variable 
buscar = re.search("Hola", var) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime
