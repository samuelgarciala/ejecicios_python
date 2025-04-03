#11- Se pide representar el algoritmo que nos calcule la suma de los N primeros números naturales. N se leerá por
#teclado.

def ingreso_de_datos():
    numero = int(input("introduzca el numero N: "))
    return numero
    

def calcular_suma(numero):
    suma=0
    for i in range(1,numero+1):
        suma = suma+i
    return suma

def salida_datos(suma):
    print(f"{suma}")

def main():
    numero = ingreso_de_datos()
    suma = calcular_suma(numero)
    salida_datos(suma)
    
main()
