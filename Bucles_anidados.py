#21- Un programa posee tres bucles anidados, cuyas variables de control toman M, N y K valores respectivamente.
#Determinar cuántas veces se ejecutan las instrucciones del cuerpo del bucle más interno.

m=int(input())
n=int(input())
k=int(input())
contador=0
for i in range(m):
    for x in range(n):
        for y in range(k):
            contador +=1

print(f"el resultado de los bucles anidados son: {i+1} x {x+1} x {y+1} = {contador}")