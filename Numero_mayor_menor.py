#6- Algoritmo que lea dos números y nos diga cuál de ellos es mayor o bien si son iguales (recuerda usar la estructura
#condicional.
def mensaje_inicio():
    print("introduzca un numero")

def ingreso_de_numero():
    numero =int(input())
    return numero

def comparar_dos_numero(numero_1,numero_2):
    if numero_1>numero_2:
        print(f"El numero {numero_1} es mayor que {numero_2}")
    elif numero_2 == numero_1:
        print(f"Ambos numeros son iguales")
    else:
        print(f"El numero {numero_2} es mayor que {numero_1}")

def main():
    mensaje_inicio()
    numero_1=ingreso_de_numero()
    mensaje_inicio()
    numero_2=ingreso_de_numero()
    comparar_dos_numero(numero_1,numero_2)
    
main()