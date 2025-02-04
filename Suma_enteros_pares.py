#24- Hacer un algoritmo que nos sume, los números naturales que sean pares, y menores que un número introducido por
#teclado.
def suma_de_los_enteros(numero_ingresado):
    suma=0
    for i in range(numero_ingresado):
        if i%2==0:
            suma=i+suma
    return suma

def salida_de_datos(numero_ingresado,suma):
    print(f"la suma de los enteros pares menor que {numero_ingresado} = {suma}")
    
def entrada_de_datos():
        numero_ingresado = int(input("ingrese numero:"))
        return numero_ingresado

def main():
    numero_ingresado=entrada_de_datos()
    suma=suma_de_los_enteros(numero_ingresado)
    salida_de_datos(numero_ingresado,suma)
    
main()
