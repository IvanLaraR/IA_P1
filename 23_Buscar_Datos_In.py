#se crea una lista //es true por que el string si esta en la lista
paises = ['mexico', 'brasil', 'canada', 'colombia']#se crea una lista de 4 elementos
print('mexico' in paises)#se muestra en la pantalla si un string esta en la variable 

#en este caso en false por lo cual no esta en la lista 
paises = ['mexico', 'brasil', 'canada', 'colombia']#se crea una lista de 4 elementos
print('colombia' in paises)#se muestra en la pantalla si un string esta en la variable 


print("\n")

obj = input("introduce el nombre del elemento: ")# se crea una variable que se iguala a la interaccion del usuario
paises = ['mexico', 'brasil', 'canada', 'colombia'] #se crea una lista con 4 elemtos
if obj in paises:# si la variable entrada esta en la lista se cumple la condicion y se compila el if 
    print("El elemento esta en la lista")#se imprime el mensaje si es true 
else:#se usa el else si la condicion no se cumle o es false 
    print("El elemento no esta en la lista")#se imprime el mensaje si es false

