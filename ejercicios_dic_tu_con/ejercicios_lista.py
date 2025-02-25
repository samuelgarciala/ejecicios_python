#1- Implementar una función que cuente la frecuencia de elementos en una lista.

def contador_de_frecuencia_elementos(lista,elemento):
    contador=0
    for elemento_lista in lista:
        if elemento == elemento_lista:
            contador+=1
    return contador

#2- Implementar una función que calcule la suma de los elementos de una lista numérica.

def suma_lista(lista):
    elemento_suma=0
    for elemento_lista in lista:
        elemento_suma+=elemento_lista
    return elemento_suma

#3- Implementar una función que elimine todas las ocurrencias de un elemento en una lista.

def eliminador_de_elementos(lista,elemento):
    lista_nueva=[]
    for elemento_lista in lista:
        if elemento != elemento_lista:
            lista_nueva.append(elemento_lista)
    return lista_nueva

#4- Implementar una función que permita extender una lista. La función debe recibir otra lista
#como parámetro y devolver la lista original con los elementos de la lista pasada como
#parámetro.

def extender_lista(lista_original,lista_copia):
    for elemento_lista in lista_copia:
        lista_original.append(elemento_lista)

#5- Implementar una función que permita copiar los elementos de una lista.

def copiar_lista(lista):
    lista_copia=[]
    for elemento_lista in lista:
        lista_copia.append(elemento_lista)
    
    return lista_copia


#6- Implementar una función que permita invertir los elementos de una lista.

def invertir_elementos(lista):
    nueva_lista=[]
    for i in range(len(lista) - 1, -1, -1):
        nueva_lista.append(lista[i])
    return nueva_lista

#7- Escriba una función que devuelva el máximo valor de una lista numérica.

def maximo_valor_lista(lista):
    if lista == []:
        return None
    
    numero_mayor = lista[0]
    for numero_lista in lista:
        if numero_lista > numero_mayor or numero_mayor==None:
            numero_mayor = numero_lista    
    return numero_mayor

#8- Crear una función que elimine los duplicados de una lista. Debe recibir una lista como parámetro y retorna una nueva lista sin elementos repetidos.

def eliminar_duplicados_lista(lista):
    lista_sin_duplicados=[]
    for numero in lista:
        if numero not in lista_sin_duplicados:
            lista_sin_duplicados.append(numero)
    
    return lista_sin_duplicados


#9- Crear una función que devuelva los números pares de una lista.

def numero_pares_lista(lista):
    lista_de_pares=[]
    for numero_lista in lista:
        if numero_lista % 2 == 0:
            lista_de_pares.append(numero_lista)
    
    return lista_de_pares

#10- Implementar una función que devuelva la intersección entre dos listas.

def encontrar_intersección_entre_dos_listas(lista_1,lista_2):
    lista_de_numeros_que_coinciden=[]
    for numero in lista_1:
        if numero in lista_2 and numero not in lista_de_numeros_que_coinciden:
            lista_de_numeros_que_coinciden.append(numero)
    
    return lista_de_numeros_que_coinciden



    


           
          

lista=[1,2,2]
lista2=[3,2,1]
lista_eliminar=encontrar_intersección_entre_dos_listas(lista,lista2)

print(lista_eliminar)
