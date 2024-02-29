
#el metodo sort se ordena alfabéticamente (a-z) //el sort son cambios permanentes para el resto del codigo//

automoviles = ["Honda", "Fiat", "BMW", "Ford", "Kia", "Bentley", "Tesla", "Toyota"]#se crea una lista con 8 palabras diferentes
automoviles.sort() #se llama a la variable y se le agrega el metodo .sort()
print(automoviles) #se imprime la lista

print("\n")#se le agrega un salto de linea para que se vea mas ordenado

#se sigue usando el metodo sort (reverse=True) pero en orden descente (z-a)

automoviles = ["Honda", "Fiat", "BMW", "Ford", "Kia", "Bentley", "Tesla", "Toyota"]#se crea una lista con 8 palabras diferentes
automoviles.sort(reverse=True) #la llama a la variable y se le agrega el orden de descendente
print(automoviles) #se imprime la lista

print("\n") #se le agrega un salto de linea para que se vea mas ordenado 

#El metodo stored() hace lo mismo pero temporal

automoviles = ["Honda", "Fiat", "BMW", "Ford", "Kia", "Bentley", "Tesla", "Toyota"]#se crea una lista con 8 palabras diferentes
print("\t",sorted(automoviles))#se va a imprimir la lista y ordenar y guardar en la variable
print("\t",automoviles) #se imprime la lista



