#24- Hacer un algoritmo que nos sume, los números naturales que sean pares, y menores que un número introducido por
#teclado.

numero_ingresado = int(input("ingrese numero:"))
suma=0

for i in range(numero_ingresado):
    if i%2==0:
        suma=i+suma
        
print(f"la suma de los enteros pares menor que {numero_ingresado} = {suma}")

    

