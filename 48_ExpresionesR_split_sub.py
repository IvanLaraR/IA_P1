#la función split(). Esta función divide una cadena de caracteres según un patrón de búsqueda.

import re #se importa la funcion re 

var = "La pícara pájara pica la típica jícara; a la típica jícara, pica la pícara pájara" #se declara una variable 
buscar = re.split("", var) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime

print("\n")
#para quiara las palabaras que se repitan
var = "La pícara pájara pica la típica jícara; a la típica jícara, pica la pícara pájara" #se declara una variable 
buscar = re.split("ara", var) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime


print("\n")
#método sub() reemplaza las coincidencias por lo que le especifiques en el segundo argumento

var = "La pícara pájara pica la típica jícara; a la típica jícara, pica la pícara pájara" #se declara una variable 
buscar = re.sub("a", "-", var) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime

print("\n")
#maxsplit() controla el máximo de coincidencias que devuelve split()

var = "La pícara pájara pica la típica jícara; a la típica jícara, pica la pícara pájara" #se declara una variable 
buscar = re.split("", var, 3) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime

print("\n")


#Puedes limitar los resultados que reemplaza sub() añadiendo el número como cuarto parámetro:

var = "La pícara pájara pica la típica jícara; a la típica jícara, pica la pícara pájara" #se declara una variable 
buscar = re.sub("a", "-", var,4) #se declara una variable y se igauala a la funcion y la busca segun el caracter que solicites 
print(buscar)#se imprime
