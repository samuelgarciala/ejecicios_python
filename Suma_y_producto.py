#7- Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo, debe imprimir el producto de los
#tres y si no lo es, imprimirá la suma.

print("Introduzca el primer numero")
primer_numero=float(input())
print("Introduzca el segundo numero")
segundo_numero=float(input())
print("Introduzca el tercer numero")
tercer_numero=float(input())

if primer_numero<0:
    producto_de_numeros=primer_numero*segundo_numero*tercer_numero
    print(f"el producto de los numeros es :{producto_de_numeros}")
else:
    suma_de_numeros=primer_numero+segundo_numero+tercer_numero
    print(f"la suma de los numeros es :{suma_de_numeros}")
    

