
#Super Clases

class Viaje: #se crea una clase
    def __init__(self, Estancia, Destino): #se declara una varible definida se utiliza el self para especificar
        self.Estancia = Estancia #se crea una varible
        self.Destino = Destino #se crea una varible 

    def imprime(self): #se declara una varible definida se utiliza el self para especificar 
        print("Tiempo de estancia: ", self.Estancia, "\nCon Destino a: ", self.Destino) #se imprime le mensaje y se le pone el self para llamr lo que queramos poner 

#SubClase

class Vip(Viaje): #se declara la subclase
    def One(self):#se declara una varible definida se utiliza el self para especificar
        print("\nWelcome VIP")#imprime el mensaje 

PM = Viaje("1 año", "Canada")#ponemos el nombre del objeto y la clase y le inicializo con un valor 
PM2 = Vip("Trajeta Platino", "Tarjeta Oro")#ponemos el nombre del objeto y la clase y le inicializo con un valor 

PM.imprime() #se manda a llamar nuestra variable definada para que se imprima 
PM2.One() #se manda a llamar nuestra variable definada para que se imprima 
PM2.imprime() #se manda a llamar nuestra variable definada para que se imprima 


