#11- Se pide representar el algoritmo que nos calcule la suma de los N primeros números naturales. N se leerá por
#teclado.
print("---------------------------")
numero = int(input("introduzca el numero N: "))
print("---------------------------")

suma=1
for i in range(1,numero+1):
    suma = suma+i
    
    print(f"{i} sumado con {suma-i} da como resultado: {suma}")
