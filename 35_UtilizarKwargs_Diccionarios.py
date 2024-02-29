
#se utiliza cuando queremos usar argumentos arbitarios en direcciones 
def paises (**kwargs):#se difine una variable definida y se le asigna el metodo args //argumentos flexiles
        print("El primer pais es " + kwargs["pais1"] + "...." + "\nEl segundo paies es " + kwargs["pais2"] + "....") #se imprime el mansaje que se la va a sumar los elemtos de la varibale definida y las va a imprimir por su pósicio
paises(pais1='Mexico', pais2='Argentina')#se usa la variable y se le asigna sus arguementos que queremos que se impriman en el mensaje
