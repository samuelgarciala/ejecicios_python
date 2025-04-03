#6- Verificar si una lista contiene elementos repetidos.

def devolver_si_tiene_elementos_repetidos(lista):  
    lista_set=set(lista)
    if len(lista) != len(lista_set):
        return True
    else:
        return False

def main():
    lista=[1,2,3,4,5]
    tiene_repedidos=devolver_si_tiene_elementos_repetidos(lista)
    if tiene_repedidos == True:
        print("La lista tiene elementos repetidos")
    else:
        print("La lista no tiene elementos repetidos")

main()