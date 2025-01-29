numero_mayor=None
numero_medio=None
numero_menor=None

print("introducir primer numero")
numero_1=int(input())
print("introducir segundo numero")
numero_2=int(input())
print("introducir tercer numero")
numero_3=int(input())

if numero_1>numero_2 and numero_1>numero_3:
    numero_mayor=numero_1
    if numero_2>numero_3:
        numero_medio=numero_2
        numero_menor=numero_3
    else:
        numero_medio=numero_3
        numero_menor=numero_2

if numero_2>numero_1 and numero_2>numero_3:
    numero_mayor=numero_2
    if numero_1>numero_3:
        numero_medio=numero_1
        numero_menor=numero_3
    else:
        numero_medio=numero_3
        numero_menor=numero_1


if numero_3>numero_1 and numero_3>numero_2:
    numero_mayor=numero_3
    if numero_1>numero_2:
        numero_medio=numero_1
        numero_menor=numero_2
    else:
        numero_medio=numero_2
        numero_menor=numero_1
        
print(f"el numero mayor es: {numero_mayor} ,numero medio es: {numero_medio}, numero menor {numero_menor}")
