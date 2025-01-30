#14- Algoritmo que visualice la cuenta de los números que son múltiplos de 2 o de 3 que hay entre 1 y 100.
contador_de_multiplos=0


for i in range(1,101):
    if i%2==0 or i%3==0:
        contador_de_multiplos+=1
        
print(f"el resultado es: {contador_de_multiplos}")