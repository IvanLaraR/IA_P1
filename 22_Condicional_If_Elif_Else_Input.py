#para que el usuario interactue con la consula se utiliza input
autos = int(input("Cuantos autos tienes:\t"))#se imprime un menaje en el cual el usario por medio el metodo input puede interactuar

if autos <= 0: #se declara una condicion si el numero que utiliza es menor o igual a 0 se ejecute 
    print("No tienes auto")#se imprime el mensaje

#elif es mientras (mientras se true se va a ejecutar otra cosa)
elif autos >=1 and autos <=3:#mientras edad sea mayor o igual a 1 y menor o igual a 17 se ejecute
    print("eres una persona promedio de 1 a 3 autos")#se imprime el mensaje

elif autos <=5: #mientras edad sea menor o igual a 100 se ejecute
    print("eres uns persona que le gustas los autos tienes mas de 5")#se imprime el mensaje

else:#cuando sea falsa la condicion se imprimira el mensaje
    print("opcion no valida")#se imprime el mensaje 
