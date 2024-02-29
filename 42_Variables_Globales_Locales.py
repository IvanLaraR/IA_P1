#Variables Locales y Globales

#Scope(alcance)

def obj(): #Creamos una funcion para dar valores adentro de la misma
    mensaje = "Mensaje dentro de la función" #A la variable se le asigna una valor que en este caso es el mansaje 
    print(mensaje)#se imprime el mensaje 

obj()#se manda a llamar el objeto

print("\n")

#Funciones Anidadas

def obj(): #Creamos una funcion para dar valores adentro de la misma
    mensaje = "Mensaje dentro de la función" #A la variable se le asigna una valor que en este caso es el mansaje 
    print(mensaje)#se imprime el mensaje 

    def obj2(): #se crea una Funcion anidada 
        mensaje = "Se modifico el mensaje" #se le asigna un nuevo valor a la variable 
        print(mensaje)#se imprime el mensaje

        
    obj2()#se manda a llamar el objeto de la funcion anidada
obj()#se manda a llamar el objeto

print("\n")

#Variable Global

var = "varibale fuera de la funcion" #se crea una variable global fuera de la funcion 

def obj(): #Creamos una funcion para dar valores adentro de la misma
   
    print(var)#se imprime el mensaje 

obj()#se manda a llamar el objeto

print("\n")
#Hacer variables locales a variables Globales con (global)

def funcion(): #se crea una funcion 
    global var1 #se variable se convierte a global
    var1 = "VARIABLE GLOBAL" #se le asigna un valor  a la variable

funcion()#se llama al objeto / funcion
print(var1)#se imprime

print("\n")







