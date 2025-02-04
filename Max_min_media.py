#13- Algoritmo que lea números enteros hasta teclear 0, y nos muestre el máximo, el mínimo y la media de todos ellos.
#Piensa cómo debemos inicializar las variables.

def introduccion_de_datos_y_cierre_con_0():  
    contador=0
    
    while True:
        print("""ingrese numero o ingrese "0" para sacar resultado de todos los numeros introducidos anteriormente""")
        numero_ingresado=float(input())
        if contador==0 and numero_ingresado== 0:
                print("no se ha intoducido nungun dato vuelva a empezar")
                numero_ingresado=None
            
        if numero_ingresado == 0:
            break
        
        lista_de_numeros.append(numero_ingresado)
        contador+=1
    return lista_de_numeros

def calcular_maximo(lista_de_numeros):
    numero_maximo=max(lista_de_numeros)
    return numero_maximo

def calcular_minimo(lista_de_numeros):
    numero_minimo=min(lista_de_numeros)
    return numero_minimo

def calcular_media(lista_de_numeros):
    la_media=sum(lista_de_numeros)/len(lista_de_numeros)
    return la_media

def salida_de_datos(numero_maximo,numero_minimo,la_media):
    print(f"el numero mayor es: {numero_maximo}.")
    print(f"el numero menor es: {numero_minimo}.")
    print(f"la media es: {la_media}.")

def main():
    lista_de_numeros=introduccion_de_datos_y_cierre_con_0()
    numero_maximo=calcular_maximo(lista_de_numeros)
    numero_minimo=calcular_minimo(lista_de_numeros)
    la_media=calcular_media(lista_de_numeros)
    salida_de_datos(numero_maximo,numero_minimo,la_media)

lista_de_numeros=[]
main()