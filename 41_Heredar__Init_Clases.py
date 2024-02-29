
class Viaje: #se crea una clase
    def __init__(self, Estancia, Destino): #se declara una varible definida se utiliza el self para especificar
        self.Estancia = Estancia #se crea una varible
        self.Destino = Destino #se crea una varible 

    def imprime(self): #se declara una varible definida se utiliza el self para especificar 
        print("Tiempo de estancia: ", self.Estancia, "\nCon Destino a: ", self.Destino) #se imprime le mensaje y se le pone el self para llamr lo que queramos poner 

Viaje1 = Viaje("1 año", "Canada")#ponemos el nombre del objeto y la clase y le inicializo con un valor 
Viaje1.imprime()#se manda a llamar nuestra variable definada para que se imprima 

#SubClase

class Vip(Viaje): #se declara la subclase
    def __init__(self, Estancia, Destino, Precio):#se declara una varible definida se utiliza el self para especificar
        Viaje.__init__(self, Estancia, Destino)
        self.Precio = Precio

    def imprimeVip(self):
        print("\nWelcome VIP")#imprime el mensaje
        print("Tiempo de estancia: ", self.Estancia, "\nCon Destino a: ", self.Destino, "\nPrecio: ", self.Precio) #se imprime le mensaje y se le pone el self para llamr lo que queramos poner 


Viaje2 = Vip("2 Años", "España", "20,000")#ponemos el nombre del objeto y la clase y le inicializo con un valor 

Viaje2.imprimeVip() #se manda a llamar nuestra variable definada para que se imprima 



