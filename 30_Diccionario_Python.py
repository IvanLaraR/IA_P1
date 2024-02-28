
#Python tiene un tipo llamado diccionario, el cuál es capaz de almacenar en él una colección de objetos con claves y valores.

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
consulta = panaderia["Sabor"]#se declara una variable consulta que va ser igual al diccionario que llama al alemto deseado
print(consulta)#se imprime la variable

print("\n")

#se pueden llamar diferentes elementos a la vez 
consulta = panaderia["Sabor"],panaderia["precio"],panaderia2["Sabor"], panaderia2["precio"]#se declara una variable consulta que va ser igual al diccionario que llama al alemto deseado
print(consulta)#se imprime la variable

print("\n")

#se usa el metodo dict() para mostrar el diccionario

muestra = dict(panaderia)#se declara la varible y se llama al diccionario completo
print(muestra)#se imprime 
