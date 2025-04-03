#18- Programa que lea 3 números de teclado y los muestre en pantalla de forma ordenada.
    
def ordenar_3_numeros(numeros):
    numero_mayor=None
    numero_medio=None
    numero_menor=None
    
    for numero in numeros:
        if numero_mayor is None or numero>numero_mayor:
            numero_menor=numero_medio
            numero_medio=numero_mayor
            numero_mayor=numero
        elif numero_medio is None or numero>numero_medio:
            numero_menor=numero_medio
            numero_medio=numero
        else:
            numero_menor=numero

    return [numero_menor,numero_medio,numero_mayor]

def main():
    numeros=[]
    for numero_ingresado in range (1,4):
        numero=int(input(f"introduzca {numero_ingresado}° numero: "))
        numeros.append(numero)
    
    lista_ordenada=ordenar_3_numeros(numeros)
    
    print(lista_ordenada)
    
main()

    
    