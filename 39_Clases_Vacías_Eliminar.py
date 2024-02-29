#Como dejar las clases Vacias
class Banco():#se crea una clase 
    pass #se usa el pass para dejarla vacia y poder compilar el programa

print("\n")

#Como eliminar las propiedades

class Banco(): #se crea una clase
    def __init__(self, clave, pin): #se usa el el unit para establecer valores iniciales 
        self.clave = clave #se declara el this al objeto y se le da un valor inicial
        self.pin = pin #se declara el this al objeto y se le da un valor inicial

    def datos(self):  #se declara una varible definida se utiliza el self para especificar
        print("Su numero de Clave es: ", self.clave ," y el pin es: ", self.pin) #se imprime le mensaje y se le pone el self para llamr lo que queramos poner 

Banco1 = Banco(21310155, 2111) #creamos una varible y le asignamos el valor de la clase 

Banco1.datos() #llamamos al objeto para que se imprima y muestre el mensaje 

del Banco1.pin#se usa para eliminar el argumento 



 

