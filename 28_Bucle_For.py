
#se crea un bucle for con una variable llamada x

for x in "Mecatronica": #se pone el bucle la variable luego el lugar y el string y para cerrar la condicion se pone :
    print(x)#se imprime la varibale

print("\n")
#tambien se puede crear una lista y separar los elemtos que contenga la lista 

nombre = ["Kevin", "Ivan", "Lara", "Ruvalcaba"]#se crea una lista con 4 elemtos 
for y in nombre: #se inicia el bucle que va a ejecutar un elemento cada vuelta
    print(y) #se imprime la variable que englomera la lista

print("\n")
#tambien se puede usar el metodo continue para descartar elemtos y break para parar el blucle 

for y in nombre: #se inicia el bucle que va a ejecutar un elemento cada vuelta
    if y == "Kevin":#se hace una condicion si el string es igual  un elemento de la lista se cumple 
        continue #si es verdad se salta ese elemento de la lista 
    print(y) #se imprime la variable que englomera la lista

    
print("\n")

for y in nombre: #se inicia el bucle que va a ejecutar un elemento cada vuelta
    if y == "Lara":#se hace una condicion si el string es igual  un elemento de la lista se cumple 
        break #si es verdad se detiene el bucle 
    print(y) #se imprime la variable que englomera la lista

print("\n")
#el pass se usa para crear una lista vacia

for x in '': #se declara un bucle for 
	pass #se crea una lista vacia o se vacia 
