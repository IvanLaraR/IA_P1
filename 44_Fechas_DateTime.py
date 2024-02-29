
#utilizar el modulo datetime para mostar la fecha actual

import datetime #se utiliza el modulo

Hoy = datetime.datetime.now() #se crea una varible y se le asigna el valor de la fecha y hora de ahora 

print(Hoy)#se imprime la variable

print("\n")

#como hacer una fecha personalizada
#año,mes y dia
FechaP = datetime.datetime(2024, 2, 29) #Se crea una varible y se le asigna el v alir del modulo el cual contiene el año,mes y dia

print(FechaP)

print("\n")
#año,mes,dia,hora,min,seg
FechaP2 = datetime.datetime(2024, 2, 29, 12, 26, 45) #Se crea una varible y se le asigna el v alir del modulo el cual contiene el año,mes y dia

print(FechaP2)#se imprime la variable 
