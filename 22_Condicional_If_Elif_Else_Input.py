#para que el usuario interactue con la consula se utiliza input
edad = int(input("Cual es tu edad:\t"))#se imprime un menaje en el cual el usario por medio el metodo input puede interactuar

if edad <= 0: #se declara una condicion si el numero que utiliza es menor o igual a 0 se ejecute 
    print("nadie puede tener esa edad")#se imprime el mensaje

#elif es mientras (mientras se true se va a ejecutar otra cosa)
elif edad >=1 and edad <=17:#mientras edad sea mayor o igual a 1 y menor o igual a 17 se ejecute
    print("eres menor de edad")#se imprime el mensaje

elif edad <=100: #mientras edad sea menor o igual a 100 se ejecute
    print("eres mayor de edad")#se imprime el mensaje

else:#cunado sea falsa la condicion se imprimira el mensaje
    print("edad no valida")#se imprime el mensaje 
