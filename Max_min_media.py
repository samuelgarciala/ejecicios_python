#13- Algoritmo que lea números enteros hasta teclear 0, y nos muestre el máximo, el mínimo y la media de todos ellos.
#Piensa cómo debemos inicializar las variables.
lista_de_numeros=[]
contador=0
while True:
      
    print("""ingrese numero o ingrese "0" para sacar resultado de todos los numeros introducidos anteriormente""")
    numero_ingresado=float(input())
    if contador==0 and numero_ingresado== 0:
            print("no se ha intoducido nungun dato vuelva a empezar")
            numero_ingresado=None
          
    if numero_ingresado == 0:
        break
    
    lista_de_numeros.append(numero_ingresado)
    contador+=1
    
numero_maximo=max(lista_de_numeros)
numero_minimo=min(lista_de_numeros)
la_media=sum(lista_de_numeros)/len(lista_de_numeros)

print(f"el numero mayor es: {numero_maximo}.")
print(f"el numero menor es: {numero_minimo}.")
print(f"la media es: {la_media}.")

