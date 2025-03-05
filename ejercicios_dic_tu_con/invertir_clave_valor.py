#4- Dado un diccionario, invierte sus claves y valores.

diccionario={
    "jose":1,
    "juan":3,
    "luis":5
}
diccionario_2={}

for clave in diccionario:
    valor = diccionario[clave]
    diccionario_2[valor] = clave
    
print(diccionario_2)