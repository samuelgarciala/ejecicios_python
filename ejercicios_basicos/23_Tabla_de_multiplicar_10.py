#23- Programa que imprima la tabla de multiplicar de un número entero (entre 1 y 10).

def mensaje_de_ingreso():
    print("ingrese el numero que quiere obtener su tabla de multiplicar")
    
def entrada_de_datos():
    numero_ingresado = int(input())
    return numero_ingresado

def multiplicar_i_del_1_al_10(numero_ingresado):
    for i in range(1,11):
        if numero_ingresado==i:
            resultado_1=1*i    
            resultado_2=2*i
            resultado_3=3*i
            resultado_4=4*i
            resultado_5=5*i
            resultado_6=6*i
            resultado_7=7*i
            resultado_8=8*i
            resultado_9=9*i
            resultado_10=10*i
            
            print (f"0x{i} = 0")
            print (f"1x{i} = {resultado_1}")
            print (f"2x{i} = {resultado_2}")
            print (f"3x{i} = {resultado_3}")
            print (f"4x{i} = {resultado_4}")
            print (f"5x{i} = {resultado_5}")
            print (f"6x{i} = {resultado_6}")
            print (f"7x{i} = {resultado_7}")
            print (f"8x{i} = {resultado_8}")
            print (f"9x{i} = {resultado_9}")
            print (f"10x{i} = {resultado_10}")
            
def main():
    mensaje_de_ingreso()
    numero_ingresado=entrada_de_datos()
    multiplicar_i_del_1_al_10(numero_ingresado)

main()
