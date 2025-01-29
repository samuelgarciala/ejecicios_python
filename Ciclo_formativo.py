#9- Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo de grado superior o no. Para acceder
#a un grado superior, si se tiene un título de bachiller, en caso de no tenerlo, se puede acceder si hemos superado una
#prueba de acceso.


intentos=0
entrada_titulo_correcta=False

while intentos<3 and entrada_titulo_correcta==False:
    intentos=intentos+1
    print("Tiene un titulo de bachiller, si o no?")
    tiene_titulo_bachiller= input()
    if tiene_titulo_bachiller=="si":
        print("puede recibir el ciclo formativo")
        raise SystemExit
    elif tiene_titulo_bachiller=="no":
        entrada_titulo_correcta=True
        
    else:
        entrada_titulo_correcta=False
        print("ha introducido un valor incorrecto")
        if intentos==3:
            print("cerrando programa")
            raise SystemExit

intentos2=0

while intentos2<3:
    intentos2=intentos2+1
    
    print("ha aprovado la prueba de acceso si o no?")
    prueva_de_acceso= input()
    
    if prueva_de_acceso == "si":
        print("puede recibir el ciclo formativo")
        break
    
    elif prueva_de_acceso == "no":
        print("no puede recibir el ciclo formativo")
        break
    
    else:
        
            print("ha introducido un valor incorrecto")

print("cerrando el programa")


