diccionario={
    "jose":1,
    "juan":3,
    "luis":5
}
diccionario_2={}

for clave,valor in diccionario.items():
    diccionario_2[valor]=clave
    
print(diccionario_2)