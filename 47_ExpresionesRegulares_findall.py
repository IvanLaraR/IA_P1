#El método findall

import re #se importa la funcion re 

var = "Hola Mundo" #se declara una variable 
buscar = re.findall("o", var) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime

print("\n")

#puedes buscar sílabas, palabras, frases, párrafos, páginas o libros enteros

var = "Hola Mundo este es mi el metodo" #se declara una variable 
buscar = re.findall("do", var) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime

