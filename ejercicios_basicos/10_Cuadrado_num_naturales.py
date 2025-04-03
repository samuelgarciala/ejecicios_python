#10- Desarrollar un algoritmo que nos calcule el cuadrado de los 9 primeros números naturales.

def cuadrado_de_numeros_naturales_hasta_9():        
    for numeros_naturales in range(1,10):
        cuadrado=numeros_naturales**2
        print(f"El cuadrago del numero {numeros_naturales} es: ({cuadrado})")


def main():
    cuadrado_de_numeros_naturales_hasta_9()

main()

