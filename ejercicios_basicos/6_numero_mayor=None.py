#6- Algoritmo que lea dos números y nos diga cuál de ellos es mayor o bien si son iguales (recuerda usar la estructura
#condicional.
def mensaje_inicio():
    print("introduzca un numero")

def ingreso_de_numero():
    numero =int(input())
    return numero 

def comparar_tres_numeros(numero_1,numero_2,numero_3):
    if numero_1>=numero_2 and numero_1>=numero_3:
        numero_mayor=numero_1
        
        if numero_2>=numero_3:
            numero_medio=numero_2
            numero_menor=numero_3
        else:
            numero_medio=numero_3
            numero_menor=numero_2
            
    elif numero_2>=numero_1 and numero_2>=numero_3:
        numero_mayor=numero_2
        
        if numero_1>=numero_3:
            numero_medio=numero_1
            numero_menor=numero_3
        else:
            numero_medio=numero_3
            numero_menor=numero_1
    
    else:
        numero_mayor=numero_3
        
        if numero_1>=numero_2:
            numero_medio=numero_1
            numero_menor=numero_2
        else:
            numero_medio=numero_2
            numero_menor=numero_1
    
    return numero_mayor,numero_medio,numero_menor

def mensaje_salida(numero_mayor,numero_medio,numero_menor):
    print(f"el numero mayor es: {numero_mayor} ,numero medio es: {numero_medio}, numero menor {numero_menor}")

def main():
    mensaje_inicio()
    numero_1=ingreso_de_numero()
    mensaje_inicio()
    numero_2=ingreso_de_numero()
    mensaje_inicio()
    numero_3=ingreso_de_numero()
    numero_mayor,numero_medio,numero_menor=comparar_tres_numeros(numero_1,numero_2,numero_3)
    mensaje_salida(numero_mayor,numero_medio,numero_menor)
    
main()