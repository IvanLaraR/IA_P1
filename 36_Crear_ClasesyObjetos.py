#Las clases se dividen en otras clases pero son clones de la principal

class Viaje: #se crea una clase 
    Estancia = "" #se crea una varible 
    Destino = "" #se crea una varible 

    def imprime(self): #se declara una varible definida se utiliza el self para especificar 
        print("Tiempo de estancia: ", self.Estancia, "\nCon Destino a: ", self.Destino) #se imprime le mensaje y se le pone el self para llamr lo que queramos poner 

airolinea = Viaje() #creamos una varible y le asignamos el valor de la clase 

airolinea.Estancia = "2 Meses" #se le asigna un valor a nuestro metodo self
airolinea.Destino = "España" # se le asigna un valor a nuestro metodo self 

airolinea. imprime() #se manda a llamar nuestra variable definada para que se imprima 
