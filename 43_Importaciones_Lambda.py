
#Las funciones lambda o funciones anónimas son funciones normales y corrientes pero con una sintaxis reducida

import math   #se utiliza la palabara reservada para usar modulos/bibliotecas

print("Area de una esfera si el radio vale 10") #se imprime el mensaje
def Area(radio):#Definimos la función
    Solucion = 4 * round(math.pi * radio * radio,2) #creamos una variable que se iguala al resultado de la operacion matematica 
    print(Solucion)#se imprime la respuesta 

Area(10)#se llama la funcion y se le asigna un numero

print("\n")
#simplificando usando lambda
print("Simplificando utilizando Lambda")
area = lambda radio: round(4 * math.pi * radio * radio,2) #se crea una varible y se iguala a la funcion lamda que contiene la operacion matematica
print(area(10))#se imprime y se llama a la funcion asignandole un valor 

