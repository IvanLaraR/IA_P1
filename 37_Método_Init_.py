#utilizaremos le metodo _init_ es un método especial que podemos poner en las clases para establecer unos valores iniciales

class Viaje: #se crea una clase
    def __init__(self, Estancia, Destino):
        self.Estancia = Estancia #se crea una varible
        self.Destino = Destino #se crea una varible 

    def imprime(self): #se declara una varible definida se utiliza el self para especificar 
        print("Tiempo de estancia: ", self.Estancia, "\nCon Destino a: ", self.Destino) #se imprime le mensaje y se le pone el self para llamr lo que queramos poner 

airolinea = Viaje("2 Meses", "España") #creamos una varible y le asignamos el valor de la clase 

airolinea. imprime() #se manda a llamar nuestra variable definada para que se imprima 
