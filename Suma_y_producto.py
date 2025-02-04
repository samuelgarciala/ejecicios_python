#7- Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo, debe imprimir el producto de los
#tres y si no lo es, imprimirá la suma.
def mensaje_de_numeros(mensaje):
    print(mensaje)

def entrada_de_datos():
    numero=float(input())
    return numero

def comprobacion_de_datos(primer_numero,segundo_numero,tercer_numero):
    if primer_numero<0:
        resultado_de_suma_o_producto=primer_numero*segundo_numero*tercer_numero
        
        return resultado_de_suma_o_producto
    else:
        resultado_de_suma_o_producto=primer_numero+segundo_numero+tercer_numero
       
        return resultado_de_suma_o_producto
    
def mensaje_de_salida(resultado_de_suma_o_producto,primer_numero,segundo_numero,tercer_numero):
    if resultado_de_suma_o_producto==(primer_numero+segundo_numero+tercer_numero):
        print(f"la suma de los numeros es :{resultado_de_suma_o_producto}")
    else:
        print(f"el producto de los numeros es :{resultado_de_suma_o_producto}")
        
def main():
    mensaje_de_numeros("introduzca primer numero")
    numero_1=entrada_de_datos()
    mensaje_de_numeros("introduzca segundo numero")
    numero_2=entrada_de_datos()
    mensaje_de_numeros("introduzca tercer numero")
    numero_3=entrada_de_datos()
    suma_o_producto_de_datos=comprobacion_de_datos(numero_1,numero_2,numero_3)
    mensaje_de_salida(suma_o_producto_de_datos,numero_1,numero_2,numero_3)

main()

    
    

    

