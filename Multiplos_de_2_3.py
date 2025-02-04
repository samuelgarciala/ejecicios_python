#14- Algoritmo que visualice la cuenta de los números que son múltiplos de 2 o de 3 que hay entre 1 y 100.

def multiplos_de_2_3():
    contador_de_multiplos=0
    for i in range(1,101):
        if i%2==0 or i%3==0:
            contador_de_multiplos+=1
    return contador_de_multiplos
        
def salida_de_datos(contador_de_multiplos):
    print(f"el resultado es: {contador_de_multiplos}")
    
def main():
    contador_de_multiplos=multiplos_de_2_3()
    salida_de_datos(contador_de_multiplos)
    
main()