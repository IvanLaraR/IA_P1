
#se puede modificar el valor de un diccionrio
panaderia = { #creo un diccionario con el nombre panaderia y usando {}
    "Tipo": "Pdulce", #añado un elemento con su atributo despues del :
    "Sabor": "chocolate",#añado un elemento con su atributo despues del :
    "precio": "20"#añado un elemento con su atributo despues del :
    
    }
panaderia2 = { #creo un diccionario con el nombre panaderia2 y usando {}
    "Tipo": "Pdulce", #añado un elemento con su atributo despues del :
    "Sabor": "fresa",#añado un elemento con su atributo despues del :
    "precio": "19"#añado un elemento con su atributo despues del :
    
    }
panaderia["precio"] = "30" #se declara uan lista y se le iguala a un valor numerico
print(panaderia["precio"]) #se imprime la lista con el numevo valor

print("\n")

#usar un bucle for en un diccionario 

panaderia = { #creo un diccionario con el nombre panaderia y usando {}
    "Tipo": "Pdulce", #añado un elemento con su atributo despues del :
    "Sabor": "chocolate",#añado un elemento con su atributo despues del :
    "precio": "20"#añado un elemento con su atributo despues del :
    
    }
panaderia2 = { #creo un diccionario con el nombre panaderia2 y usando {}
    "Tipo": "Pdulce", #añado un elemento con su atributo despues del :
    "Sabor": "fresa",#añado un elemento con su atributo despues del :
    "precio": "19"#añado un elemento con su atributo despues del :
    
    }
for x in panaderia: #se crea un bucle y se declara una variable x en la lista
    print(x)#se imprime la variable

print("\n")

#usar un bucle for en un diccionario para devolver sus valores 

panaderia = { #creo un diccionario con el nombre panaderia y usando {}
    "Tipo": "Pdulce", #añado un elemento con su atributo despues del :
    "Sabor": "chocolate",#añado un elemento con su atributo despues del :
    "precio": "20"#añado un elemento con su atributo despues del :
    
    }
panaderia2 = { #creo un diccionario con el nombre panaderia2 y usando {}
    "Tipo": "Pdulce", #añado un elemento con su atributo despues del :
    "Sabor": "fresa",#añado un elemento con su atributo despues del :
    "precio": "19"#añado un elemento con su atributo despues del :
    
    }
for x in panaderia:#se crea un bucle y se declara una variable x en la lista
    print(panaderia[x]) #se imprimr el valor de la variable y se le agrega el valor del diccionario



