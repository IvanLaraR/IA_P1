
#se usa el break despues del if para romper el flujo de ejecucion del bucle si en algun momento se cumple la condicional

y = 2 #se declara una variable

while y <= 20: #se crea un bucle x menor o igual a 20
    print(y) #se imprime la variable x 
    if y == 10: #se crea un condicional si x es igual a 10 se ejecute 
        break #se pare de ejecutar el if
    y += 2 #se va incrementando el valor de x de 2 en 2

#la funcion del continue es para hacer saltos dentro del bucle while
print("\n")

x = 0 #se declara una variable

while x < 10: #se crea un bucle x menor que 10
	x += 1 #se va incrementendo el valor 1 por 1 
	if x == 2 or x == 9: #se crea un condicional si x es igual a 5 o 7 se cumple 
		continue #se usa el metodo continue para hacer el salto de los valores 5 y 7 
	print(x) #se imprime la varible x 

