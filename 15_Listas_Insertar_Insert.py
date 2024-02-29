
#Agregar un nuevo caracter a la lista con posicion 

automoviles = ["Honda", "Fiat", "BMW", "Ford", "Kia", "Bentley", "Tesla", "Toyota"]#se crea una lista con 8 palabras diferentes 
automoviles.insert(0,"Mazda")#se utiliza la variable y se le agrega el metodo insert para agregar un caracter por el nombre y posicion de la lista 
print(automoviles) #se imprime lo que esta dentro de la lista

print("\n")

#Ejemplo
#Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. Deberás hacer esto utilizando posiciones de lista negativas.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.insert(6,"magenta")
colores.insert(7,"turquesa")
print(colores)
