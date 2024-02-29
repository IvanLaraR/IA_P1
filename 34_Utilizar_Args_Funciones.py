#Al escribir *args como argumento, me da la posibilidad de utilizarlo cuando quiera dentro de la función

def colores(*args): #se difine una variable definida y se le asigna el metodo args
    print("El primer color es " + args[0] + " y el ultimo color es " + args[3]) #se imprime el mansaje que se la va asumar los elemtos de la varibale definida y las va a imprimir por su pósicion

colores("Azul", "Blanco", "Negro", "Rojo")#se le asigna los strings a nuestra variable definida 

