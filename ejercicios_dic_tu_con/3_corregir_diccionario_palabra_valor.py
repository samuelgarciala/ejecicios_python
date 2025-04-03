
#3-Dada una lista de palabras, crea un diccionario donde las claves sean las palabras y los valores la cantidad de veces que aparecen.
lista=["jose","jose","jose","juan","juan","luis"]
diccionario ={}

for palabra_clave in lista:
    if palabra_clave in diccionario:
        diccionario[palabra_clave]=diccionario[palabra_clave]+1
    else:
        diccionario[palabra_clave] = 1
        
print(diccionario)
