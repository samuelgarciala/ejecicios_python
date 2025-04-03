#4 Diseña un programa que solicite al usuario su edad,
# y a continuación indique si es mayor o menor de edad.
def entrada_de_datos():
    print("introduzca su edad:")
    edad = int(input())
    return edad

def es_mayor_de_edad_si(edad):
    if edad>=18:
        print("es usted mayor de edad")
    else:
        print("es usted menor de edad")

def main():
    edad=entrada_de_datos()
    es_mayor_de_edad_si(edad)

main()

