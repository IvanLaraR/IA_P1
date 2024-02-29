#self es como el this en otros lenguajes de programación

class Viaje: #se crea una clase
    def __init__(self, Estancia, Destino):
        self.Estancia = Estancia #se crea una varible
        self.Destino = Destino #se crea una varible 

    def imprime(self): #se declara una varible definida se utiliza el self para especificar 
        print("Tiempo de estancia: ", self.Estancia, "\nCon Destino a: ", self.Destino) #se imprime le mensaje y se le pone el self para llamr lo que queramos poner 

airolinea = Viaje("2 Meses", "España") #creamos una varible y le asignamos el valor de la clase 
airolinea2 = Viaje("1 año", "Suecia")#ponemos el nombre del objeto y la clase y le inicializo con un valor 
airolinea2.Destino = "Canada" #ponemos el nombre del objeto punto y el nombre del argmento que queremos cambiar su valor 

airolinea2.imprime() #se manda a llamar nuestra variable definada para que se imprima


