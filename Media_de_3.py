#2 - Realizar un programa que calcule la media aritmética de tres valores que se han leído de teclado,
# y muestre el resultado por pantalla.
def texto_inicio():
        print(f"ingrese sus 3 numeros")
        
        
def ingreso_de_numero():
    numero =int(input())
    return numero

def la_media(numero_1,numero_2,numero_3):
    media = (numero_1+numero_2+numero_3)/3
    return media

def salida_de_datos(media):
    print(f"la media de los tres numeros es:{media}")
    
def main():
    texto_inicio()
    numero_1 = ingreso_de_numero()
    numero_2 = ingreso_de_numero()
    numero_3 = ingreso_de_numero()
    media=la_media(numero_1,numero_2,numero_3)
    salida_de_datos(media)
    
main()
    
    