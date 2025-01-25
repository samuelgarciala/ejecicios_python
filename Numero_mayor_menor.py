#6- Algoritmo que lea dos números y nos diga cuál de ellos es mayor o bien si son iguales (recuerda usar la estructura
#condicional.

print("introduza el primer numero")
numero_1=int(input())
print("introduza el segundo numero")
numero_2=int(input())

if numero_1>numero_2:
    print(f"El numero {numero_1} es mayor que {numero_2}")
elif numero_2 == numero_1:
    print(f"Ambos numeros son iguales")
else:
    print(f"El numero {numero_2} es mayor que {numero_1}")
