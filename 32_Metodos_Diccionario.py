#Contar elementos en un diccionario

panaderia = { #creo un diccionario con el nombre panaderia y usando {}
    "Tipo": "Pdulce", #añado un elemento con su atributo despues del :
    "Sabor": "chocolate",#añado un elemento con su atributo despues del :
    "precio": "20"#añado un elemento con su atributo despues del :
    
    }
print(len(panaderia)) #se imprime el diccionario con el método len para contar los elementos

print("\n")

#Eliminar todo o una parte del diccionario con el del

panaderia = { #creo un diccionario con el nombre panaderia y usando {}
    "Tipo": "Pdulce", #añado un elemento con su atributo despues del :
    "Sabor": "chocolate",#añado un elemento con su atributo despues del :
    "precio": "20"#añado un elemento con su atributo despues del :
    
    }
del panaderia["Sabor"]#se usa el método para elimar el elemento "Sabor" del diccionario
print(panaderia)#se imprime el diccioanrio

print("\n")
#Añadir nuevos elementos,claves y valores a un diccionario

panaderia = { #creo un diccionario con el nombre panaderia y usando {}
    "Tipo": "Pdulce", #añado un elemento con su atributo despues del :
    "Sabor": "chocolate",#añado un elemento con su atributo despues del :
    "precio": "20"#añado un elemento con su atributo despues del :
    
    }
panaderia["Tamaño"] = "Mediano" #se llama el diccionario y se le esta agregando una nueva clave y se iguala a un valor 
print(panaderia)#se imprime el diccionario 
