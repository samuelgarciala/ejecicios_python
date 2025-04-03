# 21- Un programa posee tres bucles anidados, cuyas variables de control toman M, N y K valores respectivamente.
#Determinar cuántas veces se ejecutan las instrucciones del cuerpo del bucle más interno.
m=2
n=3
k=4
contador=0

for i in range(m):
    for e in range(n):
        for x in range(k):
            contador+=1 
                    
print(contador)