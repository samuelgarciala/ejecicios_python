# notas={
#     "pepe":{
#         "matematica":5,
#         "castellano":4
#     },
#      "juan":{
#         "matematica":3,
#         "castellano":10
#     }
# }

# keys=list(notas.keys())
# values=list(notas.values())
# items=list(notas.items())

# notas_pepe=notas.get("pepe")

# #print(keys)
# print("-----")
# #print(values)
# print("-----")
# #print(items)

# notas_pepe_matematica=notas_pepe.get("matematica")
# print(notas_pepe_matematica)

# lista=[("pepe",36),("juan",40)]

# dicc=dict(lista)
# print(dicc)




#1- Sumar los valores de un diccionario.
def suma_de_valores_diccionario(diccionario):
    suma=0
    for clave in diccionario:
        suma += diccionario.get(clave)
    return suma

def suma_de_valores_diccionario_2(diccionario):
    suma=0
    for value in diccionario.values():
        suma += value
    return suma

def suma_de_valores_diccionario_3(diccionario):
    return sum(diccionario.values())
 
 
    












